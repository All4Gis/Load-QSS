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
 #   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from qgis.PyQt.QtCore import Qt
from qgis.core import *
from qgis.gui import QgsMessageBar
from qgis.utils import iface
import os
import re

try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import QApplication
except ImportError:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *


# try:
#     from pydevd import *
# except ImportError:
#     None

app = QApplication.instance()
s = QSettings()
# s.remove('myStyles')


# Reload style (Watcher)
def reload_style(path):
    # Some applications will remove a file and rewrite it.  QFileSystemWatcher will
    # ignore the file if the file handle goes away so we have to keep adding it.
    watch.removePaths(watch.files())
    watch.addPath(path)
    with open(path, "r") as f:
        stylesheet = f.read()
        # Update the image paths to use full paths. Fixes image loading in styles
        path = os.path.dirname(path).replace("\\", "/")
        stylesheet = re.sub(r'url\((.*?)\)', r'url("{}/\1")'.format(path),
                            stylesheet)
        app.setStyleSheet(stylesheet)
        app.processEvents()


watch = QFileSystemWatcher()
watch.fileChanged.connect(reload_style)


# Set Activated style
def setActivated(Name):
    s.setValue('myStyles/Activated', Name)


# GetStyle row
def getStyle(Name):
    try:
        name = s.value('myStyles/%s/name' % Name)
        path = s.value('myStyles/%s/path' % Name)
    except Exception:
        name = ""
        path = ""
    return (name, path)


# Get myStyles list
def getStyleList():
    StyleList = []
    try:
        s.beginGroup("myStyles")
        StyleList = s.childGroups()
        s.endGroup()
    except Exception:
        None
    return StyleList


# Get Activated
def getActivated():
    try:
        Activated = s.value('myStyles/Activated')
    except Exception:
        Activated = ""
    return Activated


# Set preview styles
def setPreview(Name):
    s.setValue('myStyles/Preview', Name)
    return


# Get preview styles
def getPreview():
    try:
        Preview = s.value('myStyles/Preview')
    except Exception:
        Preview = ""
    return Preview


# Add Examples Styles
def setExampleStyles(Name, path):
    s.setValue('myStyles/%s/name' % Name, Name)
    s.setValue('myStyles/%s/path' % Name, path)


# Create or update
def AddNewStyle(Name, path):
    s.setValue('myStyles/%s/name' % Name, Name)
    s.setValue('myStyles/%s/path' % Name, path)


# Delete Style
def delStyle(Name):
    try:
        s.remove('myStyles/%s/name' % Name)
        s.remove('myStyles/%s/path' % Name)
    except Exception:
        None


# Activate/Preview a specified style
def activateStyle(Name, iface, preview=False, close=None):
    name, path = getStyle(Name)
    if name == "" or name is None:
        app.setStyleSheet("")
        return

    watch.removePaths(watch.files())
    iface.messageBar().clearWidgets()

    if path == "" or path is None:
        app.setStyleSheet("")
        return

    if not os.path.exists(path):
        iface.messageBar().pushMessage("Error: "+path+" : ",
                                       "The path to the * .qss not exist.Load default style ",
                                       level=QgsMessageBar.CRITICAL,
                                       duration=2)
        app.setStyleSheet("")
        return

    if close is not None:
        return
    else:
        reload_style(path)
        if preview is False:
            setActivated(name)
            iface.messageBar().pushMessage("Style "+name+" : ", "Style loaded correctly.",
                                           level=QgsMessageBar.INFO, duration=2)
            return
        else:
            setPreview(name)
            iface.messageBar().pushMessage("Style "+name+" : ", "Style Preview loaded correctly.",
                                           level=QgsMessageBar.INFO, duration=2)
            return
