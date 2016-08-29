#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# bin/update TEST
# Test visual que permite manejar la versión de la aplicación.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Main test
if __name__ == '__main__':
    # Importación de librerías
    from _testpath import *  # @UnusedWildImport
    from bin.configLoader import configLoader
    from bin.utils import compareVersion, getVersion, printBarsConsole
    from config import DIR_CONFIG
    from bin import __version__

    # Arreglo de comparaciones
    versionDict = {1: ">", 2: "<", 0: "=="}

    # Se cargan las configuraciones del update
    printBarsConsole("Cargando configuraciones")
    updateConfig = configLoader(DIR_CONFIG, "updates.ini")
    label = updateConfig.getValue("LABEL")
    web = updateConfig.getValue("WEB")
    header = updateConfig.getValue("HEADER")
    print "Label a usar:", label
    print "Web cargada:", web
    print "Headers cargados:", header

    # Se carga la version web
    printBarsConsole("Obteniendo version web")
    version = getVersion(label, header, web)
    print "Version local:", __version__
    print "Version web:", version
    print "Comparacion version (1) Local <-> (2) Web: (1)", versionDict[compareVersion(__version__, version)], "(2)"
