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
    from bin.configloader import configLoader
    from bin.utils import compareVersion, getVersion, printBarsConsole
    from config import DIR_CONFIG
    from bin import __version__

    # Arreglo de comparaciones
    versionDict = {1: ">", 2: "<", 0: "=="}

    # Se cargan las configuraciones del update
    printBarsConsole("Cargando configuraciones")
    updateConfig = configLoader(DIR_CONFIG, "updates.ini")
    label = str(updateConfig.getValue("LABEL"))
    web = updateConfig.getValue("WEB")
    header = str(updateConfig.getValue("HEADER"))
    print "Label a usar:", label
    print "Web cargada:", web
    print "Headers cargados:", header

    # Se carga la version web
    printBarsConsole("Obteniendo version web")
    version = getVersion(label, header, web)
    print "Version local:", __version__
    print "Version web:", version
    # noinspection SpellCheckingInspection
    print "Comparacion version (1) Local, (2) Web ===> (1)", versionDict[compareVersion(__version__, version)], "(2)"
