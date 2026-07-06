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

from qgis.core import QgsSettings
from qgis.PyQt.QtCore import QFileSystemWatcher
from qgis.PyQt.QtWidgets import QApplication
from qgis.gui import QgsMessageBar
import os
import re

app = QApplication.instance()
s = QgsSettings()
watch = QFileSystemWatcher()
watch.fileChanged.connect(lambda path: reloadStyle(path))


def reloadStyle(path):
    """Reload a QSS stylesheet from disk, fixing relative image paths."""
    watch.removePaths(watch.files())
    watch.addPath(path)
    with open(path, "r") as f:
        stylesheet = f.read()
        dirPath = os.path.dirname(path).replace("\\", "/")
        stylesheet = re.sub(r"url\((.*?)\)", r'url("{}/\1")'.format(dirPath), stylesheet)
        app.setStyleSheet(stylesheet)
        app.processEvents()


def setExampleStyles(name, path):
    """Register an example style in QgsSettings."""
    s.setValue(f"myStyles/{name}/name", name)
    s.setValue(f"myStyles/{name}/path", path)


def setActivated(name):
    """Set the currently activated style name."""
    s.setValue("myStyles/Activated", name)


def getActivated():
    """Get the currently activated style name, clearing if file missing."""
    activated = s.value("myStyles/Activated", "")
    if activated:
        _, path = getStyle(activated)
        if not path or not os.path.exists(path):
            setActivated("")
            return ""
    return activated


def setPreview(name):
    """Set the currently previewed style name."""
    s.setValue("myStyles/Preview", name)


def getPreview():
    """Get the currently previewed style name."""
    return s.value("myStyles/Preview", "")


def getStyle(name):
    """Get name and path for a style by name."""
    return (s.value(f"myStyles/{name}/name", ""), s.value(f"myStyles/{name}/path", ""))


def getStyleList():
    """Get list of registered style names, removing those with missing files."""
    validStyles = []
    try:
        s.beginGroup("myStyles")
        for name in s.childGroups():
            s.beginGroup(name)
            path = s.value("path", "")
            s.endGroup()
            if path and os.path.exists(path):
                validStyles.append(name)
            else:
                s.remove(f"{name}/name")
                s.remove(f"{name}/path")
                s.remove(name)
    except Exception:
        return []
    finally:
        s.endGroup()
    return validStyles


def addNewStyle(name, path):
    """Add or update a user style in QgsSettings."""
    s.setValue(f"myStyles/{name}/name", name)
    s.setValue(f"myStyles/{name}/path", path)


def delStyle(name):
    """Delete a style from QgsSettings."""
    s.remove(f"myStyles/{name}/name")
    s.remove(f"myStyles/{name}/path")


def activateStyle(name, iface, preview=False, close=False):
    """Activate or preview a style, applying it to the application."""
    styleName, path = getStyle(name)

    if not styleName or not path:
        watch.removePaths(watch.files())
        app.setStyleSheet("")
        return

    watch.removePaths(watch.files())
    iface.messageBar().clearWidgets()

    if not os.path.exists(path):
        iface.messageBar().pushMessage(
            f"Error: {path}",
            "The path to the .qss does not exist. Load default style.",
            level=QgsMessageBar.CRITICAL,
            duration=2,
        )
        app.setStyleSheet("")
        return

    if close:
        return

    reloadStyle(path)

    if preview:
        setPreview(styleName)
        iface.messageBar().pushMessage(
            f"Style {styleName}: ",
            "Style Preview loaded correctly.",
            level=QgsMessageBar.INFO,
            duration=2,
        )
    else:
        setActivated(styleName)
        iface.messageBar().pushMessage(
            f"Style {styleName}: ", "Style loaded correctly.", level=QgsMessageBar.INFO, duration=2
        )
