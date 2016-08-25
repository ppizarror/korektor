#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# lib/packages TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from lib.packageValidator import *  # @UnusedWildImport
from bin.utils import printBarsConsole
import os  # @Reimport @UnusedImport

if __name__ == '__main__':

    # Se crea un nuevo package
    p = PackageValidator()

    # Se imprime la estructura necesaria
    printBarsConsole("Formato de estructura válido")
    print p._getStructure()