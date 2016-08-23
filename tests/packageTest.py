#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# lib/package TEST
#
# Autor: PABLO PIZARRO @ ppizarror.com
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
    p = Package(f.inspectSingleFile("Folder 3"))
    printBarsConsole("Testeo de información")
    print "Archivos en forma raw:",
    p.printRawFiles()
    print "Nombre del paquete:",
    print p.getPackageName()
    print "Archivos del paquete:"
    p.printFiles()
    print "Jerarquia del paquete:"
    p.printHierachy()

    # Paquete grande
    printBarsConsole("Testeo folder 4")
    p = Package(f.inspectSingleFile("Folder 4"))
    p.printHierachy()

    # Paquete combinado
    printBarsConsole("Testeo folder 5")
    p = Package(f.inspectSingleFile("Folder 5"))
    p.printHierachy()

    # Paquete muy sencillo
    printBarsConsole("Testeo folder 1")
    p = Package(f.inspectSingleFile("Folder 1"))
    p.printHierachy()

    # Paquete vacío
    printBarsConsole("Testeo folder sin contenido")
    p = Package(f.inspectSingleFile("Folder 0"))
    p.printHierachy()