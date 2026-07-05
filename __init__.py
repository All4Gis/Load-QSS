# -*- coding: utf-8 -*-


def classFactory(iface):
    """QGIS plugin entry point that creates and returns the LoadQSS instance."""
    from .loadQSS import LoadQSS
    return LoadQSS(iface)
