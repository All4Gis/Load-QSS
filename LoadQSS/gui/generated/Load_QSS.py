# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\Load_QSS_dialog_base.ui'
#
# Created: Thu May 07 21:36:46 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoadQSSDialog(object):
    def setupUi(self, LoadQSSDialog):
        LoadQSSDialog.setObjectName(_fromUtf8("LoadQSSDialog"))
        LoadQSSDialog.resize(307, 174)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoadQSSDialog.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(LoadQSSDialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listStyles = QtGui.QListWidget(LoadQSSDialog)
        self.listStyles.setAlternatingRowColors(True)
        self.listStyles.setObjectName(_fromUtf8("listStyles"))
        self.horizontalLayout.addWidget(self.listStyles)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Add_btn = QtGui.QPushButton(LoadQSSDialog)
        self.Add_btn.setEnabled(True)
        self.Add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add_btn.setObjectName(_fromUtf8("Add_btn"))
        self.verticalLayout.addWidget(self.Add_btn)
        self.Delete_btn = QtGui.QPushButton(LoadQSSDialog)
        self.Delete_btn.setEnabled(False)
        self.Delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_btn.setObjectName(_fromUtf8("Delete_btn"))
        self.verticalLayout.addWidget(self.Delete_btn)
        self.Activate_btn = QtGui.QPushButton(LoadQSSDialog)
        self.Activate_btn.setEnabled(False)
        self.Activate_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Activate_btn.setObjectName(_fromUtf8("Activate_btn"))
        self.verticalLayout.addWidget(self.Activate_btn)
        self.Default_btn = QtGui.QPushButton(LoadQSSDialog)
        self.Default_btn.setObjectName(_fromUtf8("Default_btn"))
        self.verticalLayout.addWidget(self.Default_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(LoadQSSDialog)
        QtCore.QObject.connect(self.Add_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.AddStyle)
        QtCore.QObject.connect(self.Delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.DeleteStyle)
        QtCore.QObject.connect(self.Activate_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.ApplyStyle)
        QtCore.QObject.connect(self.Default_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.ResetStyle)
        QtCore.QObject.connect(self.listStyles, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), LoadQSSDialog.SelectRow)
        QtCore.QMetaObject.connectSlotsByName(LoadQSSDialog)

    def retranslateUi(self, LoadQSSDialog):
        LoadQSSDialog.setWindowTitle(_translate("LoadQSSDialog", "Load QSS", None))
        self.Add_btn.setText(_translate("LoadQSSDialog", "Add", None))
        self.Delete_btn.setText(_translate("LoadQSSDialog", "Delete", None))
        self.Activate_btn.setText(_translate("LoadQSSDialog", "Activate", None))
        self.Default_btn.setText(_translate("LoadQSSDialog", "Default", None))

import resources_rc
