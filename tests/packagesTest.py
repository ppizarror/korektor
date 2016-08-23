#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# lib/packages TEST
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from lib.packages import *  # @UnusedWildImport

if __name__ == '__main__':

    # Se crea un nuevo package
    p = Packages()

    # Se imprime la estructura necesaria
    printBarsConsole("Formato de estructura válido")
    print p._getStructure()

    # Se cambia la carpeta de sources
    p.setSourceFolder(DIR_DATA_TEST_PRIVATE)

    # Se testea un elemento
    printBarsConsole("Testeo de paquetes")
    print p.validateStructureFile("Aguirre_Munoz__Daniel_Patricio.zip")
    print p.validateStructureFile("Leiva_Castro__Francisco_Ignacio.rar")