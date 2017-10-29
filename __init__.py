# -*- coding: utf-8 -*-
import sys

# try:
#     sys.path.append("D:/eclipse/plugins/org.python.pydev_5.7.0.201704111357/pysrc")
# except Exception:
#     None


def classFactory(iface):
    from .LoadQSS import LoadQSS
    return LoadQSS(iface)
