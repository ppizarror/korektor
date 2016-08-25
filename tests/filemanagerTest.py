#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# lib/filemanager TEST
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from lib.fileManager import *  # @UnusedWildImport
from bin.utils import printBarsConsole

# Test
if __name__ == '__main__':

    # Creación del objeto de filemanager
    fm = FileManager()

    # Configuración del filemanager
    fm.enable_autoExtract()
    fm.enable_doRemoveExtractedFolders()
    fm.disable_removeOnExtract()

    # Testeo del cambio del wd
    printBarsConsole("Testeo del wd")
    fm.setWorkingDirectory("C:/")
    print "Wd actual", fm.getWorkingDirectory()
    print "Restaurando WD"
    fm.restoreWD()
    print "Wd actual", fm.getWorkingDirectory()
    print "Definiendo WD de testeo"
    fm.setWorkingDirectory(DIR_DATA_TEST)
    print "Wd actual", fm.getWorkingDirectory()

    # Testeo de carpetas unicas sin archivos comprimidos
    printBarsConsole("Testeo carpetas unicas")
    fm.printSingleFile("Folder 1")
    fm.printSingleFile("Folder 2")

    # Testeo de un archivo zip
    printBarsConsole("Testeo de archivo zip")
    fm.printSingleFile("Zip Folder.zip")

    # Testeo de archivos prohibidos
    printBarsConsole("Testeo de archivos prohibidos")
    fm.printSingleFile("__MACOSX")

    # Testeo de un archivo rar
    printBarsConsole("Testeo de archivo rar")
    fm.printSingleFile("Rar Folder.rar")

    # Testeo de una carpeta con un archivo zip
    printBarsConsole("Testeo de una carpeta con un archivo zip dentro")
    fm.printSingleFile("Folder 4")

    # Testeo de una carpeta con un archivo rar
    printBarsConsole("Testeo de una carpeta con un archivo rar dentro")
    fm.printSingleFile("Folder 3")

    # Testeo de un archivo
    printBarsConsole("Testeo de un solo archivo")
    fm.printSingleFile("ABOUT")

    # Testeo de una carpeta real
    fm.setWorkingDirectory(DIR_DATA_TEST_PRIVATE)
    fm.printTree()
