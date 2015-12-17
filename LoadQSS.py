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

from AboutQSSDialog import AboutQSSDialog
from LoadQSSDialog import LoadQSSDialog
import gui.generated.resources_rc
from utils.utils import *


class LoadQSS:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'LoadQSS_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Activate last style
        try:
            activateStyle(str(getActivated()), self.iface)
        except:
            None

    def initGui(self):
        self.action = QAction(QIcon(":/imgQss/images/icon.png"), u"Load QSS - UI themes", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Load QSS - UI themes", self.action)

        self.actionAbout = QAction(QIcon(":/imgQss/images/info.png"), u"About", self.iface.mainWindow())
        self.iface.addPluginToMenu(u"&Load QSS - UI themes", self.actionAbout)
        self.actionAbout.triggered.connect(self.About)


    def unload(self):
        self.iface.removePluginMenu(u"&Load QSS - UI themes", self.action)
        self.iface.removePluginMenu(u"&Load QSS - UI themes", self.actionAbout)
        self.iface.removeToolBarIcon(self.action)

    def About(self):
        self.About = AboutQSSDialog(self.iface)
        self.About.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.About.exec_()
        return

    def run(self):
        self.dlg = LoadQSSDialog(self.iface)
        self.dlg.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.dlg.exec_()
        
        
