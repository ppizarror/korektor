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
from bin.utils import printBarsConsole
import unittest

# Constantes test
VERBOSE = False

# Se cargan argumentos desde la consola
if __name__ == '__main__':
    from bin.arguments import argumentParserFactory

    argparser = argumentParserFactory("Package Test", verbose=True, version=True).parse_args()
    VERBOSE = argparser.verbose


# Clase test
class packageTest(unittest.TestCase):
    # Inicio de los test
    def setUp(self):
        self.f = FileManager()
        self.f.setWorkingDirectory(DIR_DATA_TEST)
        if VERBOSE:
            self.f.enable_verbose()
        else:
            self.f.disable_verbose()

    # Test pesado, habilitar solo para testeo en detalle
    def _testF3(self):
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

    # Testeo de una carpeta vacía
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

    # Testeo de una carpeta con múltiples archivos zip
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

    # Testeo de una carpeta inexistente
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

    # Testeo de una carpeta grande
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

    # Testeo de varias carpetas concatenadas
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

    # Testeo de varias carpetas concatenadas sin archivos
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

    # Test sencillo
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

    # Testeo de package el cual utiliza un filemanager
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

    # Test pesado, habilitar solo para testeo en detalle
    def _testPackageWithCompressedAlreadyExistsDisableExtract(self):
        self.f.disable_extractIfFolderAlreadyExists()
        p = PackageFileManager(self.f, "Folder 8-COMPSD", True)
        if VERBOSE:
            printBarsConsole("Testeo folder 8 con archivos comprimidos de igual nombre - extraccion dehabilitada")
            p.printHierachy()
        assert p.getPackageName() == "Folder 8-COMPSD", PACKAGE_TEST_ERROR_INVALID_NAME
        assert p.getNumberOfElements() == 15, PACKAGE_TEST_ERROR_COUNT_FILES
        assert p.getNumberOfSubfolders() == 9, PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS

        # Asserts file
        assert p.isFile("Zip Folder") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFile("Parte1.java") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Parte2.java") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("PartE1.java") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 1 inside rar.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 1 inside rAr.txt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE
        assert p.isFile("Content 1.txt") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FILE

        # Asserts folder
        assert p.isFolder("Zip Folder") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Zip FOlder") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Rar Folder") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Zip Folder TARGET") == True, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER
        assert p.isFolder("Zip Folder TARGEt") == False, PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER

    # Buscar ubicación de archivos
    def testFindFile(self):
        p = Package(self.f.inspectSingleFile("Folder 6"), True)
        if VERBOSE:
            printBarsConsole("Testeo folder 6 - Busqueda de ubicacion de archivos")
            p.printHierachy()
        t = "/Subfolder 1/Subfolder 2/Subfolder 3/Subfolder 4/Hello world.txt"
        assert p.findFileLocation("Hello world.txt") == t, PACKAGE_TEST_BAD_SEARCH_LOCATION
        assert p.findFileLocation("main.java") == PACKAGE_FILE_NOT_FOUND, PACKAGE_TEST_BAD_SEARCH_LOCATION
        t = "/Subfolder 1/Subfolder 2/Subfolder 3/Subfolder 4/"
        assert p.findFileLocation("Subfolder 4") == t, PACKAGE_TEST_BAD_SEARCH_LOCATION
        t = "/Subfolder 1/Subfolder 2/Subfolder 3/"
        assert p.findFileLocation("Subfolder 3") == t, PACKAGE_TEST_BAD_SEARCH_LOCATION
        t = "/Subfolder 1/"
        assert p.findFileLocation("Subfolder 1") == t, PACKAGE_TEST_BAD_SEARCH_LOCATION
        assert p.findFileLocation("Subfolder 5") == PACKAGE_FILE_NOT_FOUND, PACKAGE_TEST_BAD_SEARCH_LOCATION
        del t

    # Buscar la profundidad de un archivo
    def testDepthFile(self):
        p = Package(self.f.inspectSingleFile("Folder 9-SIM3ZIP"), True)
        if VERBOSE:
            printBarsConsole("Testeo folder 9 similar a 3 con archivos zip - Busqueda de profundidad de archivos")
            p.printHierachy()
        assert p.getFileDepth("Zip Folder 2") == 1, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.getFileDepth("Zip Folder") == 0, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.getFileDepth("Zip Folder 3") == PACKAGE_FILE_INVALID_DEPTH, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.getFileDepth("Content A.txt") == 0, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.getFileDepth("Content C.txt") == 1, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.getFileDepth("Content E.txt") == 2, PACKAGE_TEST_BAD_SEARCH_DEPTH
        assert p.getFileDepth("Content Z.txt") == PACKAGE_FILE_INVALID_DEPTH, PACKAGE_TEST_BAD_SEARCH_DEPTH

    # Comprueba el tratamiento de errores
    def testErrorAssertionPackage(self):
        p = Package(self.f.inspectSingleFile("Folder 9-SIM3ZIP"), False, True)
        assert p.printHierachy() == "PACKAGE_ERROR_NOT_HIERACHY_CREATED", PACKAGE_TEST_BAD_EXCEPTION_TREATMENT


# Main test
if __name__ == '__main__':
    unittest.main()
