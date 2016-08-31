#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bin/utils TEST

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
# noinspection PyUnresolvedReferences
from _testpath import *  # @UnusedWildImport
from bin.errors import *  # @UnusedWildImport
from bin.kwargsUtils import *  # @UnusedWildImport
from bin.utils import *  # @UnusedWildImport
import unittest

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("Utils Test", verbose=True, version=True, enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase UnitTest
# noinspection PyMethodMayBeStatic
class UtilsTest(unittest.TestCase):
    # Inicio de los test
    def setUp(self):
        pass

    # Comprobaciones de funciones auxiliares sencillas
    def testMain(self):
        if VERBOSE:
            printBarsConsole("Test funciones varias")
            print string2list("foo bar", " ")
            print getDate()
            print getHour()
            print generateRandom6()
            print getTerminalSize()
        assert equalLists(loadFile("__init__.ini"), []) == True, "Error al cargar archivo vacio"
        t = [1, 2, 3, 4, 5, 10]
        r = sortAndUniq([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 10, 5])
        assert equalLists(t, r) == True, "Error al ordenar lista"
        del t, r

    # Se testea la función getBetweenTags usadas para el análisis de código HTML
    def testGetBetweenTags(self):
        assert getBetweenTags("<player>Username<title></title></player>", "<player>",
                              "</player>") == "Username<title></title>", ERR_GBT
        assert getBetweenTags("<player>Username</player><title>Altername</title>", "<player>",
                              "</player>") == "Username", ERR_GBT
        assert getBetweenTags("<player>Username</player><title>Altername</title>", "<title>",
                              "</title>") == "Altername", ERR_GBT

    # Testeo de la función isHiddenFile utilizada en el fileManager
    def testIsHiddenFile(self):
        assert isHiddenFile(".file") == True, ERR_HDNFL
        assert isHiddenFile("file") == False, ERR_HDNFL
        assert isHiddenFile(1) == True, ERR_HDNFL

    # Testeo del regex utilizado en el packageValidator
    def testRegexCompare(self):
        assert regexCompare("korektor test", "korektor test") == True, ERR_REGX
        assert regexCompare("korektor is nice", "korektor is not nice") == False, ERR_REGX
        assert regexCompare("*_*", "lorem.ipsum") == False, ERR_REGX
        assert regexCompare("#.#", "lorem.ipsum") == True, ERR_REGX
        assert regexCompare("*regex *", "regex are  korektor") == True, ERR_REGX
        assert regexCompare("cc3001/tarea2/#_#/Parte1.java", "cc3001/tarea2/lorem_ipsum#/Parte1.java") == True, ERR_REGX

    # Testeo de kwargs
    def testKwargs(self):
        def _testKwargsDef(**kwargs):
            assert kwargIsTrueParam(kwargs, "trueVariable") == True, ERR_KWARGS_BAD_TRUE
            assert kwargIsTrueParam(kwargs, "trueVariable_str") == True, ERR_KWARGS_BAD_TRUE
            assert kwargIsTrueParam(kwargs, "trueVariable_int") == True, ERR_KWARGS_BAD_TRUE
            assert kwargIsFalseParam(kwargs, "falseVariable") == True, ERR_KWARGS_BAD_FALSE
            assert kwargIsFalseParam(kwargs, "falseVariable_int") == True, ERR_KWARGS_BAD_FALSE
            assert kwargGetValue(kwargs, "intVariable") == 4, ERR_KWARGS_INVALID_VALUE
            assert kwargGetValue(kwargs, "strValue") == "TEST", ERR_KWARGS_INVALID_VALUE
            assert kwargExistsKey(kwargs, "strValue") == True, ERR_KWARGS_FOUND_INVALID_KEY
            assert kwargExistsKey(kwargs, "fakeVariable") == False, ERR_KWARGS_FOUND_INVALID_KEY

        _testKwargsDef(trueVariable=True, trueVariable_str="TRUE", trueVariable_int="1", falseVariable=False,
                       falseVariable_int=0, intVariable=4, strValue="TEST")

    # Testea la conversión de números
    def testNumberConverter(self):
        assert convertToNumber("5") == 5, ERR_NUMBER_CONVERTION  # Entero
        assert convertToNumber("a") == 10, ERR_NUMBER_CONVERTION  # Hexadecimal
        assert convertToNumber(5) == 5, ERR_NUMBER_CONVERTION  # No conversión
        assert convertToNumber("1.4") == 1.4, ERR_NUMBER_CONVERTION  # Número flotante


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(UtilsTest)
    runner.run(itersuite)
