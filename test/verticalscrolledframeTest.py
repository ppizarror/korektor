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

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("VerticalScrolledFrame Test", verbose=True, version=True,
                                      enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase UnitTest
# noinspection PyUnusedLocal
class VerticalScrolledFrameTest(unittest.TestCase):
    def setUp(self):
        """
        Inicio de los test.

        :return: void
        :rtype: None
        """
        sucess = False
        try:
            from bin.verticalscrolledframe import VerticalScrolledFrame  # @UnusedWildImport @UnusedImport
            sucess = True
        except Exception, e:  # @UnusedVariable
            sucess = False
        assert sucess == True, ERROR_TKINTER_NOT_INSTALLED

    @staticmethod
    def testImportTkinter():
        """
        Testeo de la importación de la librería python-tk (Tkinter).

        :return: void
        :rtype: None
        """
        sucess = False
        try:
            import Tkinter  # @UnusedImport
            sucess = True
        except Exception, e:  # @UnusedVariable
            sucess = False
        assert sucess == True, ERROR_TKINTER_NOT_INSTALLED


# Test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(VerticalScrolledFrameTest)
    runner.run(itersuite)
