# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\Load_QSS_dialog_base.ui'
#
# Created: Mon May 23 17:16:57 2016
#      by: PyQt4 UI code generator 4.10
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
        LoadQSSDialog.resize(385, 392)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgQss/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoadQSSDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(LoadQSSDialog)
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_About = QtGui.QPushButton(LoadQSSDialog)
        self.btn_About.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_About.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_About.setStyleSheet(_fromUtf8("text-align:left;"))
        self.btn_About.setFlat(True)
        self.btn_About.setObjectName(_fromUtf8("btn_About"))
        self.horizontalLayout_2.addWidget(self.btn_About)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listStyles = QtGui.QListWidget(LoadQSSDialog)
        self.listStyles.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.Default_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Default_btn.setObjectName(_fromUtf8("Default_btn"))
        self.verticalLayout.addWidget(self.Default_btn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(LoadQSSDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)

        self.retranslateUi(LoadQSSDialog)
        QtCore.QObject.connect(self.Add_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.AddStyle)
        QtCore.QObject.connect(self.Delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.DeleteStyle)
        QtCore.QObject.connect(self.Default_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.ResetStyle)
        QtCore.QObject.connect(self.listStyles, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), LoadQSSDialog.SelectRow)
        QtCore.QObject.connect(self.Activate_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.ApplyStyle)
        QtCore.QObject.connect(self.btn_About, QtCore.SIGNAL(_fromUtf8("clicked()")), LoadQSSDialog.About)
        QtCore.QMetaObject.connectSlotsByName(LoadQSSDialog)

    def retranslateUi(self, LoadQSSDialog):
        LoadQSSDialog.setWindowTitle(_translate("LoadQSSDialog", "Load QSS - UI themes", None))
        self.btn_About.setText(_translate("LoadQSSDialog", "About", None))
        self.Add_btn.setText(_translate("LoadQSSDialog", "Add", None))
        self.Delete_btn.setText(_translate("LoadQSSDialog", "Delete", None))
        self.Activate_btn.setText(_translate("LoadQSSDialog", "Activate", None))
        self.Default_btn.setText(_translate("LoadQSSDialog", "Default", None))
        self.label.setText(_translate("LoadQSSDialog", "We provide some styles as an example to show the personalizing capabilities of the interface. Some styles may have elements that can be improved. Therefore, we encourage you to improve them or to create your own designs.", None))

import resources_rc
