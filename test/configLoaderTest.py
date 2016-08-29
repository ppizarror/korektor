#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# bin/configLoader TEST
# Test del configLoader, el cual maneja la importación y manejo de configuraciones
# de la aplicación.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.configLoader import *  # @UnusedWildImport
import unittest

# Constantes de los test
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("ConfigLoader Test", verbose=True, version=True).parse_args()
    VERBOSE = argparser.verbose


# Clase UnitTest
class testConfigLoader(unittest.TestCase):
    # Inicio de los test
    def setUp(self):
        self.binconfig = configLoader(DIR_BIN + ".config/", "bin.ini", verbose=VERBOSE)

    def testMain(self):
        if VERBOSE:
            print "Parametros:", self.binconfig.getParameters()
            self.binconfig.printParameters()
        self.binconfig.setParameter("PARAM1", "VALUE1")
        self.binconfig.setParameter("PARAM2", "VALUE2")
        self.binconfig.setParameter("PARAM3", "VALUE3")
        self.binconfig.setParameter("SET_DEFAULT_ENCODING", "W-850")
        if VERBOSE:
            print "Parametros:", self.binconfig.getParameters()
            self.binconfig.printParameters()
        assert self.binconfig.isTrue("DONT_WRITE_BYTECODE") == False, "Parametro DONT_WRITE_BYTECODE debe ser Falso"
        self.binconfig.setParameter("DONT_WRITE_BYTECODE", True)
        assert self.binconfig.isTrue("DONT_WRITE_BYTECODE") == True, "Parametro DONT_WRITE_BYTECODE debe ser Verdadero"
        assert self.binconfig.getValue("PARAM1") == "VALUE1", "Valor parametro PARAM1 incorrecto"
        self.binconfig.setParameter("PARAM1", 11)
        assert self.binconfig.getValue("PARAM1") == "11", "Valor parametro PARAM1 incorrecto"
        assert self.binconfig.getValue("SET_DEFAULT_ENCODING") == "W-850", "Parametro SET_DEFAULT_ENCODING erroneo"


# Main test
if __name__ == '__main__':
    unittest.main()
