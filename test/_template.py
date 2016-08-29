#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
package/module TEST
Descripción del test.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
# noinspection PyUnresolvedReferences
from _testpath import *  # @UnusedWildImport
import unittest

# Constantes de los test
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("Template Test", verbose=True, version=True).parse_args()
    VERBOSE = argparser.verbose


# Clase UnitTest
class testTest(unittest.TestCase):
    # Inicio de los test
    def setUp(self):
        pass

    def testA(self):
        pass


# Main test
if __name__ == '__main__':
    unittest.main()
