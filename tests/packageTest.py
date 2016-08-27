#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# lib/package TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import DIR_DATA_TEST  # @UnusedWildImport
from lib.package import *  # @UnusedWildImport
from bin.utils import printBarsConsole
import unittest

# Constantes test
PACKAGE_TEST_ERROR_COUNT_FILES = "Numero de archivos malo"
PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS = "Numero de subcarpetas malas"
PACKAGE_TEST_ERROR_INVALID_NAME = "El nombre de la carpeta es invalido"
PACKAGE_TEST_FOUND_INEXISTENT_FILE = "Encontro un archivo inexistente"
PACKAGE_TEST_FOUND_NOT_CORRECT_FILE = "Encontro un archivo inexistente"
PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER = "Encontro una carpeta inexistente"
VERBOSE = False


# Clase test
class packageTest(unittest.TestCase):

    # Inicio de los test
    def setUp(self):
        self.f = FileManager()
        self.f.setWorkingDirectory(DIR_DATA_TEST)

    def testF3(self):
        p = Package(self.f.inspectSingleFile("Folder 3"), True)
        if VERBOSE:
            printBarsConsole("Testeo Folder 3")
            print "Archivos en forma raw:",
            p.printRawFiles()
            print "Nombre del paquete:",
            print p.getPackageName()
            print "Archivos del paquete:"
            p.printFileList()
            print "Jerarquia del paquete:"
            p.printHierachy()
            print "Numero de subcarpetas:",
            print p.getNumberOfSubfolders()
        assert p.getPackageName() == "Folder 3", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.getNumberOfSubfolders() == 3, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.getNumberOfElements() == 8, PACKAGE_TEST_ERROR_COUNT_FILES
        del p

    def testFEmpty(self):
        p = Package(self.f.inspectSingleFile("Folder 0"), True)
        if VERBOSE:
            printBarsConsole("Testeo folder sin contenido")
            print "Lista de archivos:", p.getFileList()
            print "Nombre del paquete:", p.getPackageName()
            print "Numero de archivos:", p.getNumberOfElements()
            print "Numero de subcarpetas:", p.getNumberOfSubfolders()
            print "Jerarquía:"
            p.printHierachy()
        assert p.getNumberOfElements() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getNumberOfSubfolders() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getPackageName() == "Folder 0", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.isFile("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.checkIfExist("") == False, PACKAGE_TEST_FOUND_INEXISTENT_FILE
        del p

    def testF4(self):
        p = Package(self.f.inspectSingleFile("Folder 4"), True)
        if VERBOSE:
            printBarsConsole("Testeo folder 4")
            p.printHierachy()
        assert p.getPackageName() == "Folder 4", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.getNumberOfElements() == 10, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getNumberOfSubfolders() == 4, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.isFile("Zip Folder") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFile("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        del p

    def testInexistente(self):
        p = Package(self.f.inspectSingleFile("Fake name"))
        p.generateHierachy()
        if VERBOSE:
            printBarsConsole("Testeo de carpeta inexistente")
            print "Lista de archivos:", p.getFileList()
            print "Nombre del paquete:", p.getPackageName()
            print "Numero de elementos:", p.getNumberOfElements()
            print "Numero de subcarpetas:", p.getNumberOfSubfolders()
        assert p.getNumberOfElements() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getNumberOfSubfolders() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getPackageName() == PACKAGE_NO_NAME, PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.isFile("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.checkIfExist("") == False, PACKAGE_TEST_FOUND_INEXISTENT_FILE
        del p

    def testBig(self):
        p = Package(self.f.inspectSingleFile("Folder 5"), True)
        if VERBOSE:
            p.printHierachy()
            printBarsConsole("Testeo folder 5")

        # Testeo general
        assert p.getPackageName() == "Folder 5", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.getNumberOfElements() == 25, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getNumberOfSubfolders() == 12, PACKAGE_TEST_ERROR_COUNT_FILES

        # Testeo de carpetas
        assert p.isFolder("Subfolder 2 with zip") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Subfolder 1 with zip") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Folder 1 inside subfolder 1") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Folder 2 inside subfolder 1") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Folder 3 inside subfolder 1") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Rar Folder inside Zip Folder") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Rar Folder inside Rar Folder") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Folder 1 inside folder 2 inside subfolder 1") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Folder 1 inside folder 2 inside subfolder 2") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("main.java") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Content 9.txt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("A2.txt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Subfolder 1") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER

        # Testeo de archivos
        assert p.isFile("Subfolder 2 with zip") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Subfolder 1 with zip") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Folder 1 inside subfolder 1") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Folder 2 inside subfolder 1") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Folder 3 inside subfolder 1") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Rar Folder inside Zip Folder") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Rar Folder inside Rar Folder") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Folder 1 inside folder 2 inside subfolder 1") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Folder 1 inside folder 2 inside subfolder 2") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 14.txt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content.txt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Subfolder with zip") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Zip Folder") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 2 inside rar") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 1 inside rar") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 3 inside rar.txt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 2 inside zip.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("A2.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 5.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content K.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Parte1.java") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 11.java") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 2 inside rar.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 2 inside rar.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 1.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        del p

    def testSeguidas(self):
        p = Package(self.f.inspectSingleFile("Folder 6"), True)
        if VERBOSE:
            p.printHierachy()
            printBarsConsole("Testeo folder 6 - Carpetas seguidas")
            print "Chequeo de existencia de Hello world:", p.checkIfExist("Hello world.txt")
        assert p.getNumberOfSubfolders() == 4, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.getNumberOfElements() == 1, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.isFile("Hello world.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Subfolder 1") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFolder("Hello world.txt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Subfolder 1") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        del p

    def testSeguidasEmpty(self):
        p = Package(self.f.inspectSingleFile("Folder 6-EMPTY"), True)
        if VERBOSE:
            p.printHierachy()
            printBarsConsole("Testeo folder 6 - Vacia")
            print "Lista de archivos:", p.getFileList()
            print "Nombre del paquete:", p.getPackageName()
            print "Numero de elementos:", p.getNumberOfElements()
            print "Numero de subcarpetas:", p.getNumberOfSubfolders()
        assert p.getNumberOfElements() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getNumberOfSubfolders() == 0, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getPackageName() == "Folder 6-EMPTY", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.isFile("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.checkIfExist("") == False, PACKAGE_TEST_FOUND_INEXISTENT_FILE
        del p

    def testSimple(self):
        p = Package(self.f.inspectSingleFile("Folder 1"), True)
        if VERBOSE:
            printBarsConsole("Testeo folder 1")
            p.printHierachy()
            print "Numero de elementos:",
            print p.getNumberOfElements()
        assert p.getNumberOfElements() == 2, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getNumberOfSubfolders() == 0, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.isFile("Content 3.txt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 1.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        del p

    def testPackageWithFilemanager(self):
        p = PackageFileManager(self.f, "Folder 4", True)
        if VERBOSE:
            printBarsConsole("Testeo folder 4")
            p.printHierachy()
        assert p.getPackageName() == "Folder 4", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.getNumberOfElements() == 10, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getNumberOfSubfolders() == 4, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS
        assert p.isFile("Zip Folder") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFile("") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        del p

# Main test
if __name__ == '__main__':
    unittest.main()

