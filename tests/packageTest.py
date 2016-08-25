#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# lib/package TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from lib.package import *  # @UnusedWildImport
from bin.utils import printBarsConsole
from lib.fileManager import FileManager

if __name__ == '__main__':

    # Creación de un paquete
    f = FileManager()
    f.setWorkingDirectory(DIR_DATA_TEST)

    # Testeo de información
    p = Package(f.inspectSingleFile("Folder 3"), True)
    printBarsConsole("Testeo de información")
    print "Archivos en forma raw:",
    p.printRawFiles()
    print "Nombre del paquete:",
    print p.getPackageName()
    print "Archivos del paquete:"
    p.printFiles()
    print "Jerarquia del paquete:"
    p.printHierachy()
    print "Numero de subcarpetas:",
    print p.getNumberOfSubfolders()

    # Paquete grande
    printBarsConsole("Testeo folder 4")
    p = Package(f.inspectSingleFile("Folder 4"), True)
    p.printHierachy()

    # Paquete muy sencillo
    printBarsConsole("Testeo folder 1")
    p = Package(f.inspectSingleFile("Folder 1"), True)
    p.printHierachy()
    print "Numero de elementos:",
    print p.getNumberOfElements()

    # Paquete vacío
    printBarsConsole("Testeo folder sin contenido")
    p = Package(f.inspectSingleFile("Folder 0"), True)
    p.printHierachy()
    print "Numero de elementos:",
    print p.getNumberOfElements()
    print "Consulta existencia archivo:",
    print p.isFile("Content")

    # Paquete combinado
    printBarsConsole("Testeo folder 5")
    p = Package(f.inspectSingleFile("Folder 5"), True)
    p.printHierachy()
    print "Numero de elementos:",
    print p.getNumberOfElements()
    print "Consulta existencia archivo Content 1 inside zip.txt:",
    print p.isFile("Content 1 inside zip.txt")
    print "Consulta existencia archivo Content 2 inside zip.txt:",
    print p.isFile("Content 2 inside zip.txt")
    print "Consulta existencia archivo Content 3 inside zip.txt:",
    print p.isFile("Content 3 inside zip.txt")
    print "Consulta existencia archivo Content 1 inside rar.txt:",
    print p.isFile("Content 1 inside rar.txt")
    print "Consulta existencia carpeta Rar Folder:",
    print p.isFolder("Rar Folder")
    print "Consulta existencia carpeta Rar Folder inside Zip Folder:",
    print p.isFolder("Rar Folder inside Zip Folder")

    # Testeo de error en String
    p = Package([], False, True)
    print "Codigo del error:", p.printHierachy()

    # Testeo de muchas carpetas seguidas
    printBarsConsole("Testeo folder 6 - Carpetas seguidas")
    p = Package(f.inspectSingleFile("Folder 6"), True)
    p.printHierachy()
    print "Chequeo de existencia de Hello world:", p.checkIfFileExist("Hello world.txt")
