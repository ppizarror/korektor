#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bin/accents TEST
Test del manejo de acentos de la aplicación.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
# noinspection PyUnresolvedReferences
from _testpath import *  # @UnusedWildImport
# noinspection PyUnresolvedReferences
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


# Main test
if __name__ == '__main__':
    unittest.main()
