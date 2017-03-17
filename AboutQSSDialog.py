# -*- coding: utf-8 -*-
"""
/***************************************************************************
IdentityTool
                                 A QGIS plugin
 Configure look and feel
                             -------------------
        begin                : 2015-04-29
        copyright            : (C) 2016 All4Gis.
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
# Import the PyQt and QGIS libraries
from qgis.PyQt.QtCore import Qt

import os

try:
    from qgis.core import Qgis
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    from PyQt5 import uic
    QT_VERSION=5
    os.environ['QT_API'] = 'pyqt5'
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4 import uic
    QT_VERSION=4
    
import os.path
from qgis.core import *
from qgis.gui import *
 
from LoadQSS.gui.generated.About import Ui_About
from LoadQSS.utils.utils import *


try:
    import sys
    from pydevd import *
except:
    None;

from PyQt5.QtWidgets import QDialog

class AboutQSSDialog(QDialog, Ui_About):
    def __init__(self, iface):
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface