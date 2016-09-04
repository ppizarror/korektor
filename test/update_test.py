#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bin/update TEST
Test visual que permite manejar la versión de la aplicación.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Main test
if __name__ == '__main__':
    # Importación de librerías
    # noinspection PyUnresolvedReferences
    from _testpath import *  # @UnusedWildImport
    from bin.configloader import ConfigLoader
    from bin.utils import compare_version, get_version, print_bars_console
    from config import DIR_CONFIG
    from bin import __version__

    # Arreglo de comparaciones
    versionDict = {1: ">", 2: "<", 0: "=="}

    # Se cargan las configuraciones del update
    print_bars_console("Cargando configuraciones")
    updateConfig = ConfigLoader(DIR_CONFIG, "updates.ini")
    label = str(updateConfig.get_value("LABEL"))
    web = updateConfig.get_value("WEB")
    header = str(updateConfig.get_value("HEADER"))
    print "Label a usar:", label
    print "Web cargada:", web
    print "Headers cargados:", header

    # Se carga la version web
    print_bars_console("Obteniendo version web")
    version = get_version(label, header, web)
    print "Version local:", __version__
    print "Version web:", version
    # noinspection SpellCheckingInspection
    print "Comparacion version (1) Local, (2) Web ===> (1)", versionDict[compare_version(__version__, version)], "(2)"
