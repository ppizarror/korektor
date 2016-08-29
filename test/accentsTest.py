#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# bin/accents TEST
# Test del manejo de acentos de la aplicación.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.accents import *  # @UnusedWildImport
import unittest

# Constantes de los test
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("Accents Test", verbose=True, version=True).parse_args()
    VERBOSE = argparser.verbose


# Clase UnitTest
class testAccents(unittest.TestCase):
    # Inicio de los test
    def setUp(self):
        pass

    def testA(self):
        pass


# Main test
if __name__ == '__main__':
    unittest.main()
