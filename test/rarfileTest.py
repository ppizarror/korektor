#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# bin/rarfile TEST
# Test que permite extraer y comprimir archivos rar.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.rarfile import *  # @UnusedWildImport
import unittest

# Constantes de los test
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("Rarfile Test", verbose=True, version=True).parse_args()
    VERBOSE = argparser.verbose


# Clase UnitTest
class testRarFile(unittest.TestCase):
    # Inicio de los test
    def setUp(self):
        pass

    def testA(self):
        pass


# Main test
if __name__ == '__main__':
    unittest.main()
