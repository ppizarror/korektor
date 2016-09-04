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
from bin.vartype import *  # @UnusedWildImport
from bin.errors import ERR_CHECKTYPE
import unittest

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argument_parser_factory

    argparser = argument_parser_factory("VarType Test", verbose=True, version=True, enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase para testear
# noinspection PyMissingOrEmptyDocstring
class TestDummyClass:
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
        assert check_variable_type(1.0, TYPE_FLOAT) is True, ERR_CHECKTYPE
        assert check_variable_type(1, TYPE_FLOAT) is False, ERR_CHECKTYPE
        assert check_variable_type(1, TYPE_INT) is True, ERR_CHECKTYPE
        assert check_variable_type("Test", TYPE_STR) is True, ERR_CHECKTYPE
        assert check_variable_type([1, 2, "a"], TYPE_LIST) is True, ERR_CHECKTYPE
        assert check_variable_type([1, 2, "a"], TYPE_INT) is False, ERR_CHECKTYPE
        r = TestDummyClass()
        assert check_variable_type(r, TYPE_OTHER, TestDummyClass) is True, ERR_CHECKTYPE
        assert check_variable_type(r, TYPE_INT) is False, ERR_CHECKTYPE
        del r
        assert check_variable_type(True, TYPE_BOOL) is True, ERR_CHECKTYPE


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(VarTypeTest)
    runner.run(itersuite)
