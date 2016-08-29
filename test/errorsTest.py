#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# bin/errors TEST
# Test del manejo de errores de la aplicación.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.errors import *  # @UnusedWildImport
import unittest

# Constantes de los test
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("Errors Test", verbose=True, version=True).parse_args()
    VERBOSE = argparser.verbose


# Clase UnitTest
class testErrors(unittest.TestCase):
    # Inicio de los test
    def setUp(self):
        pass

    def testA(self):
        if VERBOSE:
            st_error("Este es un error grave", False)
            st_info("Esta es una información")
            st_warning("Esta es una advertencia")


# Main test
if __name__ == '__main__':
    unittest.main()
