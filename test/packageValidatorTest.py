#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lib/packageValidator TEST
Testeo del módulo packageValidator el cual tiene por función validar que los
paquetes entregados cumplan con una determinada estructura para luego ser
compilados y ejecutados.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from _testpath import *  # @UnusedWildImport
# noinspection PyUnresolvedReferences
from bin.utils import printBarsConsole  # @UnusedImport
from data import DIR_STRUCTURE
from lib.packageValidator import *  # @UnusedWildImport
import unittest

# Constantes de los test
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("PackageValidator Test", verbose=True, version=True).parse_args()
    VERBOSE = argparser.verbose


# Clase UnitTest
class testPackageValidator(unittest.TestCase):
    # Inicio de los test
    def setUp(self):
        self.validator = PackageValidator(False)
        self.validator.setStructureDirectory(DIR_DATA_TEST_STRUCTURE_FOLDER)
        self.validator.loadStructure()

    # Testeo de la estructura como un paquete
    def testA(self):
        if VERBOSE:
            self.validator._printStructureHierachy()

        # Se cambia la estructura
        self.validator.setStructureDirectory(DIR_STRUCTURE)
        self.validator.loadStructure()

        # Se retorna a la estructura anterior
        self.validator.setStructureDirectory(DIR_DATA_TEST_STRUCTURE_FOLDER)
        self.validator.loadStructure()

    # Testeo de un paquete que es válido
    def testValidPackage(self):
        pass


# Main test
if __name__ == '__main__':
    unittest.main()
