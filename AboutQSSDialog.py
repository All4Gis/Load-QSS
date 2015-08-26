# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadQSS
                                 A QGIS plugin
 Configure look and feel
                             -------------------
        begin                : 2015-04-29
        copyright            : (C) 2015 All4Gis.
        email                : franka1986@gmail.com
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os.path
from qgis.core import *
from qgis.gui import *

from PyQt4 import QtCore, QtGui

from gui.generated.About import Ui_About
from utils.utils import *


try:
    import sys
    from pydevd import *
except:
    None;


class AboutQSSDialog(QtGui.QDialog, Ui_About):
    def __init__(self, iface):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        
