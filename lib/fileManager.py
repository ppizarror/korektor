#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILE MANAGER
Administra archivos, permite obtener orden jerárquico, descomprime zip y rar, elimina archivos, etc.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    from libpath import *  # @UnusedWildImport
import os  # @Reimport
import shutil  # @UnusedImport
import zipfile
from bin.configLoader import configLoader  # @UnresolvedImport
import bin.errors as err  # @UnresolvedImport @UnusedImport
from bin.utils import isHiddenFile, isFolder, isWindows, appendListToList
from bin.varType import varTypedClass
from config import DIR_CONFIG  # @UnresolvedImport
from data import DIR_UPLOADS  # @UnusedImport

if isWindows():  # Se define el ejecutable de unrar para Windows
    from bin.binpath import DIR_BIN

    try:
        import bin.rarfile as rarfile  # @UnresolvedImport
    except Exception, e:
        err.st_error(err.ERROR_RARNOTINSTALLED_WIN, True, "rarfile", e)
    rarfile.UNRAR_TOOL = DIR_BIN + "unrar.exe"
else:  # Si no es windows se utiliza la librería patool
    import bin.rarfile as rarfile  # @UnresolvedImport @Reimport
    # try:
    #    from pyunpack import Archive  # @UnusedImport @UnresolvedImport
    # except Exception, e:
    #    err.st_error(err.ERROR_RARNOTINSTALLED_NOTWIN, True, "pyunpack", e)

# Constantes
_DEFAULT_FILE_ENCODING = "utf-8"
_DEFAULT_RAR_EXTRACT_ENCODING = "utf8"
_FILEMANAGER_Y_EXTRACT_COMPRSD_FILE = "_inspectFiles extrayo el archivo '{0}' a pesar de que ya existe como carpeta."
_FILEMANAGER_NO_EXTRACT_COMPRSD_FILE = "_inspectFiles no extrayo el archivo '{0}' dado que este ya existe."


