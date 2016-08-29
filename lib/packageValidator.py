#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PACKAGE VALIDATOR
Testea que los paquetes entregados por los alumnos tengan una estructura correcta
Además testea de que las estructuras de archivos tengan también una estructura correcta.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: OCTUBRE 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
if __name__ == '__main__':
    from libpath import *  # @UnusedWildImport
from bin.configLoader import configLoader  # @UnresolvedImport
from bin.utils import isFolder  # @UnusedImport
from config import DIR_CONFIG  # @UnresolvedImport
# noinspection PyUnresolvedReferences
from data import DIR_DATA, DIR_STRUCTURE_FOLDERNAME  # @UnusedImport
from lib.package import *  # @UnusedWildImport


# noinspection PyUnresolvedReferences
class PackageValidator(varTypedClass, exceptionAsStringClass):
    """
    Clase que permite validar que los paquetes tengan una estructura adecuada, para ello se instancia
    un paquete con la estructura pedida (en regex) y la función validatePackage comprueba que un
    paquete pasado por argumento.
    """

    def __init__(self, exceptionAsString=False):
        """
        Constructor de la clase.

        :param exceptionAsString: Booleano indicando si las excepciones se retornan como String
        :type exceptionAsString: bool

        :return: void
        :rtype: None
        """

        # Se instancia la clase de tratamiento de errores
        exceptionAsStringClass.__init__(self, exceptionAsString)

        # Carga de configuraciones
        coreConfig = configLoader(DIR_CONFIG, "core.ini")
        self._verbose = coreConfig.isTrue("VERBOSE")

        # Variables de estado
        self._isStructGenerated = False
        self._isValidStructureDirectories = True

        # Variables de la estructura
        self._structureDirectoryName = DIR_STRUCTURE_FOLDERNAME
        self._structureDirectoryRoot = DIR_DATA
        self._structurePackage = None

        # Instancia un filemanager para generar la estructura
        self._fm = FileManager()
        self._fm.setDefaultWorkingDirectory(self._structureDirectoryRoot)
        self._fm.restoreWD()
        self._fm.enable_autoExtract()
        self._fm.enable_doRemoveExtractedFolders()
        self._fm.disable_removeOnExtract()
        if self._verbose:
            self._fm.enable_verbose()
        else:
            self._fm.disable_verbose()

    def disable_verbose(self):
        """
        Desactiva el printing de errores y estados de sistema.

        :return: void
        :rtype: None
        """
        self._verbose = False
        self._fm.enable_verbose()

    def enable_verbose(self):
        """
        Desactiva el printing de errores y estados de sistema.

        :return: void
        :rtype: None
        """
        self._verbose = True
        self._fm.enable_verbose()

    def _getStructureFilelist(self):
        """
        Retorna la lista de archivos de la estructura del paquete.

        :return: Lista de archivos
        :rtype: list
        """
        if self._isStructGenerated:
            return self._structurePackage.getFileList()
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_NOT_CREATED")

    def _getStructurePackage(self):
        """
        Retorna la estructura válida como un paquete.

        :return: Paquete de la estructura
        :rtype: Package
        """
        if self._isStructGenerated:
            return self._structurePackage
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_NOT_CREATED")

    def loadStructure(self):
        """
        Carga la configuración de la estructura requerida para cada tarea.

        :return: void
        :rtype: None
        """
        if self._isValidStructureDirectories:
            self._structurePackage = PackageFileManager(self._fm, self._structureDirectoryName, True,
                                                        self._exceptionStrBehaviour)
            self._isStructGenerated = True
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_FOLDER_DONT_EXIST")

    def _printStructureHierachy(self):
        """
        Imprime la lista de los archivos de la estructura válida en forma de jerarquía.

        :return: void
        :rtype: None
        """
        if self._isStructGenerated:
            self._structurePackage.printHierachy()
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_NOT_CREATED")

    def setStructureDirectory(self, structureDir):
        """
        Define el directorio de la estructura.

        :param structureDir: Nuevo directorio para cargar la estructura
        :type structureDir: str

        :return: void
        :rtype: None
        """
        if isFolder(structureDir, ""):
            structureDir = structureDir.strip().replace("\\", "/").replace("//", "/")
            structureDirList = structureDir.split("/")
            ln = len(structureDirList)
            offset = -1
            if structureDirList[ln - 1] == "":
                offset = -2
            self._structureDirectoryName = structureDirList[ln + offset]
            self._structureDirectoryRoot = "/".join(structureDirList[0:ln + offset])
            self._fm.setDefaultWorkingDirectory(self._structureDirectoryRoot)
            self._fm.restoreWD()
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_FOLDER_DONT_EXIST")

    def validatePackage(self, package):
        """
        Valida un paquete, comprobando que todos los archivos del mismo cumplan con la estructura
        cargada.

        :param package: Paquete a comprobar
        :type package: Package

        :return: void
        :rtype: None
        """
        self._checkVariableType(package, TYPE_OTHER, "package", Package)


        #     def _validateStructureFile(self, filename):
        #         """
        #         Función que valida si un archivo cumple con la estructura pedida
        #         :param filename: Archivo a comprobar
        #         :return:
        #         """
        #         folderfiles = self._fm.inspectSingleFile(filename)
        #         for structfile in self._structFiles:
        #             found = False
        #             for datafile in folderfiles:
        #                 if regexCompare("#/" + structfile, datafile):
        #                     found = True
        #                     break
        #             if not found:
        #                 return False
        #         return True
