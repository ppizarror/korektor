#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lib/fileManager TEST
Test del fileManager, módulo relacionado con el manejo y escaneo de archivos en una carpeta.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from lib.filemanager import *  # @UnusedWildImport
from bin.errors import FILEMANAGER_ERROR_RESTORE_WD, FILEMANAGER_ERROR_SCAN, FILEMANAGER_ERROR_WD
from bin.ostype import is_windows
from bin.utils import print_bars_console, equal_lists
import unittest

# Constantes de los test
DISABLE_HEAVY_TESTS = False
DISABLE_HEAVY_TESTS_MSG = "Se desactivaron los tests pesados"
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argument_parser_factory

    argparser = argument_parser_factory("FileManager Test", verbose=True, version=True,
                                        enable_skipped_test=True).parse_args()
    DISABLE_HEAVY_TESTS = argparser.enableHeavyTest
    VERBOSE = argparser.verbose


# Clase UnitTest
# noinspection PyUnnecessaryBackslash
class FileManagerTest(unittest.TestCase):
    def setUp(self):
        """
        Inicio de los test.

        :return: void
        :rtype: None
        """
        self.fm = FileManager()
        self.fm.enable_auto_extract()
        self.fm.enable_do_remove_extracted_folders()
        self.fm.disable_remove_on_extract()
        self.fm.set_default_working_directory(DIR_DATA_TEST)
        self.fm.restore_wd()
        if VERBOSE:
            self.fm.enable_verbose()
        else:
            self.fm.disable_verbose()

    def testCambioWD(self):
        """
        Testeo del cambio del working directory.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo del wd")
            print "Wd actual: ", self.fm.get_working_directory()
        b = self.fm.get_working_directory()
        if is_windows():
            self.fm.set_working_directory("C:/")
            if VERBOSE:
                print "Wd actual: ", self.fm.get_working_directory()
            assert self.fm.get_working_directory() == "C:/", FILEMANAGER_ERROR_WD
        self.fm.restore_wd()
        if VERBOSE:
            print "Wd actual: ", self.fm.get_working_directory()
        assert self.fm.get_working_directory() == b, FILEMANAGER_ERROR_RESTORE_WD
        self.fm.set_working_directory(DIR_DATA_TEST)
        if VERBOSE:
            print "Wd actual: ", self.fm.get_working_directory()
        assert self.fm.get_working_directory() == DIR_DATA_TEST, FILEMANAGER_ERROR_WD
        del b

    def testCarpetaUnica(self):
        """
        Testeo de una carpeta sencilla sin subcarpetas.

        :return: void
        :rtype: None
        """
        self.fm.restore_wd()
        if VERBOSE:
            print_bars_console("Testeo de carpetas únicas")
            print self.fm.inspect_single_file("Folder 1")
        t = ['Folder 1/Content 1.txt', \
             'Folder 1/Content 2.txt']
        assert equal_lists(t, self.fm.inspect_single_file("Folder 1")) is True, FILEMANAGER_ERROR_SCAN
        if VERBOSE:
            print self.fm.inspect_single_file("Folder 2")
        t = ['Folder 2/Content 1.txt', \
             'Folder 2/Content 2.txt', \
             'Folder 2/Subfolder/Content 1.txt', \
             'Folder 2/Subfolder/Content 2.txt']
        assert equal_lists(t, self.fm.inspect_single_file("Folder 2")) is True, FILEMANAGER_ERROR_SCAN
        del t

    def testZip(self):
        """
        Testeo de un archivo zip.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo de archivo zip")
            print self.fm.inspect_single_file("Zip Folder.zip")
        t = ['Zip Folder/Content 1 inside zip.txt', \
             'Zip Folder/Content 2 inside zip.txt']
        assert equal_lists(t, self.fm.inspect_single_file("Zip Folder.zip")) is True, FILEMANAGER_ERROR_SCAN
        del t

    def testProhibido(self):
        """
        Test de un archivo bloqueado por configuración.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo de archivos prohibidos")
            print self.fm.inspect_single_file("__MACOSX")
        assert equal_lists([], self.fm.inspect_single_file("__MACOSX")) is True, FILEMANAGER_ERROR_SCAN

    def testArchivoSingle(self):
        """
        Test de un archivo no carpeta.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo de un archivo no carpeta")
            print self.fm.inspect_single_file("ABOUT")
        assert equal_lists([], self.fm.inspect_single_file("ABOUT")), FILEMANAGER_ERROR_SCAN

    @unittest.skipIf(DISABLE_HEAVY_TESTS, DISABLE_HEAVY_TESTS_MSG)
    def testRar(self):
        """
        Testeo de un archivo rar.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo de archivo rar")
            print self.fm.inspect_single_file("Rar Folder.rar")
        t = ['Rar Folder/Content 1 inside rar.txt', 'Rar Folder/Content 2 inside rar.txt']
        assert equal_lists(t, self.fm.inspect_single_file("Rar Folder.rar")) is True, FILEMANAGER_ERROR_SCAN
        del t

    def testArchivoInexistente(self):
        """
        Testeo de un archivo inexistente.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo de un archivo inexistente")
            print self.fm.inspect_single_file("Inexistente")
        assert equal_lists([], self.fm.inspect_single_file("Inexistente")) is True, FILEMANAGER_ERROR_SCAN

    def testZipConCarpeta(self):
        """
        Testeo de un archivo zip con una carpeta dentro.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo de una carpeta con un archivo zip dentro")
            print self.fm.inspect_single_file("Folder 4")
        t = ['Folder 4/Content 1.txt', \
             'Folder 4/Content 2.txt', \
             'Folder 4/Subfolder 1/Content 1.txt', \
             'Folder 4/Subfolder 1/Content 2.txt', \
             'Folder 4/Subfolder with zip/Content 1.txt', \
             'Folder 4/Subfolder with zip/Content 2.txt', \
             'Folder 4/Subfolder with zip/Zip Folder/Content 1 inside zip.txt', \
             'Folder 4/Subfolder with zip/Zip Folder/Content 2 inside zip.txt', \
             'Folder 4/Zip Folder/Content 1 inside zip.txt', \
             'Folder 4/Zip Folder/Content 2 inside zip.txt']
        assert equal_lists(t, self.fm.inspect_single_file("Folder 4")) is True, FILEMANAGER_ERROR_SCAN
        del t

    @unittest.skipIf(DISABLE_HEAVY_TESTS, DISABLE_HEAVY_TESTS_MSG)
    def testCarpetaConRar(self):
        """
        Testeo de una carpeta con un archivo rar dentro.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo de una carpeta con un archivo rar dentro")
            print self.fm.inspect_single_file("Folder 3")
        t = ['Folder 3/Content 1.txt', \
             'Folder 3/Content 2.txt', \
             'Folder 3/Rar Folder/Content 1 inside rar.txt', \
             'Folder 3/Rar Folder/Content 2 inside rar.txt', \
             'Folder 3/Subfolder with rar/Content 1.txt', \
             'Folder 3/Subfolder with rar/Content 2.txt', \
             'Folder 3/Subfolder with rar/Rar Folder/Content 1 inside rar.txt', \
             'Folder 3/Subfolder with rar/Rar Folder/Content 2 inside rar.txt']
        assert equal_lists(t, self.fm.inspect_single_file("Folder 3")) is True, FILEMANAGER_ERROR_SCAN
        del t

    # Testeo de una carpeta grande
    @unittest.skipIf(DISABLE_HEAVY_TESTS, DISABLE_HEAVY_TESTS_MSG)
    def testFolder5(self):
        """
        Testeo de una carpeta grande.

        :return: void
        :rtype: None
        """
        if VERBOSE:
            print_bars_console("Testeo Folder 5")
            print self.fm.inspect_single_file("Folder 5")
        t = ['Folder 5/Content 1.txt', \
             'Folder 5/Content 2.txt', \
             'Folder 5/Subfolder 1/Content 3.txt', \
             'Folder 5/Subfolder 1/Content 4.txt', \
             'Folder 5/Subfolder 1/Folder 1 inside subfolder 1/Content 5.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Content 6.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Content 7.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Content C.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/README.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Subfolder 1/A1.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Subfolder 1/A2.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Subfolder with zip/Content K.txt',
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Subfolder with zip/Content X.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Subfolder with zip/Zip Folder/main.java', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Subfolder with zip/Zip Folder/Parte1.java', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Zip Folder/Content 1 inside zip.txt', \
             'Folder 5/Subfolder 1/Folder 2 inside subfolder 1/Folder 1 inside folder 2 inside subfolder 1/Zip Folder/Content 2 inside zip.txt', \
             'Folder 5/Subfolder 2 with zip/Content 8.txt', \
             'Folder 5/Subfolder 2 with zip/Content 9.txt', \
             'Folder 5/Subfolder 2 with zip/Zip Folder inside subfolder 2/Content 10', \
             'Folder 5/Subfolder 2 with zip/Zip Folder inside subfolder 2/Content 11.java', \
             'Folder 5/Zip Folder/Content A', \
             'Folder 5/Zip Folder/Content B.jar', \
             'Folder 5/Zip Folder/Rar Folder inside Zip Folder/Content 1 inside rar.txt', \
             'Folder 5/Zip Folder/Rar Folder inside Zip Folder/Content 2 inside rar.txt']
        assert equal_lists(t, self.fm.inspect_single_file("Folder 5")) is True, FILEMANAGER_ERROR_SCAN
        del t

    # noinspection SpellCheckingInspection
    @unittest.skipIf(DISABLE_HEAVY_TESTS, DISABLE_HEAVY_TESTS_MSG)
    def testCompressedFileAlreadyExists(self):
        """
        Testeo de una carpeta con archivos comprimidos que tienen el mismo nombre que una carpeta.

        :return: void
        :rtype: None
        """
        self.fm.disable_extract_if_folder_already_exists()
        if VERBOSE:
            print_bars_console("Testeo carpeta con archivos comprimidos que ya existen como carpetas")
            print self.fm.inspect_single_file("Folder 8-COMPSD")
        t = ['Folder 8-COMPSD/Subfolder 1/Content 1.txt', \
             'Folder 8-COMPSD/Subfolder 1/Content 2.txt', \
             'Folder 8-COMPSD/Subfolder 1/Subfolder inside subfolder 1/Content 1.txt', \
             'Folder 8-COMPSD/Subfolder 1/Subfolder inside subfolder 1/Content 2.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Content Y.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Content Z.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Rar Folder - target/Content target.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Rar Folder/File C.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Rar Folder/File Z.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Rar Folder/Zip Folder TARGET/Parte1.java', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Rar Folder/Zip Folder TARGET/Parte2.java', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Subfolder with rar/Content 1.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Subfolder with rar/Content 2.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Subfolder with rar/Rar Folder/Content 1 inside rar.txt', \
             'Folder 8-COMPSD/Zip Folder/Rar Folder/Subfolder with rar/Rar Folder/Content 2 inside rar.txt']
        assert equal_lists(t, self.fm.inspect_single_file("Folder 8-COMPSD")) is True, FILEMANAGER_ERROR_SCAN
        del t


# Main test
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(FileManagerTest)
    runner.run(itersuite)
