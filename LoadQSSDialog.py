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
# Import the PyQt and QGIS libraries
from qgis.PyQt.QtCore import Qt
import os
from PyQt5.QtWidgets import QDialog

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
import shutil
 
from .AboutQSSDialog import AboutQSSDialog
from LoadQSS.gui.generated.Load_QSS import Ui_LoadQSSDialog
from LoadQSS.utils.utils import *


try:
    import sys
    from pydevd import *
except:
    None;
 
class LoadQSSDialog(QDialog, Ui_LoadQSSDialog):
    def __init__(self, iface):
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.lastOpenedFile = None
        self.app = QApplication.instance()
        self.plugin_dir = os.path.dirname(os.path.abspath(__file__))
        
        ExampleStyles = dict()
        
        ExampleStyles = {
            "Dark" : "darkstyle.qss",  
            "machinery" : "machinery.qss",  
            "DarkOrange" : "DarkOrange.qss",  
            "light" : "light.qss",  
            "Minimalist" : "Minimalist.qss",  
            "Wombat" : "stylesheet.qss",  
            "Dark Blue (FreeCAD)" : "stylesheet.qss",  
            "Dark Green (FreeCAD)" : "stylesheet.qss",  
            "Dark Orange (FreeCAD)" : "stylesheet.qss",  
            "Light Blue (FreeCAD)" : "stylesheet.qss",  
            "Light Green (FreeCAD)" : "stylesheet.qss",  
            "Light Orange (FreeCAD)" : "stylesheet.qss",
            "BlueGlass" : "blueglass.qss"
        }

        for k,v in ExampleStyles.items():
            setStyle(k, self.to_exmples_folder(k, v))
 
 
        self.listStyles.addItems(getStyleList())
        self.currentItem = None
 
        
    #Copy style to examples plugin folder

    def to_exmples_folder(self, folder, stylesheet):
        return os.path.join(self.plugin_dir, "examples", folder, stylesheet)
 
    # About
    def About(self):
        self.About = AboutQSSDialog(self.iface)
        #self.About.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.About.exec_()
 

    # Selected row
    def SelectRow(self, checked):
        if checked:
            self.Delete_btn.setEnabled(True)
            self.Activate_btn.setEnabled(True)
            self.currentItem = checked
            self.ApplyStyle(preview = True)#Preview style.
        else:
            self.Delete_btn.setEnabled(False)
            self.Activate_btn.setEnabled(False)
            self.currentItem = None

    # Add new qss
    def AddStyle(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, "Open qss", self.lastOpenedFile, "*.qss")
        if len(self.filename) != 0:
            flags = Qt.WindowSystemMenuHint | Qt.WindowTitleHint
            text, ok = QInputDialog.getText(self, 'Style Name', 'Enter name for Style:', flags=flags)
            if ok:
                if text == "":
                    self.iface.messageBar().pushMessage("Error: ", "Enter theme name.", level=QgsMessageBar.CRITICAL,
                                                        duration=3)
                    return

                # Se anade al listado
                self.listStyles.addItem(text)
                setStyle(text, self.filename)

        return
 
    # Remove style in list
    def DeleteStyle(self):
        try:
            if(self.currentItem.text()== getPreview()):
 
                if (self.currentItem.text()==getActivated()):
                    ret = QtGui.QMessageBox.question(self, self.tr('Delete Style : '+self.currentItem.text()),
                        self.tr('The style you are about to remove is your active style.\nThe default Qgis style will be set.\nAre you sure you want to remove it?'),
                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if ret == QMessageBox.Yes:
                        self.ResetStyle()
                    if ret == QMessageBox.No:
                        return   
                else:
                    activateStyle(getActivated(), self.iface)    
        except Exception as e:
            None
 
        self.listStyles.takeItem(self.listStyles.currentRow())
        delStyle(self.currentItem.text())
        StyleList = getStyleList()
        self.Delete_btn.setEnabled(False)
        self.Activate_btn.setEnabled(False)
        self.currentItem = None
        
        return

    # Apply style
    def ApplyStyle(self,preview=False):
        try:
            activateStyle(self.currentItem.text(), self.iface,preview)
        except:
            None
        return

    # Restores style
    def ResetStyle(self):
        self.app.setStyleSheet("")
        setActivated("")
        return
    
    # Close dialog
    def closeEvent(self, evt):
        activateStyle(getActivated(), self.iface) 
        return
