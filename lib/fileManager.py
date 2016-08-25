#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# FILE MANAGER
# Administra archivos, permite obtener orden jerárquico, descomprime zip y rar, elimina archivos, etc.
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from libpath import *  # @UnusedWildImport
import shutil  # @UnusedImport
import zipfile
import os  # @Reimport
from bin.configLoader import configLoader  # @UnresolvedImport
import bin.errors as err  # @UnresolvedImport @UnusedImport
from bin.utils import isHiddenFile, isFolder, isWindows, appendListToList
from config import DIR_CONFIG  # @UnresolvedImport
from data import DIR_UPLOADS  # @UnusedImport

# Se define el ejecutable de unrar para Windows
if isWindows():
    from bin.binpath import DIR_BIN
    try:
        import bin.rarfile as rarfile  # @UnresolvedImport
    except Exception, e:
        err.st_error(err.ERROR_RARNOTINSTALLED_WIN, True, "rarfile", e)
    rarfile.UNRAR_TOOL = DIR_BIN + "unrar.exe"

# Si no es windows se utiliza la librería patool
else:
    try:
        from pyunpack import Archive  # @UnusedImport @UnresolvedImport
    except Exception, e:
        err.st_error(err.ERROR_RARNOTINSTALLED_NOTWIN, True, "pyunpack", e)


