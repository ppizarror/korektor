#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# PACKAGE VALIDATOR
# Testea que los paquetes entregados por los alumnos tengan una estructura correcta
# Además testea de que las estructuras de archivos tengan también una estructura correcta
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: OCTUBRE 2015 - 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from libpath import *  # @UnusedWildImport
from bin.configLoader import configLoader  # @UnresolvedImport
import bin.errors as err  # @UnresolvedImport @UnusedImport
from lib.fileManager import FileManager  # @UnusedImport @UnresolvedImport
from config import DIR_CONFIG  # @UnresolvedImport
from data import DIR_UPLOADS, DIR_STRUCTURE, DIR_DATA  # @UnusedImport
from bin.utils import regexCompare, appendListToList, isFolder
import os  # @Reimport @NoMove

# Constantes
PACKAGE_TESTER_ERROR_NO_FOUND = "El archivo consultado no existe"
PACKAGE_VALIDATE_FAIL = "FOLDER-PACKAGE-FAIL"
PACKAGE_VALIDATE_OK = "FOLDER-PACKAGE-OK"
ZIP_VALIDATE_FAIL = "ZIP-PACKAGE-FAIL"
ZIP_VALIDATE_OK = "ZIP-PACKAGE-OK"


# noinspection PyUnresolvedReferences
class PackageValidator:
    """
    package: Paquetes de usuario el cual provee funciones para acceder a los contenidos
    de cada paquete, como tambien la estructura básica pedida
    """

    def __init__(self):
        """
        Constructor
        :return: void
        """
        # Carga de configuraciones
        config = configLoader(DIR_CONFIG, "packages.ini")
        folderConfig = configLoader(DIR_CONFIG, "folder.ini")
        coreConfig = configLoader(DIR_CONFIG, "core.ini")
        self.ignoredFiles = folderConfig.getValueListed("IGNORE")
        self.packageStructedFiles = []  # Lista con archivos requeridos para cada package
        self.validChars = config.getValue("VALID_CHARACTERS")  # Caracteres válidos de los archivos del paquete
        self.validRegexChars = config.getValue("VALID_REGEX_CHARACTERS")  # Caracteres válidos para los regex
        self.verbose = coreConfig.isTrue("VERBOSE")

        # Carpeta de los paquetes a analizar
        self._defaultsourceroot = DIR_UPLOADS
        self._sourceroot = DIR_UPLOADS
        self._structureroot = DIR_STRUCTURE

        # Instancia un filemanager
        self._fm = FileManager()
        self._fm.setDefaultWorkingDirectory(self._defaultsourceroot)
        self._fm.restoreWD()

        # Genera la estructura
        self._structFiles = []
        self._loadStructure()

    def disable_verbose(self):
        """
        Desactiva el printing de errores y estados de sistema
        :return: void
        """
        self._verbose = False

    def enable_verbose(self):
        """
        Desactiva el printing de errores y estados de sistema
        :return: void
        """
        self._verbose = True

    def _getStructure(self):
        """
        Retorna la estructura de un paquete en forma de string
        :return: String
        """
        return "\n".join(self._structFiles)

    def _loadStructure(self):
        """
        Carga la configuración de la estructura requerida para cada tarea
        :return: None
        """
        self._fm.setWorkingDirectory(DIR_STRUCTURE)
        for f in os.listdir(DIR_STRUCTURE):  # @ReservedAssignment
            appendListToList(self._structFiles, self._fm.inspectSingleFile(f))
        self._fm.restoreWD()

    def restoreSourceFolder(self):
        """
        Reestablece el source root
        :return: void
        """
        self._sourceroot = self._defaultsourceroot
        self._fm.setDefaultWorkingDirectory(self._defaultsourceroot)
        self._fm.restoreWD()

    def setDefaultSourceFolder(self, foldername):
        """
        Establece la carpeta por defecto de los elementos a analizar (fuente)
        :param foldername: Carpeta de fuente
        :return: void
        """
        if isFolder(foldername, "") and len(foldername) > 0:
            foldername = foldername.replace("\\", "/")
            if foldername[len(foldername) - 1] != "/":
                foldername += "/"
            self._defaultsourceroot = foldername
        else:
            err.throw(err.ERROR_BADSOURCEFOLDER)

    def setSourceFolder(self, foldername):
        """
        Establece la carpeta de los elementos a analizar (fuente)
        :param foldername: Carpeta de fuente
        :return: void
        """
        if isFolder(foldername, "") and len(foldername) > 0:
            foldername = foldername.replace("\\", "/")
            if foldername[len(foldername) - 1] != "/":
                foldername += "/"
            self._sourceroot = foldername
            self._fm.setWorkingDirectory(foldername)
        else:
            err.throw(err.ERROR_BADSOURCEFOLDER)

    def _validateStructureFile(self, filename):
        """
        Función que valida si un archivo cumple con la estructura pedida
        :param filename: Archivo a comprobar
        :return:
        """
        folderfiles = self._fm.inspectSingleFile(filename)
        for structfile in self._structFiles:
            found = False
            for datafile in folderfiles:
                if regexCompare("#/" + structfile, datafile):
                    found = True
                    break
            if not found:
                return False
        return True
