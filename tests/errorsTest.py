#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/errors TEST
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
