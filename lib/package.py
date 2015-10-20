#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PACKAGE
# Testea que los paquetes entregados por los alumnos tengan una estructura correcta
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: ABRIL 2015
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__': from libpath import *  # @UnusedWildImport
from bin.configLoader import configLoader
from bin.utils import isHiddenFile, isFolder, regexCompare
import zipfile
from data import *  # @UnusedWildImport
from config import DIR_CONFIG
import bin.errors as err


# Constantes
PACKAGE_TESTER_ERROR_NO_FOUND = "El archivo consultado no existe"
ZIP_VALIDATE_FAIL = "ZIP-PACKAGE-FAIL"
ZIP_VALIDATE_OK = "ZIP-PACKAGE-OK"


class packageTester:
    """
    Clase package, carga paquetes en formato .zip y comprueba que cumplan con un
    formato específico.
    Posee ademas funciones utilitarias para descomprimir en un formato específico.
    """

    def __init__(self):
        # Carga de configuraciones
        config = configLoader(DIR_CONFIG, "packages.ini")  # Configuraciones de los paquetes
        self.packageStructedFiles = []  # Lista con archivos requeridos para cada package
        self.validChars = config.getValue("VALID_CHARACTERS")  # Caracteres válidos de los archivos del paquete
        self.validRegexChars = config.getValue("VALID_REGEX_CHARACTERS")  # Caracteres válidos para los regex
        # Genera la estructura
        self.structFiles = []
        self.loadStructure()

    def loadStructure(self):
        """
        Carga la configuración de la estructura requerida para cada tarea
        :return: None
        """

        folderConfig = configLoader(DIR_CONFIG, "folder.ini")
        ignoredFiles = folderConfig.getValueListed("IGNORE")

        def _isValidFile(filename):
            for c in filename:
                if c not in self.validChars:
                    return False
            return True

        # noinspection PyShadowingBuiltins
        def _walk(parent, dir, depth):  # @ReservedAssignment
            """
            Función que se mueve entre las carpetas buscando archivos de forma recursiva
            :param dir: Directorio en string
            :return:
            """
            # Recorre cada archivo de dir buscando archivos y agregandolos packageStructedFiles
            for i in os.listdir(parent + dir):
                if i not in ignoredFiles and not isHiddenFile(i) and _isValidFile(i):
                    if depth != 0:
                        filec = dir + "/" + i
                    else:
                        filec = i
                    if isFolder(dir, i):
                        _walk(parent, filec, depth + 1)
                    else:
                        self.structFiles.append(filec)

        def _searchFiles():
            """
            Busca archivos válidos en la estructura de los paquetes
            :return:
            """
            _walk(DIR_STRUCTURE, "", 0)

        _searchFiles()

    def validateZip(self, filename):
        """
        Función que valida si un zip cumple con la estructura determinada
        :param filename: Nombre del archivo
        :return: Boolean
        """
        try:
            data = zipfile.ZipFile(DIR_UPLOADS + filename)
        except:
            err.warning(PACKAGE_TESTER_ERROR_NO_FOUND)
            return False
        for structfile in self.structFiles:
            found = False
            for datafile in data.namelist():
                if regexCompare(structfile, datafile):
                    found = True
                    break
            if not found:
                return False
        return True


# Test
if __name__ == "__main__":
    p = packageTester()
    p.validateZip("cc3001.zip")
