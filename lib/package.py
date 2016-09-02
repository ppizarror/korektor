#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PACKAGE
Los paquetes corresponden a elementos lógicos que manejan los archivos que entregan los alumnos
Contienen direcciones físicas en memoria, Archivos y Jerarquía.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de variables
if __name__ == '__main__':
    from libpath import *  # @UnusedWildImport
# noinspection PyUnresolvedReferences
from bin.errors import *  # @UnusedWildImport
from bin.utils import printHierachyList, numberOfSublists
from bin.varType import *  # @UnusedWildImport
from lib.fileManager import FileManager

# Constantes del módulo
PACKAGE_DO_NOT_EXIST = "PACKAGE_DO_NOT_EXIST"
PACKAGE_EMPTY = "PACKAGE_EMPTY"
PACKAGE_FILE_INVALID_DEPTH = -1
PACKAGE_FILE_NOT_FOUND = "PACKAGE_FILE_NOT_FOUND"
PACKAGE_NO_NAME = "PACKAGE_NO_NAME"


class Package(varTypedClass, exceptionBehaviour):
    """
    Clase paquete, maneja funciones que permiten manejar listas con archivos del estilo z:/a/b/...
    con funciones auxiliares que buscan archivos, direcciones, profunidad, etc.
    """

    def __init__(self, files, generateHierachy=False):
        """
        Constructor de la clase.

        :param files: Lista de archivos generada por un FileManager
        :type files: list
        :param generateHierachy: Generar Jerarquía automáticamente
        :type generateHierachy: bool

        :return: void
        :rtype: None
        """

        # Se instancian los super
        exceptionBehaviour.__init__(self)
        varTypedClass.__init__(self)

        # Se chequean los tipos de variable
        self._checkVariableType(files, TYPE_LIST, "Package.__init()__.files")
        self._checkVariableType(generateHierachy, TYPE_BOOL, "Package.__init()__.generateHierachy")

        # Variables de clase
        self._hierachyFiles = []
        self._packageFiles = []
        self._packageName = ""
        self._rawfiles = files

        # Variables de estado
        self._isGeneratedName = False
        self._isgeneratedHierachyFiles = False
        self._isGeneratedPackageFiles = False
        self._isValid = False
        self._validated = False
        self._validatedFiles = []

        # Se crea el paquete
        self._generatePackageName(files)
        self._generatePackageFiles(files)
        if generateHierachy:
            self.generateHierachy()

    def checkIfExist(self, f):
        """
        Comprueba si un archivo o carpeta existe en el paquete.

        :param f: Nombre del elemento a buscar
        :type f: str

        :return: Booleano indicando pertenencia o no
        :rtype: bool
        """
        return self.isFile(f) or self.isFolder(f)

    def findFileLocation(self, f):
        """
        Busca la ubicación de un archivo o carpeta en el paquete.

        :param f: Nombre del archivo o carpeta a buscar
        :type f: str

        :return: Ubicación del archivo o carpeta si es que se encuentra
        :rtype: str
        """
        fileResults = self._isFile(f)
        if fileResults[0]:
            return fileResults[1]
        else:
            folderResults = self._isFolder(f)
            if folderResults[0]:
                return folderResults[1]
        return PACKAGE_FILE_NOT_FOUND

    def getFileDepth(self, f):
        """
        Obtiene la profundidad de un archivo o carpeta en el paquete.

        :param f: Nombre del archivo o carpeta a buscar
        :type f: str

        :return: Profundidad del archivo o carpeta, si es que se encuentra
        :rtype: int
        """
        fileResults = self._isFile(f)
        if fileResults[0]:
            return fileResults[2]
        else:
            folderResults = self._isFolder(f)
            if folderResults[0]:
                return folderResults[2]
        return PACKAGE_FILE_INVALID_DEPTH

    def generateHierachy(self):
        """
        Crea una lista de jerarquía de archivos.

        :return: void
        :rtype: None
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
        Almacena el nombre de los archivos que contiene el paquete.

        :param filelist: Lista de archivos para generar el paquete
        :type filelist: list

        :return: void
        :rtype: None
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
        Se crea el nombre del paquete

        :param filelist: Lista de archivos raw
        :type filelist: list

        :return: void
        :rtype: None
        """
        if len(filelist) > 0:
            self._packageName = filelist[0].split("/")[0]
        else:
            self._packageName = PACKAGE_NO_NAME
        self._isGeneratedName = True

    def getFileList(self):
        """
        Retorna una lista con los nombres de los archivos.

        :return: Lista de archivos
        :rtype: list
        """
        if self._isGeneratedPackageFiles:
            return self._packageFiles
        else:
            return self._throwException("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    def getHierachyFiles(self):
        """
        Retorna la lista de jerarquía del paquete

        :return: Lista de jerarquía de archivos
        :rtype: list
        """
        if self._isgeneratedHierachyFiles:
            return self._hierachyFiles
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def getNumberOfElements(self):
        """
        Retorna el número de archivos que contiene el paquete.

        :return: Número de archivos
        :rtype: int
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
        Retorna el número sub-carpetas que tiene un paquete.

        :return: Número de sub-carpetas
        :rtype: int
        """

        if self._isgeneratedHierachyFiles:
            return numberOfSublists(self._hierachyFiles)
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def getPackageName(self):
        """
        Retorna el nombre del paquete.

        :return: Nombre del paquete
        :rtype: str
        """
        if self._isGeneratedName:
            return self._packageName
        else:
            return self._throwException("PACKAGE_ERROR_NO_NAME")

    def _getValidatedFiles(self):
        """
        Retorna la lista de los archivos validados.

        :return: Lista de archivos
        :rtype: list
        """
        if self._validated:
            return self._validatedFiles
        else:
            return self._throwException("PACKAGE_ERROR_NOT_VALIDATED_YET")

    def printFileList(self):
        """
        Imprime en consola la lista de archivos del paquete.

        :return: void
        :rtype: None
        """
        if self._isGeneratedPackageFiles:
            for pfle in self._packageFiles:
                print pfle
        else:
            return self._throwException("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    def _printValidatedFiles(self):
        """
        Imprime en consola la lista de archivos validados del paquete.

        :return: void
        :rtype: None
        """
        if self._validated:
            for vpfle in self._validatedFiles:
                print vpfle
        else:
            return self._throwException("PACKAGE_ERROR_NOT_VALIDATED_YET")

    def _isFile(self, fl):
        """
        Retorna un vector de valores indicando si el nombre mencionado corresponde o no a un archivo.

        :param fl: Nombre del archivo
        :type fl: str

        :return: Lista de valores indicando si existe, la ubicación y la profundidad
        :rtype: list
        """

        def _recursiveSearchFile(l, f, d, s):
            """
            Función auxiliar que busca un fichero f en una lista cualquiera l de forma recursiva.

            :param l: Lista a buscar
            :type l: list
            :param f: Archivo a buscar
            :type f: str
            :param d: Profundidad actual de búsqueda
            :type d: int

            :return: Retorna un vector de valores
            :rtype: list
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
            return [False, PACKAGE_FILE_NOT_FOUND, PACKAGE_FILE_INVALID_DEPTH]

        if self._isgeneratedHierachyFiles:
            return _recursiveSearchFile(self._hierachyFiles, fl, 0, "")
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def isFile(self, f):
        """
        Retorna un booleano indicando si el nombre mencionado corresponde o no a un archivo.

        :param f: Nombre del archivo
        :type f: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        if self._isgeneratedHierachyFiles:
            self._checkVariableType(f, TYPE_STR, "f")
            if len(f) > 0:
                return self._isFile(f)[0]
            else:
                return False
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def _isFolder(self, fl):
        """
        Retorna un vector de valores indicando si el nombre mencionado corresponde o no a una carpeta.

        :param fl: Nombre del archivo a buscar
        :type fl: str

        :return: Lista de valores indicando si existe, la ubicación y la profundidad
        :rtype: list
        """

        def _recursiveSearchFolder(l, f, d, s):
            """
            Función auxiliar que busca una carpeta f en una lista cualquiera l de forma recursiva.

            :param l: Lista a buscar
            :type l: list
            :param f: Archivo a buscar
            :type f: str
            :param d: Profundidad actual de búsqueda
            :type d: int

            :return: Retorna un vector de valores
            :rtype: list
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
                return [False, PACKAGE_FILE_NOT_FOUND, PACKAGE_FILE_INVALID_DEPTH]

        if self._isgeneratedHierachyFiles:
            return _recursiveSearchFolder(self._hierachyFiles, fl, 0, "")
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def isFolder(self, f):
        """
        Retorna un booleano indicando si el nombre mencionado corresponde o no a una carpeta.

        :param f: Nombre del archivo a buscar
        :type f: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        if self._isgeneratedHierachyFiles:
            self._checkVariableType(f, TYPE_STR, "f")
            if len(f) > 0:
                return self._isFolder(f)[0]
            else:
                return False
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def isValid(self):
        """
        Retorna true/false indicando si el paquete es válido o no.

        :return: Booleano indicando validación.
        :rtype: bool
        """
        return self._isValid

    def isValidated(self):
        """
        Retorna true/false indicando si el paquete está validado o no.

        :return: Booleano indicando si el paquete actual está validado o no
        :rtype: bool
        """
        return self._validated

    def _markAsValid(self):
        """
        Indica que la estructura del paquete es válida.

        :return: void
        :rtype: None
        """
        self._isValid = True

    def _markAsValidated(self):
        """
        Indica que el paquete ya ha sido revisado por el validador.

        :return: void
        :rtype: None
        """
        self._validated = True

    def printHierachy(self, tabsLeft=0):
        """
        Imprime la lista de archivos en forma de jerarquía.

        :param tabsLeft: Número de tabs a la izquierda de los mensajes
        :type tabsLeft: int

        :return: void
        :rtype: None
        """
        if self._isgeneratedHierachyFiles:
            if len(self._packageFiles) == 0:
                print PACKAGE_FILE_NOT_FOUND
            elif self.getNumberOfElements() == 0:
                print PACKAGE_EMPTY
            else:
                printHierachyList(self._hierachyFiles, 0, tabsLeft)
        else:
            return self._throwException("PACKAGE_ERROR_NOT_HIERACHY_CREATED")

    def printRawFiles(self):
        """
        Imprime en consola la lista de archivos sin tratar del paquete.

        :return: void
        :rtype: None
        """
        print self._rawfiles

    def _setValidatedFiles(self, vfiles):
        """
        Define los archivos válidos.

        :param vfiles: Lista con archivos válidos.
        :type vfiles: list

        :return: void
        :rtype: None
        """
        self._checkVariableType(vfiles, TYPE_LIST, "Package._setValidatedFiles.vfiles")
        self._validatedFiles = vfiles


# Clase paquete que utiliza un filemanager
class PackageFileManager(Package):
    """
    Clase paquete. Exactamente la misma que Package salvo que utiliza un filemanager externo
    y un string indicando el nombre del archivo a analizar
    """

    def __init__(self, fileManager, packageName, generateHierachy=False):
        """
        Constructor de la clase.

        :param fileManager: Filemanager a utilizar
        :type fileManager: FileManager
        :param packageName: Nombre del paquete a analizar
        :type packageName: str
        :param generateHierachy: Generar Jerarquía automáticamente
        :type generateHierachy: bool

        :return: void
        :rtype: None
        """

        # Comprobacion de tipos
        self._checkVariableType(fileManager, TYPE_OTHER, "PackageFileManager.__init()__.fileManager", FileManager)
        self._checkVariableType(packageName, TYPE_STR, "PackageFileManager.__init()__.packageName")

        # Se guarda el FileManager
        self._filemanager = fileManager

        # Se crea un paquete normal
        Package.__init__(self, fileManager.inspectSingleFile(packageName), generateHierachy)

    def _deleteLastExtractedFiles(self):
        """
        Se eliminan los archivos resultantes de la última extracción por el fileManager.

        :return: void
        :rtype: None
        """
        self._filemanager.deleteLastExtractedFiles()
