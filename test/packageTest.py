#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lib/package TEST
Test que prueba la creación de paquetes por el módulo Package, tanto como sus
respectivas subclases.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from lib.package import *  # @UnusedWildImport
from bin.errors import *  # @UnusedWildImport
from bin.utils import print_bars_console
import unittest

# Constantes test
DISABLE_HEAVY_TESTS = False
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argument_parser_factory

    argparser = argument_parser_factory("Package Test", verbose=True, version=True, enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase test
class PackageTest(unittest.TestCase):
    def setUp(self):
        """
        Inicio de los test.

        :return: void
        :rtype: None
        """
        self.f = FileManager()
        self.f.set_working_directory(DIR_DATA_TEST)
        if VERBOSE:
            self.f.enable_verbose()
        else:
            self.f.disable_verbose()

    @unittest.skipIf(DISABLE_HEAVY_TESTS, DISABLE_HEAVY_TESTS_MSG)
    def testF3(self):
        """
        Testeo de una carpeta con archivos rar.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 3"), True)
        if VERBOSE:
            print_bars_console("Testeo Folder 3")
            print "Archivos en forma raw:",
            p._print_raw_files()
            print "Nombre del paquete:",
            print p.get_package_name()
            print "Archivos del paquete:"
            p._print_file_list()
            # noinspection SpellCheckingInspection
            print "Jerarquia del paquete:"
            p._print_hierarchy()
            print "Numero de subcarpetas:",
            print p.get_number_of_subfolders()
        assert p.get_package_name() == "Folder 3", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.get_number_of_subfolders() == 3, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.get_number_of_elements() == 8, PACKAGE_TEST_ERROR_COUNT_FILES
        del p

    def testFEmpty(self):
        """
        Testeo de una carpeta vacía.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 0"), True)
        if VERBOSE:
            print_bars_console("Testeo folder sin contenido")
            print "Lista de archivos:", p.get_file_list()
            print "Nombre del paquete:", p.get_package_name()
            print "Numero de archivos:", p.get_number_of_elements()
            print "Numero de subcarpetas:", p.get_number_of_subfolders()
            print "Jerarquía:"
            p._print_hierarchy()
        assert p.get_number_of_elements() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_number_of_subfolders() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_package_name() == "Folder 0", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.is_file("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.check_if_exist("") is False, PACKAGE_TEST_FOUND_INEXISTENT_FILE
        del p

    def testF4(self):
        """
        Testeo de una carpeta con múltiples archivos zip.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 4"), True)
        if VERBOSE:
            print_bars_console("Testeo folder 4")
            p._print_hierarchy()
        assert p.get_package_name() == "Folder 4", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.get_number_of_elements() == 10, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_number_of_subfolders() == 4, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.is_file("Zip Folder") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_file("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        del p

    def testInexistente(self):
        """
        Testeo de una carpeta inexistente.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Fake name"))
        p.generate_hierarchy()
        if VERBOSE:
            print_bars_console("Testeo de carpeta inexistente")
            print "Lista de archivos:", p.get_file_list()
            print "Nombre del paquete:", p.get_package_name()
            print "Numero de elementos:", p.get_number_of_elements()
            print "Numero de subcarpetas:", p.get_number_of_subfolders()
        assert p.get_number_of_elements() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_number_of_subfolders() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_package_name() == PACKAGE_NO_NAME, PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.is_file("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.check_if_exist("") is False, PACKAGE_TEST_FOUND_INEXISTENT_FILE
        del p

    @unittest.skipIf(DISABLE_HEAVY_TESTS, DISABLE_HEAVY_TESTS_MSG)
    def testBig(self):
        """
        Testeo de un paquete grande.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 5"), True)
        if VERBOSE:
            p._print_hierarchy()
            print_bars_console("Testeo folder 5")

        # Testeo general
        assert p.get_package_name() == "Folder 5", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.get_number_of_elements() == 25, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_number_of_subfolders() == 12, PACKAGE_TEST_ERROR_COUNT_FILES

        # Testeo de carpetas
        assert p.is_folder("Subfolder 2 with zip") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Subfolder 1 with zip") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Folder 1 inside subfolder 1") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Folder 2 inside subfolder 1") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Folder 3 inside subfolder 1") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Rar Folder inside Zip Folder") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Rar Folder inside Rar Folder") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Folder 1 inside folder 2 inside subfolder 1") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Folder 1 inside folder 2 inside subfolder 2") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("main.java") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Content 9.txt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("A2.txt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Subfolder 1") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER

        # Testeo de archivos
        assert p.is_file("Subfolder 2 with zip") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Subfolder 1 with zip") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Folder 1 inside subfolder 1") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Folder 2 inside subfolder 1") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Folder 3 inside subfolder 1") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Rar Folder inside Zip Folder") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Rar Folder inside Rar Folder") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Folder 1 inside folder 2 inside subfolder 1") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Folder 1 inside folder 2 inside subfolder 2") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 14.txt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content.txt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Subfolder with zip") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Zip Folder") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 2 inside rar") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 1 inside rar") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 3 inside rar.txt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 2 inside zip.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("A2.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 5.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content K.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Parte1.java") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 11.java") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 2 inside rar.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 2 inside rar.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 1.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        del p

    def testSeguidas(self):
        """
        Testeo de varias carpetas concatenados.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 6"), True)
        if VERBOSE:
            p._print_hierarchy()
            print_bars_console("Testeo folder 6 - Carpetas seguidas")
            print "Chequeo de existencia de Hello world:", p.check_if_exist("Hello world.txt")
        assert p.get_number_of_subfolders() == 4, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.get_number_of_elements() == 1, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.is_file("Hello world.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Subfolder 1") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_folder("Hello world.txt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Subfolder 1") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        del p

    def testSeguidasEmpty(self):
        """
        Testeo de varias carpetas concatenadas sin archivos.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 6-EMPTY"), True)
        if VERBOSE:
            p._print_hierarchy()
            print_bars_console("Testeo folder 6 - Vacía")
            print "Lista de archivos:", p.get_file_list()
            print "Nombre del paquete:", p.get_package_name()
            print "Numero de elementos:", p.get_number_of_elements()
            print "Numero de subcarpetas:", p.get_number_of_subfolders()
        assert p.get_number_of_elements() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_number_of_subfolders() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_package_name() == "Folder 6-EMPTY", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.is_file("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.check_if_exist("") is False, PACKAGE_TEST_FOUND_INEXISTENT_FILE
        del p

    def testSimple(self):
        """
        Test sencillo.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 1"), True)
        if VERBOSE:
            print_bars_console("Testeo folder 1")
            p._print_hierarchy()
            print "Numero de elementos:",
            print p.get_number_of_elements()
        assert p.get_number_of_elements() == 2, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_number_of_subfolders() == 0, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.is_file("Content 3.txt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 1.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        del p

    def testPackageWithFilemanager(self):
        """
        Testeo del package el cual utiliza un filemanager.

        :return: void
        :rtype: None
        """
        p = PackageFileManager(self.f, "Folder 4", True)
        if VERBOSE:
            print_bars_console("Testeo folder 4")
            p._print_hierarchy()
        assert p.get_package_name() == "Folder 4", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.get_number_of_elements() == 10, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_number_of_subfolders() == 4, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.is_file("Zip Folder") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_file("") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        del p

    # noinspection SpellCheckingInspection
    @unittest.skipIf(DISABLE_HEAVY_TESTS, DISABLE_HEAVY_TESTS_MSG)
    def testPackageWithCompressedAlreadyExistsDisableExtract(self):
        """
        Testeo de una carpeta con archivos comprimidos de igual nombre que las carpetas internas.

        :return: void
        :rtype: None
        """
        self.f.disable_extract_if_folder_already_exists()
        p = PackageFileManager(self.f, "Folder 8-COMPSD", True)
        if VERBOSE:
            print_bars_console("Testeo folder 8 con archivos comprimidos de igual nombre - extracción deshabilitada")
            p._print_hierarchy()
        assert p.get_package_name() == "Folder 8-COMPSD", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.get_number_of_elements() == 15, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.get_number_of_subfolders() == 9, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS

        # Asserts file
        assert p.is_file("Zip Folder") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_file("Parte1.java") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Parte2.java") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("PartE1.java") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 1 inside rar.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 1 inside rAr.txt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.is_file("Content 1.txt") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE

        # Asserts folder
        assert p.is_folder("Zip Folder") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Zip FOlder") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Rar Folder") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Zip Folder TARGET") is True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.is_folder("Zip Folder TARGEt") is False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER

    def testFindFile(self):
        """
        Testea la búsqueda de archivos.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 6"), True)
        if VERBOSE:
            print_bars_console("Testeo folder 6 - Busqueda de ubicación de archivos")
            p._print_hierarchy()
        t = "/Subfolder 1/Subfolder 2/Subfolder 3/Subfolder 4/Hello world.txt"
        assert p.find_file_location("Hello world.txt") == t, PACKAGE_TEST_BAD_SEARCH_LOCATION
        assert p.find_file_location("main.java") == PACKAGE_FILE_NOT_FOUND, PACKAGE_TEST_BAD_SEARCH_LOCATION
        t = "/Subfolder 1/Subfolder 2/Subfolder 3/Subfolder 4/"
        assert p.find_file_location("Subfolder 4") == t, PACKAGE_TEST_BAD_SEARCH_LOCATION
        t = "/Subfolder 1/Subfolder 2/Subfolder 3/"
        assert p.find_file_location("Subfolder 3") == t, PACKAGE_TEST_BAD_SEARCH_LOCATION
        t = "/Subfolder 1/"
        assert p.find_file_location("Subfolder 1") == t, PACKAGE_TEST_BAD_SEARCH_LOCATION
        assert p.find_file_location("Subfolder 5") == PACKAGE_FILE_NOT_FOUND, PACKAGE_TEST_BAD_SEARCH_LOCATION
        del t

    def testDepthFile(self):
        """
        Testea la búsqueda de profunidad de un archivo.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 9-SIM3ZIP"), True)
        if VERBOSE:
            print_bars_console("Testeo folder 9 similar a 3 con archivos zip - Busqueda de profundidad de archivos")
            p._print_hierarchy()
        assert p.get_file_depth("Zip Folder 2") == 1, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.get_file_depth("Zip Folder") == 0, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.get_file_depth("Zip Folder 3") == PACKAGE_FILE_INVALID_DEPTH, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.get_file_depth("Content A.txt") == 0, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.get_file_depth("Content C.txt") == 1, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.get_file_depth("Content E.txt") == 2, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.get_file_depth("Content Z.txt") == PACKAGE_FILE_INVALID_DEPTH, PACKAGE_TEST_BAD_SEARCH_DEPTH

    def testErrorAssertionPackage(self):
        """
        Comprueba el tratamiento de errores.

        :return: void
        :rtype: None
        """
        p = Package(self.f.inspect_single_file("Folder 9-SIM3ZIP"))
        p.enable_exception_as_string()
        p.enable_exception_code()
        assert p._print_hierarchy() == "PACKAGE_ERROR_NOT_HIERARCHY_CREATED", PACKAGE_TEST_BAD_EXCEPTION_TREATMENT


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(PackageTest)
    runner.run(itersuite)
