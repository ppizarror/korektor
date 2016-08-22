#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# Filemanager
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
from bin.configLoader import configLoader  # @UnresolvedImport
import bin.errors as err  # @UnresolvedImport @UnusedImport
from bin.utils import isHiddenFile, isFolder, printBarsConsole, isWindows  # @UnresolvedImport @Reimport @UnusedImport
from config import DIR_CONFIG  # @UnresolvedImport
from data import DIR_UPLOADS  # @UnusedImport

# Se define el ejecutable de unrar para Windows
if isWindows():
    from bin.binpath import DIR_BIN
    try:
        import bin.rarfile as rarfile  # @UnresolvedImport
    except:
        err.st_error(err.ERROR_RARNOTINSTALLED_WIN, True, "rarfile")
    rarfile.UNRAR_TOOL = DIR_BIN + "unrar.exe"

# Si no es windows se utiliza la librería patool
else:
    try:
        from pyunpack import Archive  # @UnusedImport @UnresolvedImport
    except:
        err.st_error(err.ERROR_RARNOTINSTALLED_NOTWIN, True, "pyunpack")

# Constantes
PACKAGE_TESTER_ERROR_NO_FOUND = "El archivo consultado no existe"
PACKAGE_VALIDATE_FAIL = "FOLDER-PACKAGE-FAIL"
PACKAGE_VALIDATE_OK = "FOLDER-PACKAGE-OK"
ZIP_VALIDATE_FAIL = "ZIP-PACKAGE-FAIL"
ZIP_VALIDATE_OK = "ZIP-PACKAGE-OK"


# noinspection PyUnresolvedReferences
class Filemanager:
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
        self._doRemoveExtractedFolders = config.isTrue("DO_REMOVE_EXTRACTED_FOLDERS")  # Eliminar carpetas extraidas tras el análisis
        self._ignoredFiles = folderConfig.getValueListed("IGNORE")
        self._removeOnExtract = config.isTrue("REMOVE_ON_EXTRACT")  # Eliminar un archivo comprimido tras extraerlo
        self._validChars = packageConfig.getValue("VALID_CHARACTERS")  # Caracteres válidos de los archivos del paquete
        self._validRegexChars = packageConfig.getValue("VALID_REGEX_CHARACTERS")  # Caracteres válidos para los regex
        self._verbose = coreConfig.isTrue("VERBOSE")  # Imprimir el estado del sistema

        # Variables del FD
        self._wd = wd

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
                for c in filename:
                    if c not in self._validChars:
                        return False
                return "." in filename

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
                        rarfile.RarFile(rootpath + filename).extractall(rootpath + newfilename + "/")
                    except:
                        print ""
                        err.st_error(err.ERROR_RARUNCOMPRESS, True, "rarfile")
                else:
                    try:
                        os.mkdir(rootpath + newfilename + "/")
                    except:
                        pass
                    Archive(rootpath + filename).extractall(rootpath + newfilename + "/")
                    try:
                        Archive(rootpath + filename).extractall(rootpath + newfilename + "/")
                    except:
                        print ""
                        err.st_error(err.ERROR_RARUNCOMPRESS, True, "pyunpack")
                if self._removeOnExtract:
                    os.remove(rootpath + filename)
                extractedFolders.append(rootpath + newfilename + "/")
                _inspect(rootpath, newfilename, filelist, extractedFolders, depth + 1)

            else:  # Si es cualquier otro archivo entonces se añade
                if depth > 0:
                    if _isValidFileName(filename):
                        filelist.append(rootpath + filename)

        def _removeExtractedFolders():
            """
            Función que elimina las carpetas extraidas durante el proceso de análisis
            :return: void
            """
            if self._doRemoveExtractedFolders:
                for i in foldersExtractedOnProcess:
                    shutil.rmtree(i, True)

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
        if ".rar" in filename:
            if isWindows():
                try:
                    rarfile.RarFile(rootpath + filename)
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
        if ".zip" in filename:
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
                fm.printSingleFile(f)

    def restoreWD(self):
        """
        Retorna el wd al estado por defecto
        :return: void
        """
        self.setWorkingDirectory(DIR_UPLOADS)

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


if __name__ == "__main__":

    # Importación de recursos para el testeo
    from data import DIR_TEST

    # Creación del objeto de filemanager
    fm = Filemanager()

    # Configuración del filemanager
    fm.enable_autoExtract()
    fm.enable_doRemoveExtractedFolders()
    fm.disable_removeOnExtract()

    # Testeo del cambio del wd
    printBarsConsole("Testeo del wd")
    fm.setWorkingDirectory("C:/")
    print "Wd actual", fm.getWorkingDirectory()
    print "Restaurando WD"
    fm.restoreWD()
    print "Wd actual", fm.getWorkingDirectory()
    print "Definiendo WD de testeo"
    fm.setWorkingDirectory(DIR_TEST)
    print "Wd actual", fm.getWorkingDirectory()

    # Testeo de carpetas unicas sin archivos comprimidos
    printBarsConsole("Testeo carpetas unicas")
    fm.printSingleFile("Folder 1")
    fm.printSingleFile("Folder 2")

    # Testeo de un archivo zip
    printBarsConsole("Testeo de archivo zip")
    fm.printSingleFile("Zip Folder.zip")

    # Testeo de archivos prohibidos
    printBarsConsole("Testeo de archivos prohibidos")
    fm.printSingleFile("__MACOSX")

    # Testeo de un archivo rar
    printBarsConsole("Testeo de archivo rar")
    fm.printSingleFile("Rar Folder.rar")

    # Testeo de una carpeta con un archivo zip
    printBarsConsole("Testeo de una carpeta con un archivo zip dentro")
    fm.printSingleFile("Folder 4")

    # Testeo de una carpeta con un archivo rar
    printBarsConsole("Testeo de una carpeta con un archivo rar dentro")
    fm.printSingleFile("Folder 3")

    # Testeo de un archivo
    printBarsConsole("Testeo de un solo archivo")
    fm.printSingleFile("ABOUT")

    # Testeo de una carpeta real
    fm.setWorkingDirectory("C:\Users\pablo\Downloads\Tarea_5")
    fm.printTree()
