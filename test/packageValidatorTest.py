#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lib/packageValidator TEST
Testeo del módulo packageValidator el cual tiene por función validar que los
paquetes entregados cumplan con una determinada estructura para luego ser
compilados y ejecutados.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from _testpath import *  # @UnusedWildImport
# noinspection PyUnresolvedReferences
from bin.errors import *
from bin.utils import printBarsConsole  # @UnusedImport
from data import DIR_STRUCTURE
from lib.packageValidator import *  # @UnusedWildImport
import unittest

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("PackageValidator Test", verbose=True, version=True,
                                      enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase UnitTest
class PackageValidatorTest(unittest.TestCase):
    def setUp(self):
        """
        Inicio de los test.

        :return: void
        :rtype: None
        """
        self.validator = PackageValidator()
        if VERBOSE:
            self.validator.enable_verbose()
        else:
            self.validator.disable_verbose()
        self.validator.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE")
        self.validator.loadStructure()
        if VERBOSE:
            printBarsConsole("Jerarquia de archivos de la estructura valida")
            print "Nombre del paquete:", self.validator._getStructurePackage().getPackageName()
            self.validator._getStructurePackage().printHierachy()
            print self.validator._getStructureFilelist()
            print self.validator._getStructurePackage().getHierachyFiles()
            print self.validator._createBoolHierachyTree()

    def testA(self):
        """
        Testeo de la estructura como un paquete.

        :return: void
        :rtype: None
        """

        # Se cambia la estructura
        self.validator.setStructureDirectory(DIR_STRUCTURE)
        self.validator.loadStructure()

        # Se retorna a la estructura anterior
        self.validator.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE")
        self.validator.loadStructure()

    def testValidPackage(self):
        """
        Testeo del hierachy tree boollist.

        :return: void
        :rtype: None
        """
        l = [False, False, False]
        assert self.validator._checkHierachyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [False, True, True]
        assert self.validator._checkHierachyTree(l) == True, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [False, True, False]
        assert self.validator._checkHierachyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, True, True]
        assert self.validator._checkHierachyTree(l) == True, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [False, True], True]
        assert self.validator._checkHierachyTree(l) == True, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [True, False], True]
        assert self.validator._checkHierachyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [True, [True, [True, False, False, True], True], True], True]
        assert self.validator._checkHierachyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [False, [False, True], [False, True, True, True]], False]
        assert self.validator._checkHierachyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [False, [False, [False, [False, [False, [True], True], True]]]]]
        assert self.validator._checkHierachyTree(l) == True, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        del l


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(PackageValidatorTest)
    runner.run(itersuite)
