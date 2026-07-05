#!/bin/bash

set -e

PLUGIN_NAME="Load-QSS"

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
PLUGIN_SOURCE="$REPO_ROOT"

# Detect QGIS profile path
QGIS_PROFILE="$HOME/Library/Application Support/QGIS/QGIS4/profiles/default"
if [ ! -d "$QGIS_PROFILE" ]; then
    echo "Error: QGIS profile not found at $QGIS_PROFILE"
    echo "Make sure QGIS 4 is installed."
    exit 1
fi

PLUGIN_DIR="$QGIS_PROFILE/python/plugins"

if [ ! -f "$PLUGIN_SOURCE/metadata.txt" ]; then
    echo "Error: Plugin source not found at $PLUGIN_SOURCE"
    echo "Are you running this from the project root?"
    exit 1
fi

echo "======================================"
echo " $PLUGIN_NAME DEV INSTALL"
echo "======================================"

mkdir -p "$PLUGIN_DIR"

# Remove previous installation if it exists
if [ -L "$PLUGIN_DIR/$PLUGIN_NAME" ]; then
    rm "$PLUGIN_DIR/$PLUGIN_NAME"
elif [ -d "$PLUGIN_DIR/$PLUGIN_NAME" ]; then
    echo "Warning: Removing existing plugin directory"
    rm -rf "$PLUGIN_DIR/$PLUGIN_NAME"
fi

# Create symlink
ln -s "$PLUGIN_SOURCE" "$PLUGIN_DIR/$PLUGIN_NAME"

echo ""
echo "Plugin linked correctly:"
ls -l "$PLUGIN_DIR/$PLUGIN_NAME"

echo ""
echo "Now open QGIS and use Plugin Reloader"
