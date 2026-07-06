#!/bin/bash

set -e

PLUGIN_NAME="Load-QSS"
PLUGIN_DIR="$HOME/Library/Application Support/QGIS/QGIS4/profiles/default/python/plugins/$PLUGIN_NAME"

echo "======================================"
echo " $PLUGIN_NAME DEV UNINSTALL"
echo "======================================"

if [ ! -e "$PLUGIN_DIR" ] && [ ! -L "$PLUGIN_DIR" ]; then
    echo "Plugin not installed. Nothing to remove."
    exit 0
fi

if [ -L "$PLUGIN_DIR" ]; then
    rm "$PLUGIN_DIR"
    echo "Symlink removed."
elif [ -d "$PLUGIN_DIR" ]; then
    rm -rf "$PLUGIN_DIR"
    echo "Plugin directory removed."
fi

echo ""
echo "$PLUGIN_NAME uninstalled successfully."
