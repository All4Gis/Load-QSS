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
import os
import pickle
import re
from qgis.core import *
from qgis.gui import QgsMessageBar
from qgis.utils import iface

try:
    import sys
    from pydevd import *
except:
    None;


def reload_style(path):
    # TODO WAT?!
    watch.removePaths(watch.files())
    watch.addPath(path)
    with open(path, "r") as f:
        stylesheet = f.read()
        # Update the image paths to use full paths. Fixes image loading in styles
        path = os.path.dirname(path).replace("\\", "/")
        stylesheet = re.sub(r'url\((.*?)\)', r'url("{}/\1")'.format(path), stylesheet)
        QApplication.instance().setStyleSheet(stylesheet)


watch = QFileSystemWatcher()
watch.fileChanged.connect(reload_style)

# Set style list
def setStyleList(StyleList):
    s = QSettings()
    s.setValue('myStyles/StyleList', pickle.dumps(StyleList))


def setActivated(Name):
    s = QSettings()
    s.remove('myStyles/Activated')
    s.setValue('myStyles/Activated', pickle.dumps(Name))


# GetStyle row
def getStyle(Name):
    s = QSettings()
    StyleList = getStyleList()
    if Name in StyleList:
        name = s.value('myStyles/%s/name' % Name)
        path = s.value('myStyles/%s/path' % Name)
    else:
        name = []
        path = []
    return (name, path)


# Get myStyles list
def getStyleList():
    s = QSettings()
    try:
        StyleList = pickle.loads(s.value('myStyles/StyleList'))
    except:
        StyleList = []
    return (StyleList)


# Get Activated
def getActivated():
    s = QSettings()
    try:
        Activated = pickle.loads(s.value('myStyles/Activated'))
    except:
        Activated = []
    return (Activated)


# Create or update
def setStyle(Name, path):
    StyleList = getStyleList()
    nStyleList = list(set([Name] + StyleList))
    setStyleList(nStyleList)
    s = QSettings()
    s.setValue('myStyles/%s/name' % Name, Name)
    s.setValue('myStyles/%s/path' % Name, path)


# Delete Style
def delStyle(Name):
    # settrace()
    s = QSettings()
    StyleList = getStyleList()
    if Name in StyleList:
        StyleList.remove(Name)
        setStyleList(StyleList)
        # path = s.value('myStyles/%s/path' % Name)
        s.remove('myStyles/%s/name' % Name)
        s.remove('myStyles/%s/path' % Name)


# try:
#             os.remove(path)
#         except:
#             None


# Activate a specified style
def activateStyle(Name, iface):
    name, path = getStyle(Name)
    app = QApplication.instance()
    if not os.path.exists(path):
        iface.messageBar().pushMessage("Error: ", "The path to the * .qss not exist.Load default style ",
                                       level=QgsMessageBar.CRITICAL, duration=3)
        app.setStyleSheet("")
    else:
        reload_style(path)
        iface.messageBar().pushMessage("Info: ", "Style loaded correctly.", level=QgsMessageBar.INFO, duration=3)
        setActivated(name)

