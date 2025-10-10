# -*- coding: utf-8 -*-
"""
/***************************************************************************
IdentityTool
                                 A QGIS plugin
 Configure look and feel
                             -------------------
        begin                : 2015-04-29
        copyright            : (C) 2016 All4Gis.
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
import os
from qgis.PyQt import uic
from .utils.utils import *
from qgis.core import *
from qgis.gui import *

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *

try:
    from pydevd import *
except ImportError:
    None


class AboutQSSDialog(QDialog):
    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        
        # Load UI at runtime for Qt6 compatibility
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(plugin_dir, 'ui.resources', 'About.ui')
        uic.loadUi(ui_file, self)
        
        # Fix window icon for Qt6 compatibility - override resource path
        icon_path = os.path.join(plugin_dir, "images", "info.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            
        # Fix embedded images in the text browser for Qt6 compatibility
        self._fix_resource_paths(plugin_dir)
    
    def _fix_resource_paths(self, plugin_dir):
        """Convert Qt resource paths to absolute file paths in the text browser"""
        if hasattr(self, 'textBrowser'):
            html = self.textBrowser.toHtml()
            # Replace resource paths with absolute paths
            html = html.replace(':/imgQss/images/icon.png', 
                              'file:///' + os.path.join(plugin_dir, 'images', 'icon.png').replace('\\', '/'))
            html = html.replace(':/imgQss/images/ScreenShot0.png', 
                              'file:///' + os.path.join(plugin_dir, 'images', 'ScreenShot0.png').replace('\\', '/'))
            html = html.replace(':/imgQss/images/ScreenShot1.png', 
                              'file:///' + os.path.join(plugin_dir, 'images', 'ScreenShot1.png').replace('\\', '/'))
            self.textBrowser.setHtml(html)
