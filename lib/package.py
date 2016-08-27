#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# PACKAGE
# Los paquetes corresponden a elementos lógicos que manejan los archivos que entregan los alumnos
# Contienen direcciones físicas en memoria, Archivos y Jerarquía
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de variables
if __name__ == '__main__':
    from libpath import *  # @UnusedWildImport
from bin.errors import *  # @UnusedWildImport
from bin.utils import printHierachyList
from bin.varType import *  # @UnusedWildImport
from lib.fileManager import FileManager

# Constantes del módulo
PACKAGE_DO_NOT_EXIST = "PACKAGE_DO_NOT_EXIST"
PACKAGE_EMPTY = "PACKAGE_EMPTY"
PACKAGE_FILE_NOT_FOUND = "PACKAGE_FILE_NOT_FOUND"
PACKAGE_NO_NAME = "PACKAGE_NO_NAME"


# Clase principal
class Package:
    """
    Clase paquete, necesita de una lista de archivos provista por un filemanager
    """

    def __init__(self, files=[], generateHierachy=False, exceptionAsString=False):
        """
        Constructor
        :param files: Lista de archivos generada por un FileManager
        :param generateHierachy: Generar Jerarquía automáticamente
        :param exceptionAsString: Retorna las excepciones como un String
        :return: void
        """

        # Se chequean los tipos de variable
        self._checkVariableType(files, TYPE_LIST, "files")
        self._checkVariableType(generateHierachy, TYPE_BOOL, "generateHierachy")
        self._checkVariableType(exceptionAsString, TYPE_BOOL, "exceptionAsString")

        # Variables de clase
        self._hierachyFiles = []
        self._packageFiles = []
        self._packageName = ""
        self._rawfiles = files

        # Variables de estado
        self._exceptionStrBehaviour = exceptionAsString
        self._isGeneratedName = False
        self._isgeneratedHierachyFiles = False
        self._isGeneratedPackageFiles = False

        # Se crea el paquete
        self._generatePackageName(files)
        self._generatePackageFiles(files)
        if generateHierachy:
            self.generateHierachy()

    def checkIfExist(self, f):
        """
        Comprueba si un archivo existe en el paquete
        :param f: Nombre del archivo
        :return: Boolean
        """
        return self.isFile(f) or self.isFolder(f)

    def _checkVariableType(self, var, clss, paramName, otherClass=None):
        """
        Chequea si una variable es de una determinada clase o no
        :param var: Variable a revisar
        :param clss: Clase a comprobar, String
        :param paramName: Nombre del parámetro
        :param otherClass: Clase requerida si es que la clase a comprobar es del tipo TYPE_OTHER
        :return: void
        """
        if not checkVariableType(var, clss, otherClass):
            throw(ERROR_BADPARAMETERTYPE_MSG.format(paramName, clss))

    def disable_exceptionAsString(self):
        """
        Desactiva el retornar los errores como String
        :return: void
        """
        self._exceptionStrBehaviour = True

    def enable_exceptionAsString(self):
        """
        Activa el retornar los errores como String
        :return: void
        """
        self._exceptionStrBehaviour = False

    def _isFile(self, f):
        """
        Retorna un vector de valores indicando si el nombre mencionado corresponde o no a un archivo
        :param f: String
        :return: List
        """

        def _recursiveSearchFile(l, f, d, s):
            """
            Función auxiliar que busca un fichero f en una lista cualquiera l de forma recursiva
            :param l: Lista
            :param f: Archivo
            :return: Boolean
            """
            for i in l:
                if isinstance(i, list):
                    r = len(i)
                    if r > 1:
                        k = _recursiveSearchFile(i[1:r], f, d + 1, s + "/" + i[0])
                        if k is not None and k[0]:
                            return k
                else:
                    if str(i) == f:  # Comprobación final
                        return [True, s + "/" + i, d]
            return [False, PACKAGE_FILE_NOT_FOUND, 0]

        if self._isgeneratedHierachyFiles:
            return _recursiveSearchFile(self._hierachyFiles, f, 0, "")
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def isFile(self, f):
        """
        Retorna un booleano indicando si el nombre mencionado corresponde o no a un archivo
        :param f: String
        :return: Boolean
        """
        if self._isgeneratedHierachyFiles:
            self._checkVariableType(f, TYPE_STR, "f")
            if len(f) > 0:
                return self._isFile(f)[0]
            else:
                return False
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def _isFolder(self, f):
        """
        Retorna un vector de valores indicando si el nombre mencionado corresponde o no a una carpeta
        :param f: String
        :return: List
        """

        def _recursiveSearchFolder(l, f, d, s):
            """
            Función auxiliar que busca una carpeta f en una lista cualquiera l de forma recursiva
            :param l: Lista
            :param f: Nombre de la carpeta
            :return: Boolean
            """
            j = 0
            for i in l:
                if isinstance(i, list):
                    r = len(i)
                    if r >= 1:
                        if i[0] == f:  # Comprobación final
                            return [True, s + "/" + i[0] + "/", d]
                        else:
                            k = _recursiveSearchFolder(i, f, d + 1, s + "/" + i[0])
                            if k is not None and k[0]:
                                return k
                else:
                    if i == f and j == 0:  # Comprobación final
                        return [True, s + "/" + i + "/", d]
                j += 1
            if d == 0:
                return [False, PACKAGE_FILE_NOT_FOUND, 0]

        if self._isgeneratedHierachyFiles:
            return _recursiveSearchFolder(self._hierachyFiles, f, 0, "")
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def isFolder(self, f):
        """
        Retorna un booleano indicando si el nombre mencionado corresponde o no a una carpeta
        :param f: String
        :return: Boolean
        """
        if self._isgeneratedHierachyFiles:
            self._checkVariableType(f, TYPE_STR, "f")
            if len(f) > 0:
                return self._isFolder(f)[0]
            else:
                return False
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def generateHierachy(self):
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
            self._isgeneratedHierachyFiles = True
        else:
            return self._throwException("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

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
            return self._throwException("PACKAGE_ERROR_NO_NAME")

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
            return self._throwException("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    def getNumberOfElements(self):
        """
        Retorna el número de archivos que contiene el paquete
        :return: int
        """
        if self._isGeneratedPackageFiles:
            if len(self._packageFiles) == 1 and self._packageFiles[0] == "":
                return 0
            else:
                return len(self._packageFiles)
        else:
            return self._throwException("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    def getNumberOfSubfolders(self):
        """
        Retorna el número sub-carpetas que tiene un paquete
        :return: int
        """

        def _numberLists(l):
            """
            Retorna el numero de sublistas que contiene una lista
            :param list: Lista a calcular
            :return: int
            """
            count = 0
            for i in l:
                if isinstance(i, list):
                    count = count + 1 + _numberLists(i)
            return count

        if self._isgeneratedHierachyFiles:
            return _numberLists(self._hierachyFiles)
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def getPackageName(self):
        """
        Retorna el nombre del paquete
        :return: String
        """
        if self._isGeneratedName:
            return self._packageName
        else:
            return self._throwException("PACKAGE_ERROR_NO_NAME")

    def printFileList(self):
        """
        Imprime en consola la lista de archivos del paquete
        :return: void
        """
        if self._isGeneratedPackageFiles:
            print self._packageFiles
        else:
            return self._throwException("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    def printHierachy(self):
        """
        Imprime la lista de archivos en forma de jerarquía
        :return: void
        """
        if self._isgeneratedHierachyFiles:
            if len(self._packageFiles) == 0:
                print PACKAGE_FILE_NOT_FOUND
            elif self.getNumberOfElements() == 0:
                print PACKAGE_EMPTY
            else:
                printHierachyList(self._hierachyFiles)
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def printRawFiles(self):
        """
        Imprime en consola la lista de archivos sin tratar del paquete
        :return: void
        """
        print self._rawfiles

    def _throwException(self, e):
        """
        Función que lanza una excepción según comportamiento
        :param e: Error string
        :return: String o void
        """
        if self._exceptionStrBehaviour:
            return e
        else:
            try:
                err = eval(e)
            except:
                err = PACKAGE_ERROR_NAME_NOT_FOUND
            throw(err)


# Clase paquete que utiliza un filemanager
class PackageFileManager(Package):
    """
    Clase paquete. Exactamente la misma que Package salvo que utiliza un filemanager externo
    y un string indicando el nombre del archivo a analizar
    """

    def __init__(self, fileManager, packageName, generateHierachy=False, exceptionAsString=False):
        """
        Constructor
        :param fileManager: Filemanager a utilizar
        :param packageName: Nombre del paquete a analizar
        :param generateHierachy: Generar Jerarquía automáticamente
        :param exceptionAsString: Retorna las excepciones como un String
        :return: void
        """

        # Comprobacion de tipos
        self._checkVariableType(fileManager, TYPE_OTHER, "fileManager", FileManager)
        self._checkVariableType(packageName, TYPE_STR, "packageName")

        # Se crea un paquete normal
        Package.__init__(self, fileManager.inspectSingleFile(packageName), generateHierachy, exceptionAsString)
