#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bin/ConfigLoader TEST
Test del ConfigLoader, el cual maneja la importación y manejo de configuraciones
de la aplicación.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.configloader import *  # @UnusedWildImport
from bin.errors import ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE
import unittest

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argument_parser_factory

    argparser = argument_parser_factory("ConfigLoader Test", verbose=True, version=True,
                                        enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase UnitTest
class ConfigLoaderTest(unittest.TestCase):
    def setUp(self):
        """
        Inicio de los test.

        :return: void
        :rtype: None
        """
        self.binconfig = ConfigLoader(DIR_BIN + ".config/", "bin.ini", verbose=VERBOSE)

    # noinspection SpellCheckingInspection
    def testMain(self):
        """
        Test principal, en el cual se cargan la mayoría de las funciones del ConfigLoader.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print "Parametros:", self.binconfig.get_parameters()
            self.binconfig.print_parameters()
        self.binconfig.set_parameter("PARAM1", "VALUE1")
        self.binconfig.set_parameter("PARAM2", "VALUE2")
        self.binconfig.set_parameter("PARAM3", "VALUE3")
        self.binconfig.set_parameter("SET_DEFAULT_ENCODING", "W-850")
        if VERBOSE:
            print "Parametros:", self.binconfig.get_parameters()
            self.binconfig.print_parameters()
        assert self.binconfig.is_true("DONT_WRITE_BYTECODE") is False, "Parametro DONT_WRITE_BYTECODE debe ser Falso"
        self.binconfig.set_parameter("DONT_WRITE_BYTECODE", True)
        assert self.binconfig.is_true("DONT_WRITE_BYTECODE") is True, "Parametro DONT_WRITE_BYTECODE debe ser Verdadero"
        assert self.binconfig.get_value("PARAM1") == "VALUE1", "Valor parametro PARAM1 incorrecto"
        self.binconfig.set_parameter("PARAM1", 11)
        assert self.binconfig.get_value("PARAM1") == "11", "Valor parametro incorrecto"
        assert self.binconfig.get_value("SET_DEFAULT_ENCODING") == "W-850", "Parametro SET_DEFAULT_ENCODING erroneo"

    def testNumberify(self):
        """
        Testeo de números y autoconversión.

        :return: void
        :rtype: None
        """
        self.binconfig.set_parameter("INT_NUMBER", 4)
        self.binconfig.set_parameter("FLOAT_NUMBER", 2.3)
        self.binconfig.set_parameter("FAKE_N", "fake")
        self.binconfig.set_parameter("BINARY_NUMBER", 1001010)
        self.binconfig.set_parameter("HEX_NUMBER", "D75A")
        assert self.binconfig.get_value("INT_NUMBER", autoNumberify=True) == 4, ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE
        assert self.binconfig.get_value("FLOAT_NUMBER", autoNumberify=True) == 2.3, ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE
        assert self.binconfig.get_value("INT_NUMBER", autoNumberify=False) == "4", ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE
        assert self.binconfig.get_value("FAKE_N", autoNumberify=True) == "fake", ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE
        assert self.binconfig.get_value("HEX_NUMBER", autoNumberify=True) == 55130, ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(ConfigLoaderTest)
    runner.run(itersuite)
