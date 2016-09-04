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
from bin.errors import *  # @UnusedWildImport
from bin.utils import printBarsConsole
from lib.packagevalidator import *  # @UnusedWildImport
import unittest

# Constantes de los test
DISABLE_HEAVY_TESTS = True
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
_DISABLE_HEAVY_TEST_TEMPORALY = "Los test se desactivaron temporalmente"
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
    # noinspection SpellCheckingInspection
    @staticmethod
    def testValidPackage():
        """
        Testeo del hierarchy tree boollist.

        :return: void
        :rtype: None
        """
        # Se crea un validador
        validator = PackageValidator()
        validator.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE")
        validator.loadStructure()

        l = [False, False, False]
        assert validator._checkHierarchyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [False, True, True]
        assert validator._checkHierarchyTree(l) == True, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [False, True, False]
        assert validator._checkHierarchyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, True, True]
        assert validator._checkHierarchyTree(l) == True, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [False, True], True]
        assert validator._checkHierarchyTree(l) == True, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [True, False], True]
        assert validator._checkHierarchyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [True, [True, [True, False, False, True], True], True], True]
        assert validator._checkHierarchyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [False, [False, True], [False, True, True, True]], False]
        assert validator._checkHierarchyTree(l) == False, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        l = [True, [False, [False, [False, [False, [False, [True], True], True]]]]]
        assert validator._checkHierarchyTree(l) == True, VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE
        del l

    @staticmethod
    def testValidationEmpty():
        """
        Test de validación simple.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE EMPTY")
        v.loadStructure()

        # Carpeta vacía y structure vacía
        p = PackageFileManager(f, "Folder 0", True)
        p.enable_exceptionThrow()
        # self.validator.validatePackage(p)
        v.validatePackage(p)
        assert p.isValidated() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH
        assert p.isValid() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

        # Paquete no existente y structure por defecto
        p = PackageFileManager(f, "Folder fake", True)
        p.enable_exceptionThrow()
        v.validatePackage(p)
        assert p.isValidated() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH
        assert p.isValid() == False, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

    @staticmethod
    def testValidationSimple():
        """
        Test de validación simple.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptionAsString()

        # Carpeta con 1 sólo archivo
        p = PackageFileManager(f, "Folder 10", True)
        p.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE SINGLE FILE")

        # Prints estructuras a verificar
        if VERBOSE:
            printBarsConsole("Testeo Folder 10 con STRUCTURE SINGLE FILE")
            p._printHierarchy()
            print ""
            v._printStructureHierachy()

        # Se valida el paquete
        v.validatePackage(p, VERBOSE)

        # Prints jerarquías de archivos
        if VERBOSE:
            print ""
            printBarsConsole("Jerarquías de archivos válidos / no validos", 1)
            p._printValidHierachyList(1)
            print ""
            p._printNotValidHierachyList(1)
            print ""

        assert p.isValid() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

    # noinspection PyMethodMayBeStatic
    def testValidationNoSubfolder(self):
        """
        Test de validación sin subcarpetas.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptionAsString()
        p = PackageFileManager(f, "Folder 11", True)
        p.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE SIMPLE")

        # Prints estructuras a verificar
        if VERBOSE:
            printBarsConsole("Testeo Folder 11 con STRUCTURE SIMPLE")
            p._printHierarchy()
            print ""
            v._printStructureHierachy()

        # Se valida el paquete
        v.validatePackage(p, VERBOSE)

        # Prints jerarquías de archivos
        if VERBOSE:
            print ""
            printBarsConsole("Jerarquías de archivos válidos / no validos", 1)
            p._printValidHierachyList(1)
            print ""
            p._printNotValidHierachyList(1)
            print ""

        assert p.isValid() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

    # noinspection PyMethodMayBeStatic
    def testValidationSubfoldered(self):
        """
        Test de validación con subcarpetas.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptions()
        p = PackageFileManager(f, "Package-validation 1", True)
        p.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE")

        # Prints estructuras a verificar
        if VERBOSE:
            printBarsConsole("Testeo Package-validation 1 con STRUCTURE")
            p._printHierarchy()
            print ""
            v._printStructureHierachy()

        # Se valida el paquete
        v.validatePackage(p, VERBOSE)

        # Prints jerarquías de archivos
        if VERBOSE:
            print ""
            printBarsConsole("Jerarquías de archivos válidos / no validos", 1)
            p._printValidHierachyList(1)
            print ""
            p._printNotValidHierachyList(1)
            print ""

        assert p.isValid() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

    # noinspection PyMethodMayBeStatic
    def testValidationSubfoldered2(self):
        """
        Test de validación con subcarpetas en donde la estructura se repite en una carpeta interna.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptions()
        p = PackageFileManager(f, "Package-validation 2", True)
        p.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE")

        # Prints estructuras a verificar
        if VERBOSE:
            printBarsConsole("Testeo de Package-validation 2 con STRUCTURE")
            p._printHierarchy()
            print ""
            v._printStructureHierachy()

        # Se valida el paquete
        v.validatePackage(p, VERBOSE)

        # Prints jerarquías de archivos
        if VERBOSE:
            print ""
            printBarsConsole("Jerarquías de archivos válidos / no validos", 1)
            p._printValidHierachyList(1)
            print ""
            p._printNotValidHierachyList(1)
            print ""

        assert p.isValid() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

    # noinspection PyMethodMayBeStatic
    def testValidationSubfoldered3(self):
        """
        Test de validación con subcarpetas en donde la estructura se repite en una carpeta interna pero falla por regex.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptions()
        p = PackageFileManager(f, "Package-validation 3", True)
        p.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE")

        # Prints estructuras a verificar
        if VERBOSE:
            printBarsConsole("Testeo Package-validation 3 con STRUCTURE")
            p._printHierarchy()
            print ""
            v._printStructureHierachy()

        # Se valida el paquete
        v.validatePackage(p, VERBOSE)

        # Falla por regex en name_surname
        assert p.isValid() == False, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

    # noinspection PyMethodMayBeStatic
    def testValidationSubfoldered4(self):
        """
        Test de validación con subcarpetas en donde la estructura se repite en una carpeta interna.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptions()
        p = PackageFileManager(f, "Package-validation 4", True)
        p.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE 2")

        # Prints estructuras a verificar
        if VERBOSE:
            printBarsConsole("Testeo Package-validation 4 con STRUCTURE 2")
            p._printHierarchy()
            print ""
            v._printStructureHierachy()

        # Se valida el paquete
        v.validatePackage(p, VERBOSE)

        # Prints jerarquías de archivos
        if VERBOSE:
            print ""
            printBarsConsole("Jerarquías de archivos válidos / no validos", 1)
            p._printValidHierachyList(1)
            print ""
            p._printNotValidHierachyList(1)
            print ""

        assert p.isValid() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

    # noinspection PyMethodMayBeStatic
    def testValidationSubfoldered5(self):
        """
        Test de validación con subcarpetas en donde la estructura se repite en una carpeta interna.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptions()
        p = PackageFileManager(f, "Package-validation 5", True)
        p.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE 2")

        # Prints estructuras a verificar
        if VERBOSE:
            printBarsConsole("Testeo Package-validation 5 con STRUCTURE 2")
            p._printHierarchy()
            print ""
            v._printStructureHierachy()

        # Se valida el paquete
        v.validatePackage(p, VERBOSE)
        p._printValidatedFileList()

        # Prints jerarquías de archivos
        if VERBOSE:
            print ""
            printBarsConsole("Jerarquías de archivos válidos / no validos", 1)
            p._printValidHierachyList(1)
            print ""
            p._printNotValidHierachyList(1)
            print ""

        assert p.isValid() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH

    @staticmethod
    def testDoubleSubfolders():
        """
        Test de validación de dos carpetas.

        :return: void
        :rtype: None
        """
        f = FileManager(DIR_DATA_TEST)
        f.disable_removeOnExtract()
        f.enable_structureCharacters()
        v = PackageValidator()
        v.enable_exceptions()
        p = PackageFileManager(f, "Package-validation 6", True)
        p.enable_exceptionThrow()
        v.setStructureDirectory(DIR_DATA_TEST + "STRUCTURE 3")

        # Prints estructuras a verificar
        if VERBOSE:
            printBarsConsole("Testeo Package-validation 6 con STRUCTURE 3")
            p._printHierarchy()
            print ""
            v._printStructureHierachy()

        # Se valida el paquete
        v.validatePackage(p, VERBOSE)

        # Prints jerarquías de archivos
        if VERBOSE:
            print ""
            printBarsConsole("Jerarquías de archivos válidos / no validos", 1)
            p._printValidHierachyList(1)
            print ""
            p._printNotValidHierachyList(1)
            print ""

        assert p.isValid() == True, VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(PackageValidatorTest)
    runner.run(itersuite)
