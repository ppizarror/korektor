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
# noinspection SpellCheckingInspection,PyArgumentEqualDefault
REGEX_VALID_CHARS = "ABCDEFGHIJKLMÑNOPQRSTUVWXYZÁÉÍÓÚ abcdefghijklmñnopqrstuvwxyzáéíóú0123456789_.-/".decode("utf-8")
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argument_parser_factory

    argparser = argument_parser_factory("Utils Test", verbose=True, version=True, enable_skipped_test=True).parse_args()
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
            print_bars_console("Test funciones varias")
            print string2list("foo bar", " ")
            print get_date()
            print get_hour()
            print generate_random6()
            print get_terminal_size()
        assert equal_lists(load_file("__init__.ini"), []) is True, "Error al cargar archivo vacío"
        t = [1, 2, 3, 4, 5, 10]
        r = sort_and_uniq([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 10, 5])
        assert equal_lists(t, r) is True, "Error al ordenar lista"
        del t, r

    def testGetBetweenTags(self):
        """
        Se testea la función get_between_tags usadas para el análisis de código HTML.

        :return: void
        :rtype: None
        """
        assert get_between_tags("<player>Username<title></title></player>", "<player>",
                              "</player>") == "Username<title></title>", ERR_GBT
        assert get_between_tags("<player>Username</player><title>Altername</title>", "<player>",
                              "</player>") == "Username", ERR_GBT
        assert get_between_tags("<player>Username</player><title>Altername</title>", "<title>",
                              "</title>") == "Altername", ERR_GBT

    def testIsHiddenFile(self):
        """
        Testeo de la función is_hidden_file_utils utilizada en el fileManager.

        :return: void
        :rtype: None
        """
        assert is_hidden_file_utils(".file") is True, ERR_HDNFL
        assert is_hidden_file_utils("file") is False, ERR_HDNFL
        assert is_hidden_file_utils(1) is True, ERR_HDNFL

    # noinspection SpellCheckingInspection
    def testRegexCompare(self):
        """
        Testeo del regex utilizado en el packageValidator.

        :return: void
        :rtype: None
        """
        assert regex_compare("korektor test", "korektor test") is True, ERR_REGX
        assert regex_compare("korektor is nice", "korektor is not nice") is False, ERR_REGX
        assert regex_compare("korektor is nice", "korektor is nice#", REGEX_VALID_CHARS) is False, ERR_REGX
        assert regex_compare("*_*", "lorem.ipsum") is False, ERR_REGX
        assert regex_compare("#.#", "lorem.ipsum") is True, ERR_REGX
        assert regex_compare("*regex *", "regex are  korektor") is True, ERR_REGX
        assert regex_compare("cc3001/tarea2/#_#/Parte1.java", "cc3001/tarea2/lorem_ipsum/Parte1.java") is True, ERR_REGX
        assert regex_compare("#.txt", "file 1.txt") is True, ERR_REGX
        assert regex_compare(u"#.txt", u"file 1.txt") is True, ERR_REGX
        assert regex_compare("#_.txt", "file 1_.txt") is True, ERR_REGX
        assert regex_compare("#_#_#.txt", "file_is_valid.txt") is True, ERR_REGX
        assert regex_compare("#_#_#.txt", "file_is not__valid.txt", "abcdefghijklmnopqrstuvwxyz") is False, ERR_REGX
        assert regex_compare("cc3001.#.name.txt", "cc3001.name.txt", REGEX_VALID_CHARS) is False, ERR_REGX
        assert regex_compare("cc3001.#.name.txt", "cc3001.other.name.txt", REGEX_VALID_CHARS) is True, ERR_REGX
        # noinspection PyArgumentEqualDefault
        assert regex_compare("test#", "testabc/", "abc".decode("utf-8")) is False, ERR_REGX
        assert regex_compare("test#", "test", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("#main", "mmmmmmmain", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("#mateh", "mamate", REGEX_VALID_CHARS) is False, ERR_REGX
        assert regex_compare("#mateh", "mamateh", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("cc3001.main.#_#.java", "cc3001.main.name_alt.java", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("cc3001.main.#_#.java", "cc3001.main.name.alt.java", REGEX_VALID_CHARS) is False, ERR_REGX
        assert regex_compare("cc3001.main.#_#.java", "cc3001.main.name_alt.ja", REGEX_VALID_CHARS) is False, ERR_REGX
        assert regex_compare("cc3001.main.###.java", "cc3001.main.name.alt.java", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("cc3001.main.###.java", "cc3001.main.name.alt.jav", REGEX_VALID_CHARS) is False, ERR_REGX
        assert regex_compare("#.main.###.java", "cc3001.main.name.alt.java", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("#_test.#", "cc3001_test.jar", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("#_test.#", "cc3001.test.png", REGEX_VALID_CHARS) is False, ERR_REGX
        assert regex_compare("#", "cc3001.test.png", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("#_", "_", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("", "", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("mmmm#mmmm", "mmmmmmm", REGEX_VALID_CHARS) is False, ERR_REGX
        assert regex_compare("mmmm#mmmm#", "mmmmmmmmk", REGEX_VALID_CHARS) is True, ERR_REGX
        assert regex_compare("#test#", "testedsttes", REGEX_VALID_CHARS) is True, ERR_REGX

    def testKwargs(self):
        """
        Testeo de kwargs.

        :return: void
        :rtype: None
        """

        def _test_kwargs_def(**kwargs):
            """
            Testea el paso de parámetros kwargs.

            :param kwargs: Parámetros opcionales
            :type kwargs: dict

            :return: void
            :rtype: None
            """
            assert kwarg_is_true_param(kwargs, "trueVariable") is True, ERR_KWARGS_BAD_TRUE
            assert kwarg_is_true_param(kwargs, "trueVariable_str") is True, ERR_KWARGS_BAD_TRUE
            assert kwarg_is_true_param(kwargs, "trueVariable_int") is True, ERR_KWARGS_BAD_TRUE
            assert kwarg_is_false_param(kwargs, "falseVariable") is True, ERR_KWARGS_BAD_FALSE
            assert kwarg_is_false_param(kwargs, "falseVariable_int") is True, ERR_KWARGS_BAD_FALSE
            assert kwarg_get_value(kwargs, "intVariable") == 4, ERR_KWARGS_INVALID_VALUE
            assert kwarg_get_value(kwargs, "strValue") == "TEST", ERR_KWARGS_INVALID_VALUE
            assert kwarg_exists_key(kwargs, "strValue") is True, ERR_KWARGS_FOUND_INVALID_KEY
            assert kwarg_exists_key(kwargs, "fakeVariable") is False, ERR_KWARGS_FOUND_INVALID_KEY

        _test_kwargs_def(trueVariable=True, trueVariable_str="TRUE", trueVariable_int="1", falseVariable=False,
                         falseVariable_int=0, intVariable=4, strValue="TEST")

    def testNumberConverter(self):
        """
        Testea la conversión de números.

        :return: void
        :rtype: None
        """
        assert convert_to_number("5") == 5, ERR_NUMBER_CONVERTION  # Entero
        assert convert_to_number("a") == 10, ERR_NUMBER_CONVERTION  # Hexadecimal
        assert convert_to_number(5) == 5, ERR_NUMBER_CONVERTION  # No conversión
        assert convert_to_number("1.4") == 1.4, ERR_NUMBER_CONVERTION  # Número flotante

    def testOS(self):
        """
        Testea el sistema operativo
        :return:
        """
        if os.name == "nt":  # Se comprueba que el sistema sea Windows si es que os.name es NT
            assert is_windows() is True, ERROR_GETTING_OS


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(UtilsTest)
    runner.run(itersuite)
