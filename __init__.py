# -*- coding: utf-8 -*-
import sys
# try:
#     sys.path.append("C:/eclipse/plugins/org.python.pydev_4.3.0.201508182223/pysrc")
# except:
#     None

def classFactory(iface):
    from LoadQSS import LoadQSS
    return LoadQSS(iface)
