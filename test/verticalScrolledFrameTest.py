#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bin/verticalScrolledFrame TEST

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
# noinspection PyUnresolvedReferences
from _testpath import *  # @UnusedWildImport
from bin.errors import ERROR_TKINTER_NOT_INSTALLED  # @UnusedImport
import unittest


# Clase UnitTest
# noinspection PyUnusedLocal
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

    # Testeo de la importación de la librería python-tk (Tkinter)
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
