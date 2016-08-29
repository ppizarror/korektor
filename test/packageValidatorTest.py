#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# lib/packageValidator TEST
# Testeo del módulo packageValidator el cual tiene por función validar que los
# paquetes entregados cumplan con una determinada estructura para luego ser
# compilados y ejecutados.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from lib.packageValidator import *  # @UnusedWildImport
from bin.utils import printBarsConsole  # @UnusedImport
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
        pass

    def testA(self):
        pass


# Main test
if __name__ == '__main__':
    unittest.main()
