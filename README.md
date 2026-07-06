# Load QSS - UI Themes

Change the look and feel of QGIS with custom Qt stylesheets.

## Features

- Apply any `.qss` stylesheet to QGIS
- Live preview when selecting themes
- Add your own custom styles
- Auto-reload when editing `.qss` files (great for theme development)
- Auto-discover themes from `examples/` folder
- Persists your last active style across sessions

## Adding Your Own Themes

Drop a folder with a `.qss` file inside `examples/` and it will appear automatically in the plugin:

```
examples/
└── My Theme/
    ├── my_theme.qss
    └── icons/          (optional)
        └── icon.png
```

## Installation

### From QGIS Plugin Manager

1. Open QGIS
2. Go to **Plugins > Manage and Install Plugins**
3. Search for **Load QSS**
4. Click **Install Plugin**

### From GitHub Release

1. Download the latest `.zip` from [Releases](https://github.com/All4Gis/Load-QSS/releases)
2. In QGIS: **Plugins > Manage and Install Plugins > Install from ZIP**
3. Select the downloaded file

## Development

### Quick Dev Install (symlink)

```bash
./install_dev.sh
```

Creates a symlink in the QGIS plugins directory. Use [Plugin Reloader](https://github.com/borysiasty/plugin_reloader) for live reload.

### Build Release

```bash
# Validate project
python3 build.py

# Create optimized plugin zip
python3 deploy/plugin_zip.py
```

The deploy script:
- Excludes dev files (`.git`, `build.py`, `*.sh`, etc.)
- Quantizes PNG images (saves ~200 KB)
- Strips Python comments and docstrings

### CI/CD

Push a tag to create a GitHub Release with the plugin zip:

```bash
git tag v1.5.0
git push origin v1.5.0
```

## Project Structure

```
LoadQSS/
├── __init__.py              # Plugin entry point (classFactory)
├── loadQSS.py               # Main plugin class (auto-discovers themes)
├── loadQSSDialog.py         # Theme selector dialog
├── aboutQSSDialog.py        # About dialog
├── metadata.txt             # QGIS plugin metadata
├── utils/
│   ├── __init__.py
│   └── utils.py             # Style management (QgsSettings)
├── ui/
│   ├── loadQSSDialog.ui     # Main dialog UI
│   └── aboutQSSDialog.ui    # About dialog UI
├── images/                  # Plugin icons (icon.png, info.png, samples)
├── examples/                # QSS themes
├── deploy/
│   └── plugin_zip.py        # Release zip builder (PNG optimize, strip comments)
├── build.py                 # Build validation (metadata, structure, syntax)
├── install_dev.sh           # Dev symlink installer
├── setup_qgis_dev.sh        # Full dev setup
├── uninstall_dev.sh         # Remove dev install
└── .github/workflows/
    ├── ci.yml               # CI pipeline
    └── plugin-deploy.yml    # Release automation
```

## License

GPL v3 - See [LICENSE](LICENSE)

## ❤️ Support this project

If this project has been useful to you, you can support its development by making a donation.

[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-0070BA?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=X2JMP4FMHDYQS)

## Author

Francisco Raga ([All4Gis](https://github.com/All4Gis)) - franka1986@gmail.com
