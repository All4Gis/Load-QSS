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
        
        # Load UI file
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(plugin_dir, 'ui.resources', 'About.ui')
        uic.loadUi(ui_file, self)
