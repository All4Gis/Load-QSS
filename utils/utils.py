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
    # Some applications will remove a file and rewrite it.  QFileSystemWatcher will
    # ignore the file if the file handle goes away so we have to keep adding it.
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

# Set preview styles
def setPreview(Name):
    s = QSettings()
    s.remove('myStyles/Preview')
    s.setValue('myStyles/Preview', pickle.dumps(Name))
    return

# Get preview styles
def getPreview():
    s = QSettings()
    try:
        Preview = pickle.loads(s.value('myStyles/Preview'))
    except:
        Preview = []
    return (Preview)
    
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
    s = QSettings()
    StyleList = getStyleList()
    if Name in StyleList:
        StyleList.remove(Name)
        setStyleList(StyleList)
        # path = s.value('myStyles/%s/path' % Name)
        s.remove('myStyles/%s/name' % Name)
        s.remove('myStyles/%s/path' % Name)
 

# Activate a specified style
def activateStyle(Name, iface,preview=False):
    
    name, path = getStyle(Name)
    app = QApplication.instance()
    watch.removePaths(watch.files())
    if not os.path.exists(path):
        iface.messageBar().pushMessage("Error: ", "The path to the * .qss not exist.Load default style ",
                                       level=QgsMessageBar.CRITICAL, duration=3)
        app.setStyleSheet("")
    else:
        reload_style(path)
        iface.messageBar().pushMessage("Info: ", "Style loaded correctly.", level=QgsMessageBar.INFO, duration=3)
        if preview==False:
            setActivated(name)
        else:
            setPreview(name)

