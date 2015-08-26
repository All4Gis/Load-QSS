# -*- coding: utf-8 -*-
import os
import site
import sys


try:
    sys.path.append("C:/eclipse/plugins/org.python.pydev_3.6.0.201406232321/pysrc");

except:
    None;


def classFactory(iface):
    from LoadQSS import LoadQSS

    return LoadQSS(iface)
