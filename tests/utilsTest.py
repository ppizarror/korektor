#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/utils TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from bin.utils import *  # @UnusedWildImport

# Test
if __name__ == '__main__':
    printBarsConsole("Test funciones varias")
    print string2list("foo bar", " ")
    print getDate()
    print getHour()
    colorcmd("test in purple\n", "purple")
    print generateRandom6()
    print getTerminalSize()
    # noinspection PyTypeChecker
    print loadFile("__init__.ini")
    print sortAndUniq([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 10, 5])
    printBarsConsole("GetBetweenTags Test")
    print getBetweenTags("<player>Username<title></title></player>", "<player>", "</player>")
    print getBetweenTags("<player>Username</player><title>Altername</title>", "<player>", "</player>")
    print getBetweenTags("<player>Username</player><title>Altername</title>", "<title>", "</title>")
    printBarsConsole("Is Hidden File Test")
    print isHiddenFile(".file")
    print isHiddenFile("file")
    print isHiddenFile(1)
    printBarsConsole("Regex Test")
    print regexCompare("korektor test", "korektor test")
    print regexCompare("korektor is nice", "korektor is not nice")
    print regexCompare("*_*", "pablo.pizarro")
    print regexCompare("#.#", "pablo.pizarro")
    print regexCompare("*regex *", "regex are  korektor")
    print regexCompare("cc3001/tarea2/*_*/Parte1.java", "cc3001/tarea2/pablo_pizarro*/Parte1.java")
    print regexCompare("cc3001/tarea2/*_*/Parte1.java", "cc3001/tarea2/pablo_pizarro*/Parte1.java",
                       "abcdefghijklmnopqrstuvwxyz")
