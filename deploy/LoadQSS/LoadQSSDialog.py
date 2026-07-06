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
 *   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMessageBox
from qgis.gui import QgsMessageBar
from .aboutQSSDialog import AboutQSSDialog
from .utils.utils import (
    getStyleList,
    getPreview,
    getActivated,
    activateStyle,
    setActivated,
    delStyle,
    addNewStyle,
)
import os

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))


class LoadQSSDialog(QDialog):
    def __init__(self, iface):
        """Initialize the theme manager dialog with UI elements."""
        QDialog.__init__(self)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowCloseButtonHint)
        self.iface = iface

        uiFile = os.path.join(PLUGIN_DIR, "ui", "loadQSSDialog.ui")
        uic.loadUi(uiFile, self)

        iconPath = os.path.join(PLUGIN_DIR, "images", "icon.png")
        if os.path.exists(iconPath):
            self.setWindowIcon(QIcon(iconPath))

        self.lastOpenedFile = None
        self.app = QApplication.instance()
        self.listStyles.addItems(getStyleList())
        self.currentItem = None

    def about(self):
        """Display the About dialog with plugin information."""
        dlg = AboutQSSDialog()
        dlg.exec()

    def selectRow(self, checked):
        """Handle list item selection and enable/disable action buttons."""
        if checked:
            self.deleteBtn.setEnabled(True)
            self.activateBtn.setEnabled(True)
            self.currentItem = checked
            self.applyStyle(preview=True)
        else:
            self.deleteBtn.setEnabled(False)
            self.activateBtn.setEnabled(False)
            self.currentItem = None

    def addStyle(self):
        """Import a new QSS file and add it to the style list."""
        filename, _ = QFileDialog.getOpenFileName(self, "Open qss", self.lastOpenedFile, "*.qss")
        if not filename:
            return

        flags = Qt.WindowType.WindowSystemMenuHint | Qt.WindowType.WindowTitleHint
        text, ok = QInputDialog.getText(self, "Style Name", "Enter name for Style:", flags=flags)
        if not ok:
            return

        if not text:
            self.iface.messageBar().clearWidgets()
            self.iface.messageBar().pushMessage(
                "Error: ", "Enter theme name.", level=QgsMessageBar.CRITICAL, duration=3
            )
            return

        self.listStyles.addItem(text)
        addNewStyle(text, filename)

    def deleteStyle(self):
        """Remove the selected style from the list and settings."""
        try:
            styleName = self.currentItem.text()
            isActive = styleName == getActivated()
            isPreview = styleName == getPreview()

            if isActive or isPreview:
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowIcon(QIcon(os.path.join(PLUGIN_DIR, "images", "info.png")))
                msgBox.setWindowTitle("Delete Style: " + styleName)
                msgBox.setText(
                    "This style is currently active. It will be removed and the default QGIS style will be set.\n"
                    "Are you sure?"
                )
                msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                msgBox.setDefaultButton(QMessageBox.StandardButton.No)
                ret = msgBox.exec()
                if ret == QMessageBox.StandardButton.Yes:
                    self.resetStyle()
                else:
                    return
        except AttributeError:
            pass

        self.listStyles.takeItem(self.listStyles.currentRow())
        delStyle(self.currentItem.text())
        self.deleteBtn.setEnabled(False)
        self.activateBtn.setEnabled(False)
        self.currentItem = None

    def applyStyle(self, preview=False):
        """Apply the selected style to QGIS, optionally as preview only."""
        try:
            activateStyle(self.currentItem.text(), self.iface, preview)
        except AttributeError:
            pass

    def resetStyle(self):
        """Reset to default QGIS style by clearing the stylesheet."""
        self.app.setStyleSheet("")
        setActivated("")

    def closeEvent(self, evt):
        """Restore the active style when the dialog is closed."""
        activateStyle(getActivated(), self.iface, close=True)
