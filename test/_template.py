#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
package/module TEST
Descripción del test.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
# noinspection PyUnresolvedReferences
from _testpath import *  # @UnusedWildImport
import unittest

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argument_parser_factory

    argparser = argument_parser_factory("Template Test", verbose=True, version=True,
                                        enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase UnitTest
class ModuleTest(unittest.TestCase):
    def setUp(self):
        """
        Inicio de los test.

        :return: void
        :rtype: None
        """
        pass

    # noinspection PyMethodMayBeStatic
    def testA(self):
        """
        Ejemplo de test.

        :return: void
        :rtype: None
        """
        pass

    @unittest.skipIf(DISABLE_HEAVY_TESTS, DISABLE_HEAVY_TESTS_MSG)
    def testSkipped(self):
        """
        Ejemplo de test saltado.

        :return: void
        :rtype: None
        """
        pass


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(ModuleTest)
    runner.run(itersuite)
