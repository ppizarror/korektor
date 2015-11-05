#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# PACKAGE
# Testea que los paquetes entregados por los alumnos tengan una estructura correcta
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from libpath import *  # @UnusedWildImport
from bin.configLoader import configLoader  # @UnresolvedImport
from bin.utils import isHiddenFile, isFolder, regexCompare
import zipfile
from data import *  # @UnusedWildImport
from config import DIR_CONFIG  # @UnresolvedImport
import bin.errors as err  # @UnresolvedImport

# Constantes
PACKAGE_TESTER_ERROR_NO_FOUND = "El archivo consultado no existe"
PACKAGE_VALIDATE_FAIL = "FOLDER-PACKAGE-FAIL"
PACKAGE_VALIDATE_OK = "FOLDER-PACKAGE-OK"
ZIP_VALIDATE_FAIL = "ZIP-PACKAGE-FAIL"
ZIP_VALIDATE_OK = "ZIP-PACKAGE-OK"


class Package:
    """
    package: Paquetes de usuario el cual provee funciones para acceder a los contenidos
    de cada paquete, como tambien la estructura básica pedida
    """

    def __init__(self):
        # Carga de configuraciones
        config = configLoader(DIR_CONFIG, "packages.ini")
        folderConfig = configLoader(DIR_CONFIG, "folder.ini")
        self.ignoredFiles = folderConfig.getValueListed("IGNORE")
        self.packageStructedFiles = []  # Lista con archivos requeridos para cada package
        # Caracteres válidos de los archivos del paquete
        self.validChars = config.getValue("VALID_CHARACTERS")
        self.validRegexChars = config.getValue(
            "VALID_REGEX_CHARACTERS")  # Caracteres válidos para los regex
        # Genera la estructura
        self.structFiles = []
        self.loadStructure()

    def _inspect(self, rootpath, packpath, filelist, lookdepth):
        """
        Inspecciona todos los archivos en un directorio y los retorna en una lista
        :param rootpath: Nombre del directorio contenedor del paquete
        :param packpath: Nombre del paquete a analizar
        :param filelist: Lista a guardar las direcciones
        :return:
        """

        def _isValidFile(filename):
            for c in filename:
                if c not in self.validChars:
                    return False
            return True

        # noinspection PyShadowingBuiltins
        def _walk(parent, dirf, depth, filelist):  # @ReservedAssignment
            """
            Función que se mueve entre las carpetas buscando archivos de forma recursiva
            :param dir: Directorio en string
            :return:
            """
            # Recorre cada archivo de dir buscando archivos y agregandolos
            # packageStructedFiles
            for i in os.listdir(parent + dirf):
                if i not in self.ignoredFiles and not isHiddenFile(i) and _isValidFile(i):
                    if depth != 0:
                        filec = dirf + "/" + i
                    else:
                        filec = i
                    if isFolder(parent, filec):
                        _walk(parent, filec, depth + 1, filelist)
                    else:
                        filelist.append(filec)

        if self.isFolder(rootpath, packpath):
            _walk(rootpath, packpath, lookdepth,
                  filelist)  # @UndefinedVariable
        elif self.isZip(rootpath, packpath):
            for file in zipfile.ZipFile(rootpath + packpath).namelist():
                filelist.append(file)
        else:
            pass

    def getStructure(self):
        """
        Retorna la estructura de un paquete en forma de string
        :return: String
        """
        return "\n".join(self.structFiles)

    def isFolder(self, rootpath, filename):
        """
        Comprueba si un paquete es un directorio
        :param filename: Nombre del archivo
        :return:
        """
        return isFolder(rootpath, filename)

    def isZip(self, rootpath, filename):
        """
        Comprueba si un paquete es un zip o un directorio
        :param filename: Nombre del archivo
        :return:
        """
        if ".zip" in filename:
            try:
                data = zipfile.ZipFile(rootpath + filename)
                return True
            except:
                return False
        return False

    def loadStructure(self):
        """
        Carga la configuración de la estructura requerida para cada tarea
        :return: None
        """
        self._inspect(DIR_STRUCTURE, "", self.structFiles, 0)

    def validateStructure(self, filename):
        """
        Función que valida si un paquete cumple con la estructura
        :param filename:
        :return:
        """
        folderfiles = []
        self._inspect(DIR_UPLOADS, filename, folderfiles, 1)
        for structfile in self.structFiles:
            found = False
            for datafile in folderfiles:
                if regexCompare(structfile, datafile):
                    found = True
                    break
            if not found:
                return False
        return True


# Test
if __name__ == "__main__":
    p = Package()
    print p.getStructure()
    print p.validateStructure("zipupload.zip")
    print p.validateStructure("cc3001")
    print p.validateStructure("cc3001_fake")