class FileManager(varTypedClass, err.exceptionBehaviour):
    """
    Administra archivos, carga archivos, etc.
    """

    def __init__(self, wd=DIR_UPLOADS):
        """
        Constructor de la clase.

        :param wd: Working directory, carpeta de trabajo sobre la cual se cargarán los distintos archivos
        :type wd: str

        :return: void
        :rtype: None
        """

        # Se instancian los super
        err.exceptionBehaviour.__init__(self)
        varTypedClass.__init__(self)

        # Carga de configuraciones
        config = configLoader(DIR_CONFIG, "filemanager.ini")
        coreConfig = configLoader(DIR_CONFIG, "core.ini")
        folderConfig = configLoader(DIR_CONFIG, "folder.ini")
        packageConfig = configLoader(DIR_CONFIG, "packages.ini")

        # Parámetros de extracción
        self._autoExtract = config.isTrue("AUTOEXTRACT")  # Auto extraer un archivo comprimido
        self._doRemoveExtractedFolders = config.isTrue("DO_REMOVE_EXTRACTED_FOLDERS")
        self._extractIfFolderAlreadyExists = config.isTrue("REPLACE_IF_FOLDER_ALREADY_EXISTS")
        if config.paramExists("RAR_EXTRACT_ENCODING"):
            self._rarFileEncoding = config.getValue("RAR_EXTRACT_ENCODING")
        else:
            self._rarFileEncoding = _DEFAULT_RAR_EXTRACT_ENCODING

        # Parámetros de exclusión
        self._ignoredFiles = folderConfig.getValueListed("IGNORE")
        self._removeOnExtract = config.isTrue("REMOVE_ON_EXTRACT")

        # Parámetros de carácteres
        self._doCharactersRestricted = config.isTrue("CHARACTERS_DO_RESTRICT")
        self._needDotOnFile = packageConfig.isTrue("NEED_DOT_ON_FILE")
        self._validChars = packageConfig.getValue("VALID_CHARACTERS")
        self._validChars_rec = self._validChars
        self._validStructureChars = packageConfig.getValue("VALID_STRUCTURE_CHARACTERS")
        self._validRegexChars = packageConfig.getValue("VALID_REGEX_CHARACTERS")

        # Otros parámetros
        if packageConfig.paramExists("ENCODE"):
            self._fileEncoding = packageConfig.getValue("ENCODE")
        else:
            self._fileEncoding = _DEFAULT_FILE_ENCODING
        self._verbose = coreConfig.isTrue("VERBOSE")

        # Variables del FD
        self._wd = wd
        self._defaultwd = DIR_UPLOADS
        self._lastExecutionExtractedFilelist = []

    def deleteLastExtractedFiles(self):
        """
        Elimina los archivos presentes en la última ejecución del programa.

        :return: void
        :rtype: None
        """
        for i in self._lastExecutionExtractedFilelist:
            shutil.rmtree(i, True)
        self._lastExecutionExtractedFilelist = []

    def disable_autoExtract(self):
        """
        Desactiva el extraer automáticamente un archivo comprimido.

        :return: void
        :rtype: None
        """
        self._autoExtract = False

    def disable_doRemoveExtractedFolders(self):
        """
        Desactiva el borrar las carpetas extraidas tras el análisis.

        :return: void
        :rtype: None
        """
        self._doRemoveExtractedFolders = False

    def disable_extractIfFolderAlreadyExists(self):
        """
        Desactiva el extraer un archivo comprimido si es que este ya se encuentra en la carpeta padre.

        :return: void
        :rtype: None
        """
        self._extractIfFolderAlreadyExists = False

    def disable_removeOnExtract(self):
        """
        Desactiva el borrar un archivo comprimido tras extraerlo.

        :return: void
        :rtype: None
        """
        self._removeOnExtract = False

    def disable_restrictCharacters(self):
        """
        Desactiva el restringir los carácteres inválidos definidos en el parámetro de configuración VALID_CHARACTERS
        dentro de config/packages.ini.

        :return: void
        :rtype: None
        """
        self._doCharactersRestricted = False

    def disable_structureCharacters(self):
        """
        Desactiva los carácteres de la estructura como válidos, VALID_STRUCTURE_CHARACTERS reemplaza a VALID_CHARACTERS.

        :return: void
        :rtype: None
        """
        self._validChars = self._validChars_rec

    def disable_verbose(self):
        """
        Desactiva el printing de errores y estados de sistema.

        :return: void
        :rtype: None
        """
        self._verbose = False

    def enable_autoExtract(self):
        """
        Activa el extraer automáticamente un archivo comprimido.

        :return: void
        :rtype: None
        """
        self._autoExtract = True

    def enable_extractIfFolderAlreadyExists(self):
        """
        Activa el extraer un archivo comprimido si es que este ya se encuentra en la carpeta padre.

        :return: void
        :rtype: None
        """
        self._extractIfFolderAlreadyExists = True

    def enable_doRemoveExtractedFolders(self):
        """
        Activa el borrar las carpetas extraidas tras el análisis.

        :return: void
        :rtype: None
        """
        self._doRemoveExtractedFolders = True

    def enable_removeOnExtract(self):
        """
        Activa el borrar un archivo comprimido tras extraerlo.

        :return: void
        :rtype: None
        """
        self._removeOnExtract = True

    def enable_restrictCharacters(self):
        """
        Activa el restringir los carácteres inválidos definidos en el parámetro de configuración VALID_CHARACTERS dentro
        de config/packages.ini.

        :return: void
        :rtype: None
        """
        self._doCharactersRestricted = True

    def enable_structureCharacters(self):
        """
        Activa los carácteres de la estructura como válidos, VALID_STRUCTURE_CHARACTERS reemplaza a VALID_CHARACTERS.

        :return: void
        :rtype: None
        """
        self._validChars = self._validStructureChars

    def enable_verbose(self):
        """
        Desactiva el printing de errores y estados de sistema.

        :return: void
        :rtype: None
        """
        self._verbose = True

    def getFilesInWD(self):
        """
        Retorna una lista con todos los archivos dentro del WD.

        :return: Lista con nombres de archivos.
        :rtype: list
        """
        return os.listdir(self._wd.decode(self._fileEncoding))

    def _getValidRegexChars(self):
        """
        Retorna el string de los carácteres válidos para el regex.

        :return: String con carácteres válidos
        :rtype: str
        """
        return str(self._validRegexChars)

    def getWorkingDirectory(self):
        """
        Retorna el directorio root de los archivos.

        :return: Dirección del directorio root (padre)
        :rtype: str
        """
        return self._wd

    def _inspectFiles(self, d_rootpath, foldername, l_filelist=None):
        """
        Retorna una lista con los nombres de los archivos que contiene una carpeta.

        :param d_rootpath: Carpeta contenedora del archivo a analizar
        :type d_rootpath: str
        :param foldername: Nombre de la carpeta a revisar
        :type foldername: str
        :param l_filelist: Lista de archivos a agregar los nuevos encontrados
        :type l_filelist: list

        :return: Lista de archivos encontrados
        :rtype: list
        """

        foldersExtractedOnProcess = []  # Carpetas extraidas @UnusedVariable

        def _isValidFile(filnm):
            """
            Verifica si un nombre de un archivo es válido.

            :param filnm: String del nombre del archivo
            :type filnm: str

            :return: Booleano indicando validez
            :rtype: bool
            """
            for f in self._ignoredFiles:
                if f in filnm:
                    return False
            return not isHiddenFile(str(filnm))

        def _isValidFolderName(filnm):
            """
            Verifica si un nombre de una carpeta es válido (carácteres).

            :param filnm: String del nombre de la carpeta
            :type filnm: str

            :return: Booleano indicando validez
            :rtype: bool
            """
            # Si los carácteres son restrictivos
            if self._doCharactersRestricted:
                for c in filnm:
                    if c not in self._validChars:
                        return False
            return True

        def _isValidFileName(filnm):
            """
            Verifica si un nombre de un archivo es válido (carácteres).

            :param filnm: String del nombre del archivo
            :type filnm: str

            :return: Booleano indicando validez
            :rtype: bool
            """
            # Si los carácteres son restrictivos
            if self._doCharactersRestricted:
                for c in filnm:
                    if c not in self._validChars:
                        return False
            # Si requiere . en un archivo
            if self._needDotOnFile:
                return "." in filnm
            return True

        def _inspect(rootpath, filename, filelist, extractedFolders, depth=0):
            """
            Inspecciona todos los archivos de un paquete.

            :param rootpath: Carpeta contenedora
            :type rootpath: str
            :param filename: Nombre del archivo a analizar
            :type filename: str, unicode
            :param filelist: Lista de archivos actuales a agregar
            :type filelist: list
            :param extractedFolders: Lista de carpetas extraídas durante el proceso
            :type extractedFolders: list
            :param depth: Profundidad de búsqueda
            :type depth: int

            :return: void
            :rtype: None
            """

            if not _isValidFile(filename):  # Si el archivo no es válido
                return

            if self._isFolder(rootpath, filename) and _isValidFolderName(filename):  # Si el archivo es una carpeta
                pathToInspect = rootpath + filename
                for filef in os.listdir(pathToInspect.decode(self._fileEncoding)):
                    _inspect(rootpath + filename + "/", filef, filelist, extractedFolders, depth + 1)

            elif self._isZip(rootpath, filename) and self._autoExtract:  # Si el archivo es paquete zip
                newfilename = filename.replace(".zip", "").replace(".ZIP", "")
                fileAlreadyExists = False
                doExtract = True
                try:
                    fileAlreadyExists = newfilename in os.listdir(rootpath.decode(self._fileEncoding))
                except:
                    pass
                if fileAlreadyExists:
                    doExtract = doExtract and self._extractIfFolderAlreadyExists
                    if self._verbose:
                        if doExtract:
                            print _FILEMANAGER_Y_EXTRACT_COMPRSD_FILE.format(newfilename)
                        else:
                            print _FILEMANAGER_NO_EXTRACT_COMPRSD_FILE.format(newfilename)
                if doExtract:
                    zipfile.ZipFile(rootpath + filename).extractall(rootpath + newfilename + "/")
                    if self._removeOnExtract:
                        os.remove(rootpath + filename)
                    extractedFolders.append(rootpath + newfilename + "/")
                    if _isValidFolderName(newfilename):
                        _inspect(rootpath, newfilename, filelist, extractedFolders, depth + 1)

            elif self._isRar(rootpath, filename) and self._autoExtract:  # Si el archivo es paquete rar
                newfilename = filename.replace(".rar", "").replace(".RAR", "")
                fileAlreadyExists = False
                doExtract = True
                try:
                    fileAlreadyExists = newfilename in os.listdir(rootpath.decode(self._fileEncoding))
                except:
                    pass
                if fileAlreadyExists:
                    doExtract = doExtract and self._extractIfFolderAlreadyExists
                    if self._verbose:
                        if doExtract:
                            print _FILEMANAGER_Y_EXTRACT_COMPRSD_FILE.format(newfilename)
                        else:
                            print _FILEMANAGER_NO_EXTRACT_COMPRSD_FILE.format(newfilename)
                if doExtract:
                    # Si el sistema operativo huesped es Windows
                    if isWindows():
                        try:
                            rarfile.RarFile(rootpath + filename, "r", 'utf8').extractall(rootpath + newfilename + "/")
                        except Exception, ex:
                            print ""
                            err.st_error(err.ERROR_RARUNCOMPRESS, True, "rarfile", ex)
                    # Para sistemas basados en POSIX - OSX
                    else:
                        # Para linux y con Archive/pyunpack
                        # try:
                        #    os.mkdir(rootpath + newfilename + "/")
                        # except:
                        #    pass
                        try:
                            rarfile.RarFile(rootpath + filename, "r", 'utf8').extractall(rootpath + newfilename + "/")
                            # Archive(rootpath + filename).extractall(rootpath + newfilename + "/") # Para linux con Archive/pyunpack
                        except Exception, ex:
                            print ""
                            # err.st_error(err.ERROR_RARUNCOMPRESS, True, "pyunpack", e) # Para linux con Archive/pyunpack
                            err.st_error(err.ERROR_RARUNCOMPRESS_LINUX, True, "rarfile", ex)
                    if self._removeOnExtract:
                        os.remove(rootpath + filename)
                    extractedFolders.append(rootpath + newfilename + "/")
                    if _isValidFolderName(newfilename):
                        _inspect(rootpath, newfilename, filelist, extractedFolders, depth + 1)

            else:  # Si es cualquier otro archivo entonces se añade
                if _isValidFileName(filename):
                    if filename in os.listdir(rootpath.decode(self._fileEncoding)):
                        newfilename = rootpath + filename
                        if newfilename not in filelist:  # Evitar archivos duplicados
                            filelist.append(newfilename)

        def _removeExtractedFolders():
            """
            Función que elimina las carpetas extraidas durante el proceso de análisis.

            :return: void
            :rtype: None
            """
            self._lastExecutionExtractedFilelist = []
            appendListToList(self._lastExecutionExtractedFilelist, foldersExtractedOnProcess)
            if self._doRemoveExtractedFolders:
                self.deleteLastExtractedFiles()

        def _appendIfEmpty(l, f, r):
            """
            Función que añade un fichero en caso de que la lista de archivos no esta vacía.

            :param l: Lista de archivos
            :type l: list
            :param f: Nombre del archivo
            :type f: str
            :param r: Carpeta raíz del archivo
            :type r: str

            :return: void
            :rtype: None
            """
            if len(l) == 0:
                if f in os.listdir(r.decode(self._fileEncoding)) and _isValidFile(f):
                    l.append(f)

        if l_filelist is not None:
            _inspect(d_rootpath, foldername, l_filelist, foldersExtractedOnProcess, 0)
            for i in range(len(l_filelist)):
                l_filelist[i] = l_filelist[i].replace("//", "/").replace(d_rootpath, "")
            _removeExtractedFolders()
            _appendIfEmpty(l_filelist, foldername, d_rootpath)
        else:
            l_filelist = []
            _inspect(d_rootpath, foldername, l_filelist, foldersExtractedOnProcess, 0)
            for i in range(len(l_filelist)):
                l_filelist[i] = l_filelist[i].replace("//", "/").replace(d_rootpath, "")
            _removeExtractedFolders()
            _appendIfEmpty(l_filelist, foldername, d_rootpath)
            return l_filelist

    def inspectSingleFile(self, filename):
        """
        Inspecciona los elementos de un solo archivo o carpeta.

        :param filename: Nombre del archivo a inspeccionar
        :type filename: str, unicode

        :return: Lista de archivos que contiene la carpeta
        :rtype: list
        """
        return self._inspectFiles(self._wd, filename)

    # noinspection PyMethodMayBeStatic
    def _isFolder(self, rootpath, filename):
        """
        Comprueba si un nombre de carpeta es un directorio en el sistema huésped.

        :param rootpath: Ubicación del archivo
        :type rootpath: str
        :param filename: Nombre del archivo
        :type filename: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        return isFolder(rootpath, filename)

    # noinspection PyMethodMayBeStatic
    def _isRar(self, rootpath, filename):
        """
        Comprueba si el paquete es un archivo rar.

        :param rootpath: Ubicación del archivo
        :type rootpath: str
        :param filename: Archivo a analizar
        :type filename: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        if ".rar" in filename.lower():
            try:
                rarfile.RarFile(rootpath + filename, "r", "utf8")
                # Archive(rootpath + filename) para linux
                return True
            except:
                return False
        return False

    # noinspection PyMethodMayBeStatic
    def _isZip(self, rootpath, filename):
        """
        Comprueba si un paquete es un zip.

        :param rootpath: Ubicación del archivo
        :type rootpath: str
        :param filename: Archivo a analizar
        :type filename: str

        :return: Booleano indicando pertenencia
        :rtype: bool
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
        Imprime una lista de archivos resultante de inspectFiles.

        :param fl: Lista de archivos
        :type fl: list
        :param filename: Nombre de la carpeta contenedora
        :type filename: str

        :return: void
        :rtype: None
        """
        if fl is not None:
            print "Archivos de " + self.getWorkingDirectory() + filename
            if len(fl) > 0:
                for i in range(0, len(fl)):
                    print "\t", fl[i]
            else:
                print "\t", err.ERROR_NOFILES

    def _printFilesInWD(self):
        """
        Imprime los archivos que están dentro del working directory.

        :return: void
        :rtype: None
        """
        for f in os.listdir(self._wd.decode(self._fileEncoding)):  # @ReservedAssignment
            print f

    def printSingleFile(self, filename):
        """
        Imprime los archivos dentro de una sola carpeta.

        :param filename: Nombre del archivo a analizar
        :type filename: str, unicode

        :return: void
        :rtype: None
        """
        print self._printFileList(self.inspectSingleFile(filename), filename)

    def printTree(self):
        """
        Imprime los archivos de cada una de las carpetas del working directory.

        :return: void
        :rtype: None
        """
        for f in os.listdir(self._wd.decode(self._fileEncoding)):  # @ReservedAssignment
            if f is not None:
                self.printSingleFile(f)

    def restoreWD(self):
        """
        Retorna el wd al estado por defecto.

        :return: void
        :rtype: None
        """
        self.setWorkingDirectory(self._defaultwd)

    def setDefaultWorkingDirectory(self, new_wd):
        """
        Establece el directorio root por defecto del working directory.

        :param new_wd: Ubicación del nuevo working directory por defecto
        :type new_wd: str

        :return: void
        :rtype: None
        """
        if self._isFolder(new_wd, "") and len(new_wd) > 0:
            new_wd = new_wd.replace("\\", "/").replace("//", "/")
            if new_wd[len(new_wd) - 1] != "/":
                new_wd += "/"
            self._defaultwd = new_wd
        else:
            err.throw(err.ERROR_BADWD)

    def _setFileEncoding(self, enc):
        """
        Establece la codificación de los nombres de los archivos.

        :param enc: Codificación de cada uno de los nombres de los archivos
        :type enc: str, unicode

        :return: void
        :rtype: None
        """
        self._fileEncoding = enc

    def setWorkingDirectory(self, new_wd):
        """
        Establece el directorio root del working directory.

        :param new_wd: Ubicación del nuevo working directory
        :type new_wd: str

        :return: void
        :rtype: None
        """
        if self._isFolder(new_wd, "") and len(new_wd) > 0:
            new_wd = new_wd.replace("\\", "/").replace("//", "/")
            if new_wd[len(new_wd) - 1] != "/":
                new_wd += "/"
            self._wd = new_wd
        else:
            err.throw(err.ERROR_BADWD)

    def tree(self):
        """
        Retorna una lista con todos los archivos de cada uno de los elementos.

        :return: Lista con archivos de cada una de las carpetas del working directory
        :rtype: list
        """
        treelist = []
        for f in os.listdir(self._wd.decode(self._fileEncoding)):  # @ReservedAssignment
            if f is not None:
                treelist.append(self.inspectSingleFile(f))
        return treelist
