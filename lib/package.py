#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# PACKAGE
# Los paquetes corresponden a elementos lógicos que manejan los archivos que entregan los alumnos
# Contienen direcciones físicas en memoria, Archivos y Jerarquía
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de variables
if __name__ == '__main__':
    from libpath import *  # @UnusedWildImport
from bin.errors import *  # @UnusedWildImport
from bin.utils import printHierachyList

# Constantes del módulo
PACKAGE_NO_NAME = "PACKAGE_EMPTY"


class Package:

    def __init__(self, files=[]):
        """
        Constructor
        :return: void
        """

        # Variables de clase
        self._hierachyFiles = []
        self._packageFiles = []
        self._packageName = ""
        self._rawfiles = files

        # Variables de estado
        self._isGeneratedName = False
        self._isGeneratedPackageFiles = False

        # Se crea el paquete
        self._generatePackageName(files)
        self._generatePackageFiles(files)
        self._generateHierachy()

    def _generateHierachy(self):
        """
        Crea una lista de jerarquía de archivos
        :return: void
        """
        if self._isGeneratedPackageFiles:
            self._hierachyFiles.append(self._packageName)
            for i in self._packageFiles:
                if "/" not in i:
                    self._hierachyFiles.append(i)
                else:
                    # Se añaden las carpetas
                    j = i.split("/")
                    sublvl = self._hierachyFiles
                    for k in range(0, len(j) - 1):
                        # Se busca en cada elemento del subnivel
                        found = False
                        for m in range(0, len(sublvl)):
                            if isinstance(sublvl[m], list):  # Si es un nombre de carpeta
                                if sublvl[m][0] == j[k]:
                                    sublvl = sublvl[m]
                                    found = True
                                    break
                            else:  # Si es un string
                                if sublvl[m] == j[k]:
                                    sublvl = sublvl[m]
                                    found = True
                                    break
                        if not found:
                            sublvl.append([j[k]])
                            sublvl = sublvl[len(sublvl) - 1]
                    # Se añade el archivo
                    sublvl.append(j[len(j) - 1])
        else:
            throw(PACKAGE_ERROR_NOT_INDEXED_FILES_YET)

    def _generatePackageFiles(self, filelist):
        """
        Almacena el nombre de los archivos que contiene el paquete
        :return: void
        """
        if self._isGeneratedName:
            for i in filelist:
                a = i.split("/")
                b = ""
                c = len(a)
                for j in range(1, c):
                    b += a[j]
                    if j < c - 1:
                        b += "/"
                self._packageFiles.append(b)
            self._isGeneratedPackageFiles = True
        else:
            throw(PACKAGE_ERROR_NO_NAME)

    def _generatePackageName(self, filelist):
        """
        Crea el nombre del paquete
        :param filelist: Lista de archivos raw
        :return: String
        """
        if len(filelist) > 0:
            self._packageName = filelist[0].split("/")[0]
        else:
            self._packageName = PACKAGE_NO_NAME
        self._isGeneratedName = True

    def getFileList(self):
        """
        Retorna una lista con los nombres de los archivos
        :return: list
        """
        if self._isGeneratedPackageFiles:
            return self._packageFiles
        else:
            throw(PACKAGE_ERROR_NOT_INDEXED_FILES_YET)

    def getPackageName(self):
        """
        Retorna el nombre del paquete
        :return: String
        """
        if self._isGeneratedName:
            return self._packageName
        else:
            throw(PACKAGE_ERROR_NO_NAME)

    def printFiles(self):
        """
        Imprime en consola la lista de archivos del paquete
        :return: void
        """
        if self._isGeneratedPackageFiles:
            print self._packageFiles
        else:
            throw(PACKAGE_ERROR_NOT_INDEXED_FILES_YET)

    def printHierachy(self):
        """
        Imprime la lista de archivos en forma de jerarquía
        :return: void
        """
        if self._isGeneratedPackageFiles:
            printHierachyList(self._hierachyFiles)
        else:
            throw(PACKAGE_ERROR_NOT_INDEXED_FILES_YET)

    def printRawFiles(self):
        """
        Imprime en consola la lista de archivos sin tratar del paquete
        :return: void
        """
        print self._rawfiles
