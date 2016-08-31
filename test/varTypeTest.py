#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bin/varType TEST
Testeo de modulo que comprueba tipos de variable

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
# noinspection PyUnresolvedReferences
from _testpath import *  # @UnusedWildImport
from bin.varType import *  # @UnusedWildImport
from bin.errors import ERR_CHECKTYPE
import unittest

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("VarType Test", verbose=True, version=True, enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase para testear
# noinspection PyMissingOrEmptyDocstring
class testDummyClass:
    def __init__(self):
        pass


# Clase UnitTest
class VarTypeTest(unittest.TestCase):
    def setUp(self):
        """
        Inicio de los test.

        :return: void
        :rtype: None
        """
        pass

    @staticmethod
    def testCheckVariableType():
        """
        Comprobación de los tipos de variables.

        :return: void
        :rtype: None
        """
        assert checkVariableType(1.0, TYPE_FLOAT) == True, ERR_CHECKTYPE
        assert checkVariableType(1, TYPE_FLOAT) == False, ERR_CHECKTYPE
        assert checkVariableType(1, TYPE_INT) == True, ERR_CHECKTYPE
        assert checkVariableType("Test", TYPE_STR) == True, ERR_CHECKTYPE
        assert checkVariableType([1, 2, "a"], TYPE_LIST) == True, ERR_CHECKTYPE
        assert checkVariableType([1, 2, "a"], TYPE_INT) == False, ERR_CHECKTYPE
        r = testDummyClass()
        assert checkVariableType(r, TYPE_OTHER, testDummyClass) == True, ERR_CHECKTYPE
        assert checkVariableType(r, TYPE_INT) == False, ERR_CHECKTYPE
        del r
        assert checkVariableType(True, TYPE_BOOL) == True, ERR_CHECKTYPE


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(VarTypeTest)
    runner.run(itersuite)
