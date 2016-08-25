#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# lib/packages TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from lib.packageValidator import *  # @UnusedWildImport
from bin.utils import printBarsConsole  # @UnusedImport
import os  # @Reimport @UnusedImport
import unittest

# Constantes de los test
VERBOSE = False

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