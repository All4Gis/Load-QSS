# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadQSS
                                 A QGIS plugin
 Configure look and feel
                             -------------------
        begin                : 2015-04-29
        copyright            : (C) 2015 All4Gis.
        email                : franka1986 at gmail dot com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.core import QgsMessageLog, Qgis
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QApplication
from .aboutQSSDialog import AboutQSSDialog
from .loadQSSDialog import LoadQSSDialog
from .utils import PLUGIN_DIR
from .utils.utils import getActivated, activateStyle, setExampleStyles, setActivated
import os


def _discoverStyles(examplesDir):
    """Scan examples/ and return {folder_name: qss_path} for each theme."""
    styles = {}
    if not os.path.isdir(examplesDir):
        return styles
    for folder in sorted(os.listdir(examplesDir)):
        folderPath = os.path.join(examplesDir, folder)
        if not os.path.isdir(folderPath):
            continue
        for f in os.listdir(folderPath):
            if f.endswith(".qss"):
                styles[folder] = os.path.join(folderPath, f)
                break
    return styles


PLUGIN_MENU = "&Load QSS - UI themes"


class LoadQSS:
    def __init__(self, iface):
        """Initialize the plugin with QGIS interface reference."""
        self.iface = iface

        examplesDir = os.path.join(PLUGIN_DIR, "examples")
        for name, path in _discoverStyles(examplesDir).items():
            setExampleStyles(name, path)

    def initGui(self):
        """Create toolbar icons and menu entries for the plugin."""
        iconPath = os.path.join(PLUGIN_DIR, "images", "icon.png")
        infoIconPath = os.path.join(PLUGIN_DIR, "images", "info.png")

        self.action = QAction(QIcon(iconPath), "Load QSS - UI themes", self.iface.mainWindow())
        self.action.setObjectName("mLoadQSS")
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(PLUGIN_MENU, self.action)

        self.actionAbout = QAction(QIcon(infoIconPath), "About", self.iface.mainWindow())
        self.actionAbout.triggered.connect(self.showAbout)
        self.iface.addPluginToMenu(PLUGIN_MENU, self.actionAbout)

        self.iface.initializationCompleted.connect(self.startupStyleCheck)

    def startupStyleCheck(self):
        """Apply the previously activated style when QGIS starts."""
        try:
            savedStyle = getActivated()
            if savedStyle:
                activateStyle(savedStyle, self.iface)
        except Exception as e:
            level = Qgis.MessageLevel.Warning if hasattr(Qgis, "MessageLevel") else Qgis.Warning
            QgsMessageLog.logMessage(f"LoadQSS Startup Error: {e}", "LoadQSS", level)

    def unload(self):
        """Remove plugin menu items, toolbar icons, and reset to default style."""
        self.iface.removePluginMenu(PLUGIN_MENU, self.action)
        self.iface.removePluginMenu(PLUGIN_MENU, self.actionAbout)
        self.iface.removeToolBarIcon(self.action)
        # Reset to default style
        app = QApplication.instance()
        if app:
            app.setStyleSheet("")
        setActivated("")

    def showAbout(self):
        """Open the About dialog window."""
        dlg = AboutQSSDialog()
        dlg.exec()

    def run(self):
        """Open the main LoadQSS dialog for theme selection."""
        dlg = LoadQSSDialog(self.iface)
        dlg.exec()
