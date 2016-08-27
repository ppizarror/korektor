#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# lib/filemanager TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import DIR_DATA_TEST  # @UnusedWildImport
from lib.fileManager import *  # @UnusedWildImport
from bin.utils import printBarsConsole, equalLists
import unittest

# Constantes de los test
VERBOSE = False

# Clase UnitTest
class testFileManager(unittest.TestCase):

    # Inicio de los test
    def setUp(self):
        self.fm = FileManager()
        self.fm.enable_autoExtract()
        self.fm.enable_doRemoveExtractedFolders()
        self.fm.disable_removeOnExtract()
        self.fm.setDefaultWorkingDirectory(DIR_DATA_TEST)
        self.fm.restoreWD()

    def testCambioWD(self):
        if VERBOSE:
            printBarsConsole("Testeo del wd")
            print "Wd actual: ", self.fm.getWorkingDirectory()
        b = self.fm.getWorkingDirectory()
        self.fm.setWorkingDirectory("C:/")
        if VERBOSE:
            print "Wd actual: ", self.fm.getWorkingDirectory()
        assert self.fm.getWorkingDirectory() == "C:/", "WD erroneo"
        self.fm.restoreWD()
        if VERBOSE:
            print "Wd actual: ", self.fm.getWorkingDirectory()
        assert self.fm.getWorkingDirectory() == b, "Restauracion WD erronea"
        self.fm.setWorkingDirectory(DIR_DATA_TEST)
        if VERBOSE:
            print "Wd actual: ", self.fm.getWorkingDirectory()
        assert self.fm.getWorkingDirectory() == DIR_DATA_TEST, "WD erroneo"
        del b

    def testCarpetaUnica(self):
        self.fm.restoreWD()
        if VERBOSE:
            printBarsConsole("Testeo de carpetas unicas")
            print self.fm.inspectSingleFile("Folder 1")
        t = ['Folder 1/Content 1.txt', 'Folder 1/Content 2.txt']
        assert equalLists(t, self.fm.inspectSingleFile("Folder 1"))==True, "Escaneo erroneo"
        if VERBOSE:
            print self.fm.inspectSingleFile("Folder 2")
        t = ['Folder 2/Content 1.txt', 'Folder 2/Content 2.txt', 'Folder 2/Subfolder/Content 1.txt', 'Folder 2/Subfolder/Content 2.txt']
        assert equalLists(t, self.fm.inspectSingleFile("Folder 2"))==True, "Escaneo erroneo"
        del t

    def testZip(self):
        if VERBOSE:
            printBarsConsole("Testeo de archivo zip")
            print self.fm.inspectSingleFile("Zip Folder.zip")
        t = ['Zip Folder/Content 1 inside zip.txt', 'Zip Folder/Content 2 inside zip.txt']
        assert equalLists(t, self.fm.inspectSingleFile("Zip Folder.zip"))==True, "Escaneo erroneo"
        del t

    def testProhibido(self):
        if VERBOSE:
            printBarsConsole("Testeo de archivos prohibidos")
            print self.fm.inspectSingleFile("__MACOSX")
        assert equalLists([], self.fm.inspectSingleFile("__MACOSX"))==True, "Escaneo erroneo"

    def testArchivoSingle(self):
        if VERBOSE:
            printBarsConsole("Testeo de un archivo no carpeta")
            print self.fm.inspectSingleFile("ABOUT")
        assert equalLists([], self.fm.inspectSingleFile("ABOUT"))==True, "Escaneo erroneo"

    def testRar(self):
        if VERBOSE:
            printBarsConsole("Testeo de archivo rar")
            print self.fm.inspectSingleFile("Rar Folder.rar")
        t = ['Rar Folder/Content 1 inside rar.txt', 'Rar Folder/Content 2 inside rar.txt']
        assert equalLists(t, self.fm.inspectSingleFile("Rar Folder.rar"))==True, "Escaneo erroneo"
        del t

    def testArchivoInexistente(self):
        if VERBOSE:
            printBarsConsole("Testeo de un archivo inexistente")
            print self.fm.inspectSingleFile("Inexistente")
        assert equalLists([], self.fm.inspectSingleFile("Inexistente"))==True, "Escaneo erroneo"

    def testZipConCarpeta(self):
        if VERBOSE:
            printBarsConsole("Testeo de una carpeta con un archivo zip dentro")
            print self.fm.inspectSingleFile("Folder 4")
        t = ['Folder 4/Content 1.txt', 'Folder 4/Content 2.txt', 'Folder 4/Subfolder 1/Content 1.txt', \
             'Folder 4/Subfolder 1/Content 2.txt', 'Folder 4/Subfolder with zip/Content 1.txt', \
             'Folder 4/Subfolder with zip/Content 2.txt', \
             'Folder 4/Subfolder with zip/Zip Folder/Content 1 inside zip.txt', \
             'Folder 4/Subfolder with zip/Zip Folder/Content 2 inside zip.txt', \
             'Folder 4/Zip Folder/Content 1 inside zip.txt', \
             'Folder 4/Zip Folder/Content 2 inside zip.txt']
        assert equalLists(t, self.fm.inspectSingleFile("Folder 4"))==True, "Escaneo erroneo"
        del t

    def testCarpetaConRar(self):
        if VERBOSE:
            printBarsConsole("Testeo de una carpeta con un archivo rar dentro")
            print self.fm.inspectSingleFile("Folder 3")
        t = ['Folder 3/Content 1.txt', 'Folder 3/Content 2.txt', \
             'Folder 3/Rar Folder/Content 1 inside rar.txt', \
             'Folder 3/Rar Folder/Content 2 inside rar.txt', 'Folder 3/Subfolder with rar/Content 1.txt', \
             'Folder 3/Subfolder with rar/Content 2.txt', \
             'Folder 3/Subfolder with rar/Rar Folder/Content 1 inside rar.txt', \
             'Folder 3/Subfolder with rar/Rar Folder/Content 2 inside rar.txt']
        assert equalLists(t, self.fm.inspectSingleFile("Folder 3"))==True, "Escaneo erroneo"
        del t

    def testFolder5(self):
        if VERBOSE:
            printBarsConsole("Testeo Folder 5")
            print self.fm.inspectSingleFile("Folder 5")
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
        assert equalLists(t, self.fm.inspectSingleFile("Folder 5"))==True, "Escaneo erroneo"
        del t


# Main test
if __name__ == '__main__':
    unittest.main()