# noinspection PyUnresolvedReferences
class FileManager:
    """
    filemanager: Administra archivos, carga archivos, etc.
    """

    def __init__(self, wd=DIR_UPLOADS):
        """
        Constructor
        :param wd: Working directory
        :return: void
        """

        # Carga de configuraciones
        config = configLoader(DIR_CONFIG, "filemanager.ini")
        coreConfig = configLoader(DIR_CONFIG, "core.ini")
        folderConfig = configLoader(DIR_CONFIG, "folder.ini")
        packageConfig = configLoader(DIR_CONFIG, "packages.ini")
        self._autoExtract = config.isTrue("AUTOEXTRACT")  # Auto extraer un archivo comprimido
        # Eliminar carpetas extraidas tras el análisis
        self._doCharactersRestricted = packageConfig.isTrue("CHARACTERS_DO_RESTRICT")
        self._doRemoveExtractedFolders = config.isTrue("DO_REMOVE_EXTRACTED_FOLDERS")
        self._ignoredFiles = folderConfig.getValueListed("IGNORE")
        self._needDotOnFile = packageConfig.isTrue("NEED_DOT_ON_FILE")
        self._removeOnExtract = config.isTrue("REMOVE_ON_EXTRACT")
        # Eliminar un archivo comprimido tras extraerlo
        self._validChars = packageConfig.getValue("VALID_CHARACTERS")
        # Caracteres válidos de los archivos del paquete
        self._validRegexChars = packageConfig.getValue("VALID_REGEX_CHARACTERS")
        # Caracteres válidos para los regex
        self._verbose = coreConfig.isTrue("VERBOSE")  # Imprimir el estado del sistema

        # Variables del FD
        self._wd = wd
        self._defaultwd = DIR_UPLOADS
        self._lastExecutionExtractedFilelist = []

    def deleteLastExtractedFiles(self):
        """
        Elimina los archivos presentes en la última ejecución del programa
        :return: void
        """
        for i in self._lastExecutionExtractedFilelist:
            shutil.rmtree(i, True)
        self._lastExecutionExtractedFilelist = []

    def disable_autoExtract(self):
        """
        Desactiva el extraer automáticamente un archivo comprimido
        :return: void
        """
        self._autoExtract = False

    def disable_doRemoveExtractedFolders(self):
        """
        Desactiva el borrar las carpetas extraidas tras el análisis
        :return: void
        """
        self._doRemoveExtractedFolders = False

    def disable_removeOnExtract(self):
        """
        Desactiva el borrar un archivo comprimido tras extraerlo
        :return: void
        """
        self._removeOnExtract = False

    def enable_autoExtract(self):
        """
        Activa el extraer automáticamente un archivo comprimido
        :return: void
        """
        self._autoExtract = True

    def enable_doRemoveExtractedFolders(self):
        """
        Activa el borrar las carpetas extraidas tras el análisis
        :return: void
        """
        self._doRemoveExtractedFolders = True

    def enable_removeOnExtract(self):
        """
        Activa el borrar un archivo comprimido tras extraerlo
        :return: void
        """
        self._removeOnExtract = True

    def getWorkingDirectory(self):
        """
        Retorna el directorio root de los archivos
        :return: String
        """
        return self._wd

    def _inspectFiles(self, rootpath, filename, filelist=None):
        """
        Retorna una lista con los nombres de los archivos del paquete
        :param rootpath: Carpeta contenedora
        :param filename: Archivo
        :param removeOnExtract: Remover al extraer un zip o rar
        :param filelist: lista de archivos
        :return:
        """

        foldersExtractedOnProcess = []  # Carpetas extraidas @UnusedVariable

        def _inspect(rootpath, filename, filelist, extractedFolders, depth=0):
            """
            Inspecciona todos los archivos de un paquete
            :param rootpath: Carpeta contenedora
            :param filename: Nombre del paquete a inspeccionar
            :param filelist: Lista de archivos
            :return:
            """

            def _isValidFile(filename):
                for f in self._ignoredFiles:
                    if f in filename:
                        return False
                return not isHiddenFile(str(filename))

            def _isValidFileName(filename):
                # Si los carácteres son restrictivos
                if self._doCharactersRestricted:
                    for c in filename:
                        if c not in self._validChars:
                            return False
                # Si requiere . en un archivo
                if self._needDotOnFile:
                    return "." in filename
                return True

            if not _isValidFile(filename):  # Si el archivo no es válido
                return

            if self._isFolder(rootpath, filename):  # Si el archivo es una carpeta
                for filef in os.listdir(rootpath + filename):
                    _inspect(rootpath + filename + "/", filef, filelist, extractedFolders, depth + 1)

            elif self._isZip(rootpath, filename) and self._autoExtract:  # Si el archivo es paquete zip
                newfilename = filename.replace(".zip", "").replace(".ZIP", "")
                zipfile.ZipFile(rootpath + filename).extractall(rootpath + newfilename + "/")
                if self._removeOnExtract:
                    os.remove(rootpath + filename)
                extractedFolders.append(rootpath + newfilename + "/")
                _inspect(rootpath, newfilename, filelist, extractedFolders, depth + 1)

            elif self._isRar(rootpath, filename) and self._autoExtract:  # Si el archivo es paquete rar
                newfilename = filename.replace(".rar", "").replace(".RAR", "")
                if isWindows():
                    try:
                        rarfile.RarFile(rootpath + filename, "r", 'utf8').extractall(rootpath + newfilename + "/")
                    except Exception, e:
                        print ""
                        err.st_error(err.ERROR_RARUNCOMPRESS, True, "rarfile", e)
                else:
                    try:
                        os.mkdir(rootpath + newfilename + "/")
                    except:
                        pass
                    try:
                        Archive(rootpath + filename).extractall(rootpath + newfilename + "/")
                    except Exception, e:
                        print ""
                        err.st_error(err.ERROR_RARUNCOMPRESS, True, "pyunpack", e)
                if self._removeOnExtract:
                    os.remove(rootpath + filename)
                extractedFolders.append(rootpath + newfilename + "/")
                _inspect(rootpath, newfilename, filelist, extractedFolders, depth + 1)

            else:  # Si es cualquier otro archivo entonces se añade
                if _isValidFileName(filename):
                    filelist.append(rootpath + filename)

        def _removeExtractedFolders():
            """
            Función que elimina las carpetas extraidas durante el proceso de análisis
            :return: void
            """
            self._lastExecutionExtractedFilelist = []
            appendListToList(self._lastExecutionExtractedFilelist, foldersExtractedOnProcess)
            if self._doRemoveExtractedFolders:
                self.deleteLastExtractedFiles()

        if filelist is not None:
            _inspect(rootpath, filename, filelist, foldersExtractedOnProcess, 0)
            for i in range(len(filelist)):
                filelist[i] = filelist[i].replace("//", "/").replace(rootpath, "")
            _removeExtractedFolders()
        else:
            filelist = []
            _inspect(rootpath, filename, filelist, foldersExtractedOnProcess, 0)
            for i in range(len(filelist)):
                filelist[i] = filelist[i].replace("//", "/").replace(rootpath, "")
            _removeExtractedFolders()
            return filelist

    def inspectSingleFile(self, filename):
        """
        Inspecciona los elementos de un solo archivo
        :return: List
        """
        return self._inspectFiles(self._wd, filename)

    def _isFolder(self, rootpath, filename):
        """
        Comprueba si un paquete es un directorio
        :param filename: Nombre del archivo
        :param rootpath: Ubicación del archivo
        :return:
        """
        return isFolder(rootpath, filename)

    def _isRar(self, rootpath, filename):
        """
        Comprueba si el paquete es un archivo rar
        :param rootpath: Ubicación del archivo
        :param filename: Archivo a analizar
        :return:
        """
        if ".rar" in filename.lower():
            if isWindows():
                try:
                    rarfile.RarFile(rootpath + filename, "r", "utf8")
                    return True
                except:
                    return False
            else:
                try:
                    Archive(rootpath + filename)
                    return True
                except:
                    return False
        return False

    def _isZip(self, rootpath, filename):
        """
        Comprueba si un paquete es un zip
        :param filename: Nombre del archivo
        :param rootpath: Ubicación del archivo
        :return:
        """
        if ".zip" in filename.lower():
            try:
                zipfile.ZipFile(rootpath + filename)
                return True
            except:
                return False
        return False

    def _printFileList(self, fl, filename):
        """
        Imprime una lista de archivos resultante de inspectFiles
        :return: void
        """
        if fl is not None:
            print "Archivos de " + self.getWorkingDirectory() + filename
            if len(fl) > 0:
                for i in range(0, len(fl)):
                    print "\t", fl[i]
            else:
                print "\t", err.ERROR_NOFILES

    def printSingleFile(self, filename):
        """
        Imprime la lista de archivos de un solo elemento dentro del wd
        :return: void
        """
        return self._printFileList(self.inspectSingleFile(filename), filename)

    def printTree(self):
        """
        Imprime la estructura de cada archivo del wd
        :return: void
        """
        for f in os.listdir(self._wd):  # @ReservedAssignment
            if f is not None:
                self.printSingleFile(f)

    def restoreWD(self):
        """
        Retorna el wd al estado por defecto
        :return: void
        """
        self.setWorkingDirectory(self._defaultwd)

    def setDefaultWorkingDirectory(self, new_wd):
        """
        Establece el directorio root de los archivos
        :return: String
        """
        if self._isFolder(new_wd, "") and len(new_wd) > 0:
            new_wd = new_wd.replace("\\", "/")
            if new_wd[len(new_wd) - 1] != "/":
                new_wd += "/"
            self._defaultwd = new_wd
        else:
            err.throw(err.ERROR_BADWD)

    def setWorkingDirectory(self, new_wd):
        """
        Establece el directorio root de los archivos
        :return: String
        """
        if self._isFolder(new_wd, "") and len(new_wd) > 0:
            new_wd = new_wd.replace("\\", "/")
            if new_wd[len(new_wd) - 1] != "/":
                new_wd += "/"
            self._wd = new_wd
        else:
            err.throw(err.ERROR_BADWD)

    def tree(self):
        """
        Retorna una lista con todos los archivos de cada uno de los elementos
        :return: list
        """
        treelist = []
        for f in os.listdir(self._wd):  # @ReservedAssignment
            if f is not None:
                treelist.append(self.inspectSingleFile(f))
        return treelist
