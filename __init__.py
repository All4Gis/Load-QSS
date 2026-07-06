# -*- coding: utf-8 -*-
import os


def classFactory(iface):
    """QGIS plugin entry point that creates and returns the LoadQSS instance."""
    from .loadQSS import LoadQSS

    plugin = LoadQSS(iface)

    if os.environ.get("FRAN_DEBUG") == "1":
        try:
            import debugpy
            debugpy.connect(("localhost", 5678))
            print("[QGIS] Client connected!")
        except ImportError:
            print("[QGIS] debugpy not found in QGIS profile python/")
        except Exception as e:
            print(f"[QGIS] DEBUG INIT ERROR: {e}")

    return plugin
