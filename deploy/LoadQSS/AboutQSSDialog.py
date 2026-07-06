# -*- coding: utf-8 -*-
import os
from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDialog

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))


class AboutQSSDialog(QDialog):
    def __init__(self):
        """Initialize the About dialog with plugin info and sample images."""
        QDialog.__init__(self)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowCloseButtonHint)
        uic.loadUi(os.path.join(PLUGIN_DIR, "ui", "aboutQSSDialog.ui"), self)

        images_dir = os.path.join(PLUGIN_DIR, "images")
        html = self.textBrowser.toHtml()
        for name in ("icon.png", "sample0.png", "sample1.png"):
            html = html.replace(
                f"../images/{name}",
                f'file:///{os.path.join(images_dir, name).replace(chr(92), "/")}',
            )
        self.textBrowser.setHtml(html)
