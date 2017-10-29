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
 #   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from .AboutQSSDialog import AboutQSSDialog
from .LoadQSSDialog import LoadQSSDialog
from LoadQSS.utils.utils import *
from qgis.PyQt.QtCore import Qt
import LoadQSS.gui.generated.resources_rc
import os

try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

# try:
#     from pydevd import *
# except ImportError:
#     None


class LoadQSS:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(os.path.abspath(__file__))

        # Examples
        ExampleStyles = {
            "Dark": "darkstyle.qss",
            "machinery": "machinery.qss",
            "DarkOrange": "DarkOrange.qss",
            "light": "light.qss",
            "Minimalist": "Minimalist.qss",
            "Wombat": "stylesheet.qss",
            "Dark Blue (FreeCAD)": "stylesheet.qss",
            "Dark Green (FreeCAD)": "stylesheet.qss",
            "Dark Orange (FreeCAD)": "stylesheet.qss",
            "Light Blue (FreeCAD)": "stylesheet.qss",
            "Light Green (FreeCAD)": "stylesheet.qss",
            "Light Orange (FreeCAD)": "stylesheet.qss",
            "BlueGlass": "blueglass.qss",
            "Coffee": "coffee.qss"
        }

        for k, v in ExampleStyles.items():
            setExampleStyles(k, self.to_exmples_folder(k, v))

        try:
            # Activate last style
            activateStyle(getActivated(), self.iface)
        except Exception:
            None

    # Copy style to examples plugin folder
    def to_exmples_folder(self, folder, stylesheet):
        return os.path.join(self.plugin_dir, "examples", folder, stylesheet)

    def initGui(self):
        self.action = QAction(QIcon(":/imgQss/images/icon.png"),
                              u"Load QSS - UI themes", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Load QSS - UI themes", self.action)

        self.actionAbout = QAction(QIcon(":/imgQss/images/info.png"),
                                   u"About", self.iface.mainWindow())
        self.iface.addPluginToMenu(u"&Load QSS - UI themes", self.actionAbout)
        self.actionAbout.triggered.connect(self.About)

    def unload(self):
        self.iface.removePluginMenu(u"&Load QSS - UI themes", self.action)
        self.iface.removePluginMenu(u"&Load QSS - UI themes", self.actionAbout)
        self.iface.removeToolBarIcon(self.action)

    def About(self):
        self.About = AboutQSSDialog(self.iface)
        self.About.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.About.exec_()

    def run(self):
        self.dlg = LoadQSSDialog(self.iface)
        self.dlg.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.dlg.exec_()
