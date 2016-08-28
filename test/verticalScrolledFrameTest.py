#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# bin/verticalScrolledFrame TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.errors import throw, ERROR_TKINTER_NOT_INSTALLED  # @UnusedImport
import unittest

# Clase UnitTest
class testColors(unittest.TestCase):

    # Inicio de los test
    def setUp(self):
        sucess = False
        try:
            from bin.verticalScrolledFrame import VerticalScrolledFrame  # @UnusedWildImport @UnusedImport
            sucess = True
        except Exception, e:  # @UnusedVariable
            sucess = False
        assert sucess == True, ERROR_TKINTER_NOT_INSTALLED

    def testImportTkinter(self):
        sucess = False
        try:
            import Tkinter  # @UnusedImport
            sucess = True
        except Exception, e:  # @UnusedVariable
            sucess = False
        assert sucess == True, ERROR_TKINTER_NOT_INSTALLED

# Test
if __name__ == '__main__':
    unittest.main()
