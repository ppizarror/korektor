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
from bin.configloader import ConfigLoader  # @UnresolvedImport
import bin.errors as err  # @UnresolvedImport @UnusedImport
from bin.ostype import is_windows
from bin.utils import is_hidden_file_utils, is_folder_utils, append_list_to_list
from bin.vartype import VarTypedClass
from config import DIR_CONFIG  # @UnresolvedImport
from data import DIR_UPLOADS  # @UnusedImport

if is_windows():  # Se define el ejecutable de unrar para Windows
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
_FILEMANAGER_Y_EXTRACT_COMPRSD_FILE = "_inspect_files extrajo el archivo '{0}' a pesar de que ya existe como carpeta."
_FILEMANAGER_NO_EXTRACT_COMPRSD_FILE = "_inspect_files no extrajo el archivo '{0}' dado que este ya existe."


class FileManager(VarTypedClass, err.ExceptionBehaviour):
    """
    Administra archivos, carga archivos, etc.
    """

    # noinspection SpellCheckingInspection
    def __init__(self, wd=DIR_UPLOADS):
        """
        Constructor de la clase.

        :param wd: Working directory, carpeta de trabajo sobre la cual se cargarán los distintos archivos
        :type wd: str

        :return: void
        :rtype: None
        """
        # Se instancian los super
        err.ExceptionBehaviour.__init__(self)
        VarTypedClass.__init__(self)

        # Carga de configuraciones
        config = ConfigLoader(DIR_CONFIG, "filemanager.ini")
        core_config = ConfigLoader(DIR_CONFIG, "core.ini")
        folder_config = ConfigLoader(DIR_CONFIG, "folder.ini")
        package_config = ConfigLoader(DIR_CONFIG, "packages.ini")

        # Parámetros de extracción
        self._autoExtract = config.is_true("AUTOEXTRACT")  # Auto extraer un archivo comprimido
        self._doRemoveExtractedFolders = config.is_true("DO_REMOVE_EXTRACTED_FOLDERS")
        self._extractIfFolderAlreadyExists = config.is_true("REPLACE_IF_FOLDER_ALREADY_EXISTS")
        if config.param_exists("RAR_EXTRACT_ENCODING"):
            self._rarFileEncoding = config.get_value("RAR_EXTRACT_ENCODING")
        else:
            self._rarFileEncoding = _DEFAULT_RAR_EXTRACT_ENCODING

        # Parámetros de exclusión
        self._ignoredFiles = folder_config.get_value_listed("IGNORE")
        self._removeOnExtract = config.is_true("REMOVE_ON_EXTRACT")

        # Parámetros de caracteres
        self._doCharactersRestricted = config.is_true("CHARACTERS_DO_RESTRICT")
        self._needDotOnFile = package_config.is_true("NEED_DOT_ON_FILE")
        self._validChars = package_config.get_value("VALID_CHARACTERS")
        self._validChars_rec = self._validChars
        self._validStructureChars = package_config.get_value("VALID_STRUCTURE_CHARACTERS")
        self._validRegexChars = package_config.get_value("VALID_REGEX_CHARACTERS")

        # Otros parámetros
        if package_config.param_exists("ENCODE"):
            self._fileEncoding = package_config.get_value("ENCODE")
        else:
            self._fileEncoding = _DEFAULT_FILE_ENCODING
        self._verbose = core_config.is_true("VERBOSE")

        # Variables del FD
        self._wd = wd
        self._defaultwd = DIR_UPLOADS
        self._lastExecutionExtractedFilelist = []

    def delete_last_extracted_files(self):
        """
        Elimina los archivos presentes en la última ejecución del programa.

        :return: void
        :rtype: None
        """
        for i in self._lastExecutionExtractedFilelist:
            shutil.rmtree(i, True)
        self._lastExecutionExtractedFilelist = []

    def disable_auto_extract(self):
        """
        Desactiva el extraer automáticamente un archivo comprimido.

        :return: void
        :rtype: None
        """
        self._autoExtract = False

    def disable_do_remove_extracted_folders(self):
        """
        Desactiva el borrar las carpetas extraídas tras el análisis.

        :return: void
        :rtype: None
        """
        self._doRemoveExtractedFolders = False

    def disable_extract_if_folder_already_exists(self):
        """
        Desactiva el extraer un archivo comprimido si es que este ya se encuentra en la carpeta padre.

        :return: void
        :rtype: None
        """
        self._extractIfFolderAlreadyExists = False

    def disable_remove_on_extract(self):
        """
        Desactiva el borrar un archivo comprimido tras extraerlo.

        :return: void
        :rtype: None
        """
        self._removeOnExtract = False

    def disable_restrict_characters(self):
        """
        Desactiva el restringir los caracteres inválidos definidos en el parámetro de configuración VALID_CHARACTERS
        dentro de config/packages.ini.

        :return: void
        :rtype: None
        """
        self._doCharactersRestricted = False

    def disable_structure_characters(self):
        """
        Desactiva los caracteres de la estructura como válidos, VALID_STRUCTURE_CHARACTERS reemplaza a VALID_CHARACTERS.

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

    def enable_auto_extract(self):
        """
        Activa el extraer automáticamente un archivo comprimido.

        :return: void
        :rtype: None
        """
        self._autoExtract = True

    def enable_extract_if_folder_already_exists(self):
        """
        Activa el extraer un archivo comprimido si es que este ya se encuentra en la carpeta padre.

        :return: void
        :rtype: None
        """
        self._extractIfFolderAlreadyExists = True

    def enable_do_remove_extracted_folders(self):
        """
        Activa el borrar las carpetas extraídas tras el análisis.

        :return: void
        :rtype: None
        """
        self._doRemoveExtractedFolders = True

    def enable_remove_on_extract(self):
        """
        Activa el borrar un archivo comprimido tras extraerlo.

        :return: void
        :rtype: None
        """
        self._removeOnExtract = True

    def enable_restrict_characters(self):
        """
        Activa el restringir los caracteres inválidos definidos en el parámetro de configuración VALID_CHARACTERS dentro
        de config/packages.ini.

        :return: void
        :rtype: None
        """
        self._doCharactersRestricted = True

    def enable_structure_characters(self):
        """
        Activa los caracteres de la estructura como válidos, VALID_STRUCTURE_CHARACTERS reemplaza a VALID_CHARACTERS.

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

    def get_files_in_wd(self):
        """
        Retorna una lista con todos los archivos dentro del WD.

        :return: Lista con nombres de archivos.
        :rtype: list
        """
        return os.listdir(self._wd.decode(self._fileEncoding))

    def _get_valid_regex_chars(self):
        """
        Retorna el string de los caracteres válidos para el regex.

        :return: String con caracteres válidos
        :rtype: str
        """
        return str(self._validRegexChars)

    def get_working_directory(self):
        """
        Retorna el directorio root de los archivos.

        :return: Dirección del directorio root (padre)
        :rtype: str
        """
        return self._wd

    def _inspect_files(self, d_rootpath, foldername, l_filelist=None):
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
        folders_extracted_on_process = []  # Carpetas extraídas @UnusedVariable

        # noinspection SpellCheckingInspection
        def is_valid_file(filnm):
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
            return not is_hidden_file_utils(str(filnm))

        # noinspection SpellCheckingInspection
        def is_valid_folder_name(filnm):
            """
            Verifica si un nombre de una carpeta es válido (caracteres).

            :param filnm: String del nombre de la carpeta
            :type filnm: str

            :return: Booleano indicando validez
            :rtype: bool
            """
            # Si los caracteres son restrictivos
            if self._doCharactersRestricted:
                for c in filnm:
                    if c not in self._validChars:
                        return False
            return True

        # noinspection SpellCheckingInspection
        def is_valid_file_name(filnm):
            """
            Verifica si un nombre de un archivo es válido (caracteres).

            :param filnm: String del nombre del archivo
            :type filnm: str

            :return: Booleano indicando validez
            :rtype: bool
            """
            # Si los caracteres son restrictivos
            if self._doCharactersRestricted:
                for c in filnm:
                    if c not in self._validChars:
                        return False
            # Si requiere . en un archivo
            if self._needDotOnFile:
                return "." in filnm
            return True

        # noinspection PyBroadException
        def _inspect(rootpath, filename, filelist, extracted_folders, depth):
            """
            Inspecciona todos los archivos de un paquete.

            :param rootpath: Carpeta contenedora
            :type rootpath: str
            :param filename: Nombre del archivo a analizar
            :type filename: str, unicode
            :param filelist: Lista de archivos actuales a agregar
            :type filelist: list
            :param extracted_folders: Lista de carpetas extraídas durante el proceso
            :type extracted_folders: list
            :param depth: Profundidad de búsqueda
            :type depth: int

            :return: void
            :rtype: None
            """
            if not is_valid_file(filename):  # Si el archivo no es válido
                return

            if self._is_folder(rootpath, filename) and is_valid_folder_name(filename):  # Si el archivo es una carpeta
                path_to_inspect = rootpath + filename
                for filef in os.listdir(path_to_inspect.decode(self._fileEncoding)):
                    _inspect(rootpath + filename + "/", filef, filelist, extracted_folders, depth + 1)

            elif self._is_zip(rootpath, filename) and self._autoExtract:  # Si el archivo es paquete zip
                newfilename = filename.replace(".zip", "").replace(".ZIP", "")
                file_already_exists = False
                do_extract = True
                try:
                    file_already_exists = newfilename in os.listdir(rootpath.decode(self._fileEncoding))
                except:
                    pass
                if file_already_exists:
                    do_extract = do_extract and self._extractIfFolderAlreadyExists
                    if self._verbose:
                        if do_extract:
                            print _FILEMANAGER_Y_EXTRACT_COMPRSD_FILE.format(newfilename)
                        else:
                            print _FILEMANAGER_NO_EXTRACT_COMPRSD_FILE.format(newfilename)
                if do_extract:
                    zipfile.ZipFile(rootpath + filename).extractall(rootpath + newfilename + "/")
                    if self._removeOnExtract:
                        os.remove(rootpath + filename)
                    extracted_folders.append(rootpath + newfilename + "/")
                    if is_valid_folder_name(newfilename):
                        _inspect(rootpath, newfilename, filelist, extracted_folders, depth + 1)

            elif self._is_rar(rootpath, filename) and self._autoExtract:  # Si el archivo es paquete rar
                newfilename = filename.replace(".rar", "").replace(".RAR", "")
                file_already_exists = False
                do_extract = True
                try:
                    file_already_exists = newfilename in os.listdir(rootpath.decode(self._fileEncoding))
                except:
                    pass
                if file_already_exists:
                    do_extract = do_extract and self._extractIfFolderAlreadyExists
                    if self._verbose:
                        if do_extract:
                            print _FILEMANAGER_Y_EXTRACT_COMPRSD_FILE.format(newfilename)
                        else:
                            print _FILEMANAGER_NO_EXTRACT_COMPRSD_FILE.format(newfilename)
                if do_extract:
                    # Si el sistema operativo huésped es Windows
                    if is_windows():
                        try:
                            # noinspection PyArgumentEqualDefault
                            rarfile.RarFile(rootpath + filename, 'r', 'utf8').extractall(rootpath + newfilename + "/")
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
                            # noinspection PyArgumentEqualDefault
                            rarfile.RarFile(rootpath + filename, 'r', 'utf8').extractall(rootpath + newfilename + "/")
                        except Exception, ex:
                            print ""
                            err.st_error(err.ERROR_RARUNCOMPRESS_LINUX, True, "rarfile", ex)
                    if self._removeOnExtract:
                        os.remove(rootpath + filename)
                    extracted_folders.append(rootpath + newfilename + "/")
                    if is_valid_folder_name(newfilename):
                        _inspect(rootpath, newfilename, filelist, extracted_folders, depth + 1)

            else:  # Si es cualquier otro archivo entonces se añade
                if is_valid_file_name(filename):
                    if filename in os.listdir(rootpath.decode(self._fileEncoding)):
                        newfilename = rootpath + filename
                        if newfilename not in filelist:  # Evitar archivos duplicados
                            filelist.append(newfilename)

        def _remove_extracted_folders():
            """
            Función que elimina las carpetas extraídas durante el proceso de análisis.

            :return: void
            :rtype: None
            """
            self._lastExecutionExtractedFilelist = []
            append_list_to_list(self._lastExecutionExtractedFilelist, folders_extracted_on_process)
            if self._doRemoveExtractedFolders:
                self.delete_last_extracted_files()

        def _append_if_empty(l, f, r):
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
                if f in os.listdir(r.decode(self._fileEncoding)) and is_valid_file(f):
                    l.append(f)

        if l_filelist is not None:
            _inspect(d_rootpath, foldername, l_filelist, folders_extracted_on_process, 0)
            for i in range(len(l_filelist)):
                l_filelist[i] = l_filelist[i].replace("//", "/").replace(d_rootpath, "")
            _remove_extracted_folders()
            _append_if_empty(l_filelist, foldername, d_rootpath)
        else:
            l_filelist = []
            _inspect(d_rootpath, foldername, l_filelist, folders_extracted_on_process, 0)
            for i in range(len(l_filelist)):
                l_filelist[i] = l_filelist[i].replace("//", "/").replace(d_rootpath, "")
            _remove_extracted_folders()
            _append_if_empty(l_filelist, foldername, d_rootpath)
            return l_filelist

    def inspect_single_file(self, filename):
        """
        Inspecciona los elementos de un solo archivo o carpeta.

        :param filename: Nombre del archivo a inspeccionar
        :type filename: str, unicode

        :return: Lista de archivos que contiene la carpeta
        :rtype: list
        """
        return self._inspect_files(self._wd, filename)

    # noinspection PyMethodMayBeStatic
    def _is_folder(self, rootpath, filename):
        """
        Comprueba si un nombre de carpeta es un directorio en el sistema huésped.

        :param rootpath: Ubicación del archivo
        :type rootpath: str
        :param filename: Nombre del archivo
        :type filename: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        return is_folder_utils(rootpath, filename)

    # noinspection PyMethodMayBeStatic,PyBroadException
    def _is_rar(self, rootpath, filename):
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
                # noinspection PyArgumentEqualDefault
                rarfile.RarFile(rootpath + filename, 'r', "utf8")
                # Archive(rootpath + filename) para linux
                return True
            except:
                return False
        return False

    # noinspection PyMethodMayBeStatic,PyBroadException
    def _is_zip(self, rootpath, filename):
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

    def _print_file_list(self, fl, filename):
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
            print "Archivos de " + self.get_working_directory() + filename
            if len(fl) > 0:
                for i in range(0, len(fl)):
                    print "\t", fl[i]
            else:
                print "\t", err.ERROR_NOFILES

    def _print_files_in_wd(self):
        """
        Imprime los archivos que están dentro del working directory.

        :return: void
        :rtype: None
        """
        for f in os.listdir(self._wd.decode(self._fileEncoding)):  # @ReservedAssignment
            print f

    def _print_single_file(self, filename):
        """
        Imprime los archivos dentro de una sola carpeta.

        :param filename: Nombre del archivo a analizar
        :type filename: str, unicode

        :return: void
        :rtype: None
        """
        print self._print_file_list(self.inspect_single_file(filename), filename)

    def _print_tree(self):
        """
        Imprime los archivos de cada una de las carpetas del working directory.

        :return: void
        :rtype: None
        """
        for f in os.listdir(self._wd.decode(self._fileEncoding)):  # @ReservedAssignment
            if f is not None:
                self._print_single_file(f)

    def restore_wd(self):
        """
        Retorna el wd al estado por defecto.

        :return: void
        :rtype: None
        """
        self.set_working_directory(self._defaultwd)

    def set_default_working_directory(self, new_wd):
        """
        Establece el directorio root por defecto del working directory.

        :param new_wd: Ubicación del nuevo working directory por defecto
        :type new_wd: str

        :return: void
        :rtype: None
        """
        if self._is_folder(new_wd, "") and len(new_wd) > 0:
            new_wd = new_wd.replace("\\", "/").replace("//", "/")
            if new_wd[len(new_wd) - 1] != "/":
                new_wd += "/"
            self._defaultwd = new_wd
        else:
            err.throw(err.ERROR_BADWD)

    def _set_file_encoding(self, enc):
        """
        Establece la codificación de los nombres de los archivos.

        :param enc: Codificación de cada uno de los nombres de los archivos
        :type enc: str, unicode

        :return: void
        :rtype: None
        """
        self._fileEncoding = enc

    def set_working_directory(self, new_wd):
        """
        Establece el directorio root del working directory.

        :param new_wd: Ubicación del nuevo working directory
        :type new_wd: str

        :return: void
        :rtype: None
        """
        if self._is_folder(new_wd, "") and len(new_wd) > 0:
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
                treelist.append(self.inspect_single_file(f))
        return treelist
