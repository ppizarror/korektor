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
import bin.rarfile as rarfile

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

    def getStructure(self):
        """
        Retorna la estructura de un paquete en forma de string
        :return: String
        """
        return "\n".join(self.structFiles)

    def inspectFiles(self, rootpath, filename, removeOnExtract=False, filelist=None):
        """
        Retorna una lista con los nombres de los archivos del paquete
        :param rootpath: Carpeta contenedora
        :param filename: Archivo
        :param removeOnExtract: Remover al extraer un zip o rar
        :param filelist: lista de archivos
        :return:
        """

        def _inspect(rootpath, filename, filelist, depth=0):
            """
            Inspecciona todos los archivos de un paquete
            :param rootpath: Carpeta contenedora
            :param filename: Nombre del paquete a inspeccionar
            :param filelist: Lista de archivos
            :return:
            """

            def _isValidFile(filename):
                for f in self.ignoredFiles:
                    if f in filename:
                        return False
                return not isHiddenFile(str(filename))

            def _isValidFileName(filename):
                for c in filename:
                    if c not in self.validChars:
                        return False
                return "." in filename

            def _getMainFolder(filelist):
                for f in filelist:
                    f = f.replace("\\", "/")
                    if "/" in f:
                        return f.split("/")[0]

            if self.isFolder(rootpath, filename):  # Si el archivo es una carpeta
                for filef in os.listdir(rootpath + filename):
                    if _isValidFile(filef):
                        _inspect(rootpath + filename + "/", filef, filelist, depth + 1)
            elif self.isZip(rootpath, filename):  # Si el archivo es paquete rar
                zipfile.ZipFile(rootpath + filename).extractall(DIR_UPLOADS)
                folder = _getMainFolder(zipfile.ZipFile(rootpath + filename).namelist())
                if removeOnExtract:
                    os.remove(rootpath + filename)
                _inspect(rootpath, folder, filelist, depth + 1)
            elif self.isRar(rootpath, filename):  # Si el archivo es paquete zip
                rarfile.RarFile(rootpath + filename).extractall(DIR_UPLOADS)
                folder = _getMainFolder(rarfile.RarFile(rootpath + filename).namelist())
                if removeOnExtract:
                    os.remove(rootpath + filename)
                _inspect(rootpath, str(folder), filelist, depth + 1)
            else:  # Si es cualquier otro archivo entonces se añade
                if depth > 0:
                    if _isValidFileName(filename):
                        filelist.append(rootpath + filename)

        if filelist is not None:
            _inspect(rootpath, filename, filelist)
            for i in range(len(filelist)):
                filelist[i] = filelist[i].replace("//", "/").replace(rootpath, "")
        else:
            filelist = []
            _inspect(rootpath, filename, filelist)
            for i in range(len(filelist)):
                filelist[i] = filelist[i].replace("//", "/").replace(rootpath, "")
            return filelist

    def isFolder(self, rootpath, filename):
        """
        Comprueba si un paquete es un directorio
        :param filename: Nombre del archivo
        :param rootpath: Ubicación del archivo
        :return:
        """
        return isFolder(rootpath, filename)

    def isRar(self, rootpath, filename):
        """
        Comprueba si el paquete es un archivo rar
        :param rootpath: Ubicación del archivo
        :param filename: Archivo a analizar
        :return:
        """
        if ".rar" in filename:
            try:
                data = rarfile.RarFile(rootpath + filename)
                return True
            except:
                return False
        return False

    def isZip(self, rootpath, filename):
        """
        Comprueba si un paquete es un zip
        :param filename: Nombre del archivo
        :param rootpath: Ubicación del archivo
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
        self.inspectFiles(DIR_STRUCTURE, "", False, self.structFiles)

    def validateStructure(self, filename):
        """
        Función que valida si un paquete cumple con la estructura
        :param filename:
        :return:
        """
        folderfiles = self.inspectFiles(DIR_UPLOADS, filename, False)
        print folderfiles
        for structfile in self.structFiles:
            found = False
            for datafile in folderfiles:
                if regexCompare(structfile, datafile):
                    found = True
                    break
            if not found:
                return False
        return True  # Test


if __name__ == "__main__":
    p = Package()
    print p.getStructure()
    for file in os.listdir(DIR_UPLOADS):
       a = p.validateStructure(file)
       print a
    # p.validateStructure("Aguirre_Munoz__Daniel_Patricio.zip")
    # p.validateStructure("zipfile.zip")
    # p.validateStructure("rarfile.rar")
    # p.validateStructure("pablo_pizarro")
