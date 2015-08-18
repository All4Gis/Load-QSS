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
import shutil

from PyQt4 import QtCore, QtGui

from AboutQSSDialog import AboutQSSDialog
from gui.generated.Load_QSS import Ui_LoadQSSDialog
from utils.utils import *


try:
    import sys
    from pydevd import *
except:
    None;
 
class LoadQSSDialog(QtGui.QDialog, Ui_LoadQSSDialog):
    def __init__(self, iface):      
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.lastOpenedFile = None
        self.app = QApplication.instance() 
        self.plugin_dir = os.path.dirname(__file__);

        setStyle("Dark Style", self.plugin_dir + "\\examples\\Dark\\darkstyle.qss")
        setStyle("Machinery Style", self.plugin_dir + "\\examples\\machinery\\machinery.qss")
        setStyle("Dark Orange", self.plugin_dir + "\\examples\\DarkOrange\\DarkOrange.qss")
        setStyle("light", self.plugin_dir + "\\examples\\light\\light.qss")
        setStyle("Minimalist", self.plugin_dir + "\\examples\\Minimalist\\Minimalist.qss")
 
        self.listStyles.addItems(getStyleList())
        self.currentItem = None
        self.AddAboutButton() 
    
    # About
    def about(self):
        self.About = AboutQSSDialog(self.iface)
        self.About.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint) 
        self.About.exec_()
        return
    
    def AddAboutButton(self):
        layout = QVBoxLayout()
        toolBar = QToolBar(self)
        toolBar.addAction(u"About", self.about)
        toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        toolBar.setStyleSheet("QToolBar {border-bottom: 0px solid grey }")
        toolBar.setInputMethodHints(QtCore.Qt.ImhNone)
        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        toolBar.setFloatable(False)
        layout.addWidget(toolBar)
        layout.setMargin(0)
        layout.setSpacing(0)
        layout.addStretch(0)
        self.setLayout(layout)
        return
       
    # Selected row
    def SelectRow(self, checked):
        if checked:
            self.Delete_btn.setEnabled(True)
            self.Activate_btn.setEnabled(True) 
            self.currentItem = checked
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
                    self.iface.messageBar().pushMessage("Error: ", "Enter theme name.", level=QgsMessageBar.CRITICAL, duration=3) 
                    return 
 
                # Se anade al listado
                self.listStyles.addItem(text)
                setStyle(text, self.filename)
         
        return
 
    # Remove style in list 
    def  DeleteStyle(self):  
            
        self.listStyles.takeItem(self.listStyles.currentRow())
        delStyle(self.currentItem.text())
        StyleList = getStyleList()
        self.Delete_btn.setEnabled(False)
        self.Activate_btn.setEnabled(False)
        self.currentItem = None 
 
        return
    
    # Apply style
    def  ApplyStyle(self):
        try:
            activateStyle(self.currentItem.text(), self.iface)
        except:
            None   
        return
        
    # Restores style 
    def ResetStyle(self):
        self.app.setStyleSheet("") 
        setActivated("")
        return
