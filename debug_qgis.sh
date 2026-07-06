#!/bin/bash
set -e

export FRAN_DEBUG=1

# Ensure debugpy is installed in QGIS profile's python dir
QGIS_PYTHON_DIR="$HOME/Library/Application Support/QGIS/QGIS4/profiles/default/python"
if [ ! -d "$QGIS_PYTHON_DIR/debugpy" ]; then
    echo "Installing debugpy into QGIS profile..."
    pip3 install --target="$QGIS_PYTHON_DIR" debugpy 2>/dev/null || {
        echo "Error: Could not install debugpy"
        echo "Run manually: pip3 install --target=\"$QGIS_PYTHON_DIR\" debugpy"
        exit 1
    }
fi

QGIS_BIN="/Applications/QGIS.app/Contents/MacOS/QGIS-final-4_0_0"

if [ ! -x "$QGIS_BIN" ]; then
    echo "Error: QGIS binary not found at $QGIS_BIN"
    exit 1
fi

echo "======================================"
echo " LoadQSS DEBUG MODE"
echo "======================================"
echo ""
echo "Starting QGIS with debug mode..."
echo ""

exec "$QGIS_BIN"
