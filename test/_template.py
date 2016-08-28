#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# package/module TEST
# Descripción del test
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from bin.colors import *  # @UnusedWildImport
from _testpath import *  # @UnusedWildImport
import unittest

# Constantes de los test
VERBOSE = False

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
