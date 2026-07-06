#!/usr/bin/env python3
# coding: utf-8
"""Create QGIS Plugin Zip for upload to QGIS Repository."""

from configparser import ConfigParser
from fnmatch import fnmatch
from pathlib import Path
import ast
import os
import shutil
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
OUTPUT_DIR = SCRIPT_DIR / "Output"

# Directories and patterns to exclude from the plugin zip
EXCLUDE_PATTERNS = [
    # Directories
    "__pycache__",
    ".settings",
    "deploy",
    ".git",
    ".github",
    # File patterns
    "*.json",
    "*.sh",
    "*.bat",
    "*.pyc",
    "*.bak",
    "*.yml",
    "*.ps1",
    ".gitignore",
    ".gitattributes",
    "build.py",
    "LICENSE",
    "README.md",
]


def optimizePngs(directory):
    """Optimize PNG images using Pillow (lossy reduction)."""
    try:
        from PIL import Image
    except ImportError:
        print("  [skip] Pillow not installed, PNG optimization skipped")
        return 0

    saved = 0
    for png in Path(directory).rglob("*.png"):
        originalSize = png.stat().st_size
        try:
            img = Image.open(png)
            if img.mode == "RGBA":
                img = img.quantize(colors=256, method=2).convert("RGBA")
            else:
                img = img.quantize(colors=256, method=2).convert("RGB")
            img.save(png, optimize=True)
            newSize = png.stat().st_size
            saved += originalSize - newSize
        except Exception:
            pass
    return saved


def stripPythonComments(directory):
    """Strip comments and docstrings from Python files."""
    saved = 0
    for py in Path(directory).rglob("*.py"):
        originalSize = py.stat().st_size
        try:
            content = py.read_text(encoding="utf-8")
            tree = ast.parse(content)
            docstringLines = set()
            for node in ast.walk(tree):
                if isinstance(
                    node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)
                ):
                    if (node.body and isinstance(
                        node.body[0], ast.Expr
                    ) and isinstance(
                        node.body[0].value, (ast.Constant, ast.Str)
                    )):
                        docstringLines.add(node.body[0].lineno)

            lines = content.splitlines(keepends=True)
            newLines = []
            inDocstring = False
            docstringQuote = None

            for i, line in enumerate(lines, 1):
                stripped = line.strip()

                if not inDocstring and i in docstringLines:
                    for quote in ('"""', "'''"):
                        if quote in stripped:
                            count = stripped.count(quote)
                            if count == 1:
                                inDocstring = True
                                docstringQuote = quote
                                break
                            elif count >= 2:
                                break
                    if inDocstring:
                        continue

                if inDocstring:
                    if docstringQuote in stripped:
                        inDocstring = False
                    continue

                if stripped.startswith("#"):
                    continue

                newLines.append(line)

            newContent = "".join(newLines)
            if newContent != content:
                py.write_text(newContent, encoding="utf-8")
                newSize = py.stat().st_size
                saved += originalSize - newSize
        except (SyntaxError, Exception):
            pass
    return saved


def makeIgnoreFn(patterns):
    """Return a shutil.copytree ignore function."""

    def ignore(directory, contents):
        """Filter out files matching any of the given patterns."""
        return {name for name in contents if any(fnmatch(name, p) for p in patterns)}

    return ignore


def copyProjectStructure(patterns):
    """Copy project structure excluding dev/CI artifacts."""
    print("Copying structure...")
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    shutil.copytree(ROOT_DIR, OUTPUT_DIR, ignore=makeIgnoreFn(patterns))
    print(f"  -> {OUTPUT_DIR}")


def optimizeAssets(directory):
    """Optimize images and strip Python comments in copied directory."""
    print("Optimizing assets...")
    totalSaved = 0

    saved = optimizePngs(directory)
    if saved > 0:
        print(f"  PNGs: saved {saved / 1024:.1f} KB")
        totalSaved += saved

    saved = stripPythonComments(directory)
    if saved > 0:
        print(f"  Python: saved {saved / 1024:.1f} KB")
        totalSaved += saved

    if totalSaved > 0:
        print(f"  Total saved: {totalSaved / 1024:.1f} KB")
    else:
        print("  No optimization applied")


def createZip(sourceDir, zipPath):
    """Create a zip archive from sourceDir."""
    print(f"Creating {zipPath.name}...")
    shutil.make_archive(str(zipPath.with_suffix("")), "zip", sourceDir)
    print(f"  -> {zipPath}")


def createZipWithFolder(sourceDir, zipPath, folderName):
    """Create a zip archive with sourceDir contents inside folderName."""
    print(f"Creating {zipPath.name}...")
    import zipfile
    with zipfile.ZipFile(zipPath, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(sourceDir):
            for file in files:
                filePath = Path(root) / file
                arcname = os.path.join(folderName, os.path.relpath(filePath, sourceDir))
                zipf.write(filePath, arcname)
    print(f"  -> {zipPath}")


def main():
    """Main build function."""
    metadata = ROOT_DIR / "metadata.txt"
    if not metadata.exists():
        print(f"Error: {metadata} not found")
        sys.exit(1)

    cp = ConfigParser()
    with metadata.open() as f:
        cp.read_file(f)

    if not cp.has_option("general", "name") or not cp.has_option("general", "version"):
        print("Error: metadata.txt missing required fields")
        sys.exit(1)

    pluginName = "LoadQSS"

    copyProjectStructure(EXCLUDE_PATTERNS)
    optimizeAssets(OUTPUT_DIR)
    zipPath = OUTPUT_DIR.parent / f"{pluginName}.zip"
    createZipWithFolder(OUTPUT_DIR, zipPath, pluginName)
    shutil.rmtree(OUTPUT_DIR)

    zipSize = zipPath.stat().st_size / 1024
    print(f"\n  Plugin zip: {zipPath.name} ({zipSize:.1f} KB)")
    print("Done.")


if __name__ == "__main__":
    main()
