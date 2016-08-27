#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/utils TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.utils import *  # @UnusedWildImport
import unittest

# Constantes de los test
ERR_GBT = "Error al ejecutar getBetweenTags"
ERR_HDNFL = "Error al ejecutar isHiddenFile"
ERR_REGX = "Error al ejecutar regexCompare"
VERBOSE = False


# Clase UnitTest
class testUtils(unittest.TestCase):

    # Inicio de los test
    def setUp(self):
        pass

    def testMain(self):
        if VERBOSE:
            printBarsConsole("Test funciones varias")
            print string2list("foo bar", " ")
            print getDate()
            print getHour()
            colorcmd("test in purple\n", "purple")
            print generateRandom6()
            print getTerminalSize()
        assert equalLists(loadFile("__init__.ini"), []) == True, "Error al cargar archivo vacio"
        t = [1, 2, 3, 4, 5, 10]
        r = sortAndUniq([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 10, 5])
        assert equalLists(t, r) == True, "Error al ordenar lista"
        del t, r

    def testGetBetweenTags(self):
        assert getBetweenTags("<player>Username<title></title></player>", "<player>", "</player>") == "Username<title></title>", ERR_GBT
        assert getBetweenTags("<player>Username</player><title>Altername</title>", "<player>", "</player>") == "Username", ERR_GBT
        assert getBetweenTags("<player>Username</player><title>Altername</title>", "<title>", "</title>") == "Altername", ERR_GBT

    def testIsHiddenFile(self):
        assert isHiddenFile(".file") == True, ERR_HDNFL
        assert isHiddenFile("file") == False, ERR_HDNFL
        assert isHiddenFile(1) == True, ERR_HDNFL

    def testRegexCompare(self):
        assert regexCompare("korektor test", "korektor test") == True, ERR_REGX
        assert regexCompare("korektor is nice", "korektor is not nice") == False, ERR_REGX
        assert regexCompare("*_*", "lorem.ipsum") == False, ERR_REGX
        assert regexCompare("#.#", "lorem.ipsum") == True, ERR_REGX
        assert regexCompare("*regex *", "regex are  korektor") == True, ERR_REGX
        assert regexCompare("cc3001/tarea2/#_#/Parte1.java", "cc3001/tarea2/lorem_ipsum#/Parte1.java") == True, ERR_REGX

# Main test
if __name__ == '__main__':
    unittest.main()
