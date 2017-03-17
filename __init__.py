# -*- coding: utf-8 -*-
import sys

try:
    sys.path.append("X:/eclipse/plugins/org.python.pydev_5.5.0.201701191708/pysrc")
except:
    None

def classFactory(iface):
    from .LoadQSS import LoadQSS
    return LoadQSS(iface)
