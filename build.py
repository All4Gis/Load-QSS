#!/usr/bin/env python3
# coding: utf-8
"""Build script for Load QSS plugin.

Validates project structure and metadata before release.
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent


def validateMetadata():
    """Validate metadata.txt has required fields."""
    metadata = ROOT_DIR / "metadata.txt"
    if not metadata.exists():
        print(f"Error: {metadata} not found")
        return False

    content = metadata.read_text(encoding="utf-8")
    required = ["name", "version", "qgisMinimumVersion"]
    for field in required:
        if f"{field}=" not in content:
            print(f"Error: metadata.txt missing '{field}'")
            return False

    print("  metadata.txt OK")
    return True


def validateStructure():
    """Validate required files exist."""
    requiredFiles = [
        "__init__.py",
        "LoadQSS.py",
        "LoadQSSDialog.py",
        "AboutQSSDialog.py",
        "metadata.txt",
        "images/icon.png",
    ]
    for f in requiredFiles:
        if not (ROOT_DIR / f).exists():
            print(f"Error: missing {f}")
            return False

    print("Project structure OK")
    return True


def validatePythonSyntax():
    """Check Python files for syntax errors."""
    pyFiles = list[Path](ROOT_DIR.glob("*.py")) + list[Path](ROOT_DIR.glob("utils/*.py"))
    for py in pyFiles:
        try:
            compile(py.read_text(encoding="utf-8"), str(py), "exec")
        except SyntaxError as e:
            print(f"Error: {py.name}: {e}")
            return False

    print("  Python syntax OK")
    return True


def main():
    """Main build function."""
    print("=" * 50)
    print("Load QSS Build")
    print("=" * 50)

    checks = [
        ("Metadata", validateMetadata),
        ("Structure", validateStructure),
        ("Syntax", validatePythonSyntax),
    ]

    for name, fn in checks:
        print(f"\n[{name}]")
        if not fn():
            sys.exit(1)

    print("\n" + "=" * 50)
    print("Build completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
