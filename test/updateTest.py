#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/update TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.configLoader import configLoader
from bin.utils import compareVersion, getVersion, printBarsConsole
from config import DIR_CONFIG
from lib import __version__

# Test
if __name__ == '__main__':

    # Arreglo de comparaciones
    versionDict = {1:">", 2:"<", 0:"=="}

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
    print "Version web:", version
    print "Comparacion version (1) Local <-> (2) Web: (1)", versionDict[compareVersion(__version__, version)], "(2)"
