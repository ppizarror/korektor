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
from bin.kwargsutils import *  # @UnusedWildImport
from bin.ostype import is_windows
from bin.utils import *  # @UnusedWildImport
import unittest
import os  # @Reimport

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
# noinspection SpellCheckingInspection
REGEX_VALID_CHARS = "ABCDEFGHIJKLMÑNOPQRSTUVWXYZÁÉÍÓÚ abcdefghijklmñnopqrstuvwxyzáéíóú0123456789_.-/".decode("utf-8")
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
    def setUp(self):
        """
        Inicio de los test.

        :return: void
        :rtype: None
        """
        pass

    def testMain(self):
        """
        Comprobaciones de funciones auxiliares sencillas.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            printBarsConsole("Test funciones varias")
            print string2list("foo bar", " ")
            print getDate()
            print getHour()
            print generateRandom6()
            print getTerminalSize()
        assert equalLists(loadFile("__init__.ini"), []) == True, "Error al cargar archivo vacío"
        t = [1, 2, 3, 4, 5, 10]
        r = sortAndUniq([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 10, 5])
        assert equalLists(t, r) == True, "Error al ordenar lista"
        del t, r

    def testGetBetweenTags(self):
        """
        Se testea la función getBetweenTags usadas para el análisis de código HTML.

        :return: void
        :rtype: None
        """
        assert getBetweenTags("<player>Username<title></title></player>", "<player>",
                              "</player>") == "Username<title></title>", ERR_GBT
        assert getBetweenTags("<player>Username</player><title>Altername</title>", "<player>",
                              "</player>") == "Username", ERR_GBT
        assert getBetweenTags("<player>Username</player><title>Altername</title>", "<title>",
                              "</title>") == "Altername", ERR_GBT

    def testIsHiddenFile(self):
        """
        Testeo de la función isHiddenFile utilizada en el fileManager.

        :return: void
        :rtype: None
        """
        assert isHiddenFile(".file") == True, ERR_HDNFL
        assert isHiddenFile("file") == False, ERR_HDNFL
        assert isHiddenFile(1) == True, ERR_HDNFL

    # noinspection SpellCheckingInspection
    def testRegexCompare(self):
        """
        Testeo del regex utilizado en el packageValidator.

        :return: void
        :rtype: None
        """
        assert regexCompare("korektor test", "korektor test") == True, ERR_REGX
        assert regexCompare("korektor is nice", "korektor is not nice") == False, ERR_REGX
        assert regexCompare("korektor is nice", "korektor is nice#", REGEX_VALID_CHARS) == False, ERR_REGX
        assert regexCompare("*_*", "lorem.ipsum") == False, ERR_REGX
        assert regexCompare("#.#", "lorem.ipsum") == True, ERR_REGX
        assert regexCompare("*regex *", "regex are  korektor") == True, ERR_REGX
        assert regexCompare("cc3001/tarea2/#_#/Parte1.java", "cc3001/tarea2/lorem_ipsum/Parte1.java") == True, ERR_REGX
        assert regexCompare("#.txt", "file 1.txt") == True, ERR_REGX
        assert regexCompare(u"#.txt", u"file 1.txt") == True, ERR_REGX
        assert regexCompare("#_.txt", "file 1_.txt") == True, ERR_REGX
        assert regexCompare("#_#_#.txt", "file_is_valid.txt") == True, ERR_REGX
        assert regexCompare("#_#_#.txt", "file_is not__valid.txt", "abcdefghijklmnopqrstuvwxyz") == False, ERR_REGX
        assert regexCompare("cc3001.#.name.txt", "cc3001.name.txt", REGEX_VALID_CHARS) == False, ERR_REGX
        assert regexCompare("cc3001.#.name.txt", "cc3001.other.name.txt", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("test#", "testabc/", "abc".decode("utf-8")) == False, ERR_REGX
        assert regexCompare("test#", "test", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("#main", "mmmmmmmain", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("#mateh", "mamate", REGEX_VALID_CHARS) == False, ERR_REGX
        assert regexCompare("#mateh", "mamateh", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("cc3001.main.#_#.java", "cc3001.main.name_alt.java", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("cc3001.main.#_#.java", "cc3001.main.name.alt.java", REGEX_VALID_CHARS) == False, ERR_REGX
        assert regexCompare("cc3001.main.#_#.java", "cc3001.main.name_alt.ja", REGEX_VALID_CHARS) == False, ERR_REGX
        assert regexCompare("cc3001.main.###.java", "cc3001.main.name.alt.java", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("cc3001.main.###.java", "cc3001.main.name.alt.jav", REGEX_VALID_CHARS) == False, ERR_REGX
        assert regexCompare("#.main.###.java", "cc3001.main.name.alt.java", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("#_test.#", "cc3001_test.jar", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("#_test.#", "cc3001.test.png", REGEX_VALID_CHARS) == False, ERR_REGX
        assert regexCompare("#", "cc3001.test.png", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("#_", "_", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("", "", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("mmmm#mmmm", "mmmmmmm", REGEX_VALID_CHARS) == False, ERR_REGX
        assert regexCompare("mmmm#mmmm#", "mmmmmmmmk", REGEX_VALID_CHARS) == True, ERR_REGX
        assert regexCompare("#test#", "testedsttes", REGEX_VALID_CHARS) == True, ERR_REGX

    def testKwargs(self):
        """
        Testeo de kwargs.

        :return: void
        :rtype: None
        """

        def _testKwargsDef(**kwargs):
            """
            Testea el paso de parámetros kwargs.

            :param kwargs: Parámetros opcionales
            :type kwargs: dict

            :return: void
            :rtype: None
            """
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

    def testNumberConverter(self):
        """
        Testea la conversión de números.

        :return: void
        :rtype: None
        """
        assert convertToNumber("5") == 5, ERR_NUMBER_CONVERTION  # Entero
        assert convertToNumber("a") == 10, ERR_NUMBER_CONVERTION  # Hexadecimal
        assert convertToNumber(5) == 5, ERR_NUMBER_CONVERTION  # No conversión
        assert convertToNumber("1.4") == 1.4, ERR_NUMBER_CONVERTION  # Número flotante

    def testOS(self):
        """
        Testea el sistema operativo
        :return:
        """
        if os.name == "nt":  # Se comprueba que el sistema sea Windows si es que os.name es NT
            assert is_windows() == True, ERROR_GETTING_OS


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(UtilsTest)
    runner.run(itersuite)
