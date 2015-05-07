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
from PyQt4 import QtCore, QtGui
from gui.generated.Load_QSS import Ui_LoadQSSDialog
from utils.utils import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os.path
 
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
        self.lastOpenedFile=None
        self.app = QApplication.instance() 
        self.plugin_dir = os.path.dirname(__file__);

        setStyle("Dark Style", self.plugin_dir + "\\examples\\Dark\\Dark.qss")
        setStyle("Machinery Style",  self.plugin_dir + "\\examples\\machinery\\qmc2-machinery-0.3.qss")
 
        self.listStyles.addItems(getStyleList())
        self.currentItem = None
        
    #Selected row
    def SelectRow(self,checked):
        if checked:
            self.Delete_btn.setEnabled(True)
            self.Activate_btn.setEnabled(True) 
            self.currentItem = checked
        else:
            self.Delete_btn.setEnabled(False)
            self.Activate_btn.setEnabled(False)
            self.currentItem = None
 
    #Add new qss           
    def AddStyle(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self,"Open qss",self.lastOpenedFile,"*.qss" )
        if len(self.filename)!=0:
            flags = Qt.WindowSystemMenuHint | Qt.WindowTitleHint
            text, ok = QInputDialog.getText(self, 'Style Name', 'Enter name for Style:',flags=flags)
            if ok:
                self.listStyles.addItem(text)
                setStyle(text, self.filename)
        return
 
    #Remove style in list 
    def  DeleteStyle(self):      
        self.listStyles.takeItem(self.listStyles.currentRow())
        delStyle(self.currentItem.text())
        StyleList = getStyleList()
        if len(StyleList)==0:
            self.Delete_btn.setEnabled(False)
            self.Activate_btn.setEnabled(False)
            self.currentItem = None 
        return
    
    #Apply style
    def  ApplyStyle(self):
        activateStyle(self.currentItem.text(),self.iface)
        return
    
    #Restores style 
    def ResetStyle(self):
        self.app.setStyleSheet("") 
        setActivated("")
        return