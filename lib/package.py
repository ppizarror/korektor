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

# Importación de librerías
if __name__ == '__main__':
    from libpath import *  # @UnusedWildImport
# noinspection PyUnresolvedReferences
from bin.errors import *  # @UnusedWildImport
from bin.utils import print_hierachy_list, number_of_sublists
from bin.vartype import *  # @UnusedWildImport
from lib.filemanager import FileManager

# Constantes del módulo
PACKAGE_DO_NOT_EXIST = "PACKAGE_DO_NOT_EXIST"
PACKAGE_EMPTY = "PACKAGE_EMPTY"
PACKAGE_FILE_INVALID_DEPTH = -1
PACKAGE_FILE_NOT_FOUND = "PACKAGE_FILE_NOT_FOUND"
PACKAGE_NO_NAME = "PACKAGE_NO_NAME"


class Package(VarTypedClass, ExceptionBehaviour):
    """
    Clase paquete, maneja funciones que permiten manejar listas con archivos del estilo z:/a/b/...
    con funciones auxiliares que buscan archivos, direcciones, profundidad, etc.
    """

    def __init__(self, files, generate_hierarchy=False):
        """
        Constructor de la clase.

        :param files: Lista de archivos generada por un FileManager
        :type files: list
        :param generate_hierarchy: Generar Jerarquía automáticamente
        :type generate_hierarchy: bool

        :return: void
        :rtype: None
        """
        # Se instancian los super
        ExceptionBehaviour.__init__(self)
        VarTypedClass.__init__(self)

        # Se chequean los tipos de variable
        self._check_variable_type(files, TYPE_LIST, "Package.__init()__.files")
        self._check_variable_type(generate_hierarchy, TYPE_BOOL, "Package.__init()__.generate_hierarchy")

        # Variables de clase
        self._hierarchyFiles = []
        self._packageFiles = []
        self._packageName = ""
        self._rawfiles = files

        # Variables de estado
        self._isGeneratedName = False
        self._isgeneratedHierarchyFiles = False
        self._isGeneratedPackageFiles = False

        # Variables de validación
        self._isValid = False
        self._notvalidFiles = []
        self._notValidHierarchyFiles = []
        self._validFiles = []
        self._validHierarchyFiles = []
        self._validated = False
        self._validatedFiles = []  # 0: Ubicación real, 1: Nombre en structure, 3: Nombre nuevo de la ruta, 4: Nombre del archivo
        self._validatedFilesHierarchyCreated = False

        # Se crea el paquete
        self._generate_package_name(files)
        self._generate_package_files(files)
        if generate_hierarchy:
            self.generate_hierarchy()

    def check_if_exist(self, f):
        """
        Comprueba si un archivo o carpeta existe en el paquete.

        :param f: Nombre del elemento a buscar
        :type f: str

        :return: Booleano indicando pertenencia o no
        :rtype: bool
        """
        return self.is_file(f) or self.is_folder(f)

    def find_file_location(self, f):
        """
        Busca la ubicación de un archivo o carpeta en el paquete.

        :param f: Nombre del archivo o carpeta a buscar
        :type f: str

        :return: Ubicación del archivo o carpeta si es que se encuentra
        :rtype: str
        """
        file_results = self._is_file(f)
        if file_results[0]:
            return file_results[1]
        else:
            folder_results = self._is_folder(f)
            if folder_results[0]:
                return folder_results[1]
        return PACKAGE_FILE_NOT_FOUND

    def get_file_depth(self, f):
        """
        Obtiene la profundidad de un archivo o carpeta en el paquete.

        :param f: Nombre del archivo o carpeta a buscar
        :type f: str

        :return: Profundidad del archivo o carpeta, si es que se encuentra
        :rtype: int
        """
        file_results = self._is_file(f)
        if file_results[0]:
            return file_results[2]
        else:
            folder_results = self._is_folder(f)
            if folder_results[0]:
                return folder_results[2]
        return PACKAGE_FILE_INVALID_DEPTH

    def generate_hierarchy(self):
        """
        Crea la lista de jerarquía para el paquete.

        :return: void
        :rtype: None
        """
        if self._isGeneratedPackageFiles:
            self._generate_hierarchy_from_file_list(self._packageFiles, self._packageName, self._hierarchyFiles)
            self._isgeneratedHierarchyFiles = True
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    @staticmethod
    def _generate_hierarchy_from_file_list(package_files, package_name, hierarchy_file_list):
        """
        Crea una lista de jerarquía a partir de una lista de nombres de archivos.

        :param package_files: Lista de archivos a revisar
        :type package_files: list
        :param package_name: Nombre del paquete
        :type package_name: str, unicode
        :param hierarchy_file_list: Lista de jerarquía nueva
        :type hierarchy_file_list: list

        :return: void
        :rtype: None
        """
        hierarchy_file_list.append(package_name)
        for i in package_files:
            if "/" not in i:
                hierarchy_file_list.append(i)
            else:
                # Se añaden las carpetas
                j = i.split("/")
                sublvl = hierarchy_file_list
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

    def _generate_package_files(self, filelist):
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
            return self._throw_exception("PACKAGE_ERROR_NO_NAME")

    def _generate_package_name(self, filelist):
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

    def get_file_list(self):
        """
        Retorna una lista con los nombres de los archivos.

        :return: Lista de archivos
        :rtype: list
        """
        if self._isGeneratedPackageFiles:
            return self._packageFiles
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    def get_hierarchy_files(self):
        """
        Retorna la lista de jerarquía del paquete

        :return: Lista de jerarquía de archivos
        :rtype: list
        """
        if self._isgeneratedHierarchyFiles:
            return self._hierarchyFiles
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_CREATED")

    def _get_external_hierarchy_files(self, external_package_files, external_package_name):
        """
        Retorna la jerarquía de archivos utilizando una lista de archivos y nombre de paquete externos.

        :param external_package_files: Lista de archivos externa a crear una jerarquía.
        :type external_package_files: list
        :param external_package_name: Nombre del paquete externo.
        :type external_package_name: str, unicode

        :return: Lista de jerarquía
        :rtype: list
        """
        hierarchy_list = []
        self._generate_hierarchy_from_file_list(external_package_files, external_package_name, hierarchy_list)
        return hierarchy_list

    def get_number_of_elements(self):
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
            return self._throw_exception("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    def get_number_of_subfolders(self):
        """
        Retorna el número sub-carpetas que tiene un paquete.

        :return: Número de sub-carpetas
        :rtype: int
        """
        if self._isgeneratedHierarchyFiles:
            return number_of_sublists(self._hierarchyFiles)
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_CREATED")

    def get_package_name(self):
        """
        Retorna el nombre del paquete.

        :return: Nombre del paquete
        :rtype: str
        """
        if self._isGeneratedName:
            return self._packageName
        else:
            return self._throw_exception("PACKAGE_ERROR_NO_NAME")

    def get_validated_files(self):
        """
        Retorna la lista de los archivos validados.

        :return: Lista de archivos
        :rtype: list
        """
        if self._validated:
            return self._validatedFiles
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_VALIDATED_YET")

    def _is_file(self, fl):
        """
        Retorna un vector de valores indicando si el nombre mencionado corresponde o no a un archivo.

        :param fl: Nombre del archivo
        :type fl: str

        :return: Lista de valores indicando si existe, la ubicación y la profundidad
        :rtype: list
        """

        def recursive_search_file(l, f, d, s):
            """
            Función auxiliar que busca un fichero f en una lista cualquiera l de forma recursiva.

            :param l: Lista a buscar
            :type l: list
            :param f: Archivo a buscar
            :type f: str
            :param d: Profundidad actual de búsqueda
            :type d: int
            :param s: String de la posición de cada archivo
            :type s: str

            :return: Retorna un vector de valores
            :rtype: list
            """
            for i in l:
                if isinstance(i, list):
                    r = len(i)
                    if r > 1:
                        k = recursive_search_file(i[1:r], f, d + 1, s + "/" + i[0])
                        if k is not None and k[0]:
                            return k
                else:
                    if str(i) == f:  # Comprobación final
                        return [True, s + "/" + i, d]
            return [False, PACKAGE_FILE_NOT_FOUND, PACKAGE_FILE_INVALID_DEPTH]

        if self._isgeneratedHierarchyFiles:
            return recursive_search_file(self._hierarchyFiles, fl, 0, "")
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_CREATED")

    def is_file(self, f):
        """
        Retorna un booleano indicando si el nombre mencionado corresponde o no a un archivo.

        :param f: Nombre del archivo
        :type f: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        if self._isgeneratedHierarchyFiles:
            self._check_variable_type(f, TYPE_STR, "f")
            if len(f) > 0:
                return self._is_file(f)[0]
            else:
                return False
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_CREATED")

    def _is_folder(self, fl):
        """
        Retorna un vector de valores indicando si el nombre mencionado corresponde o no a una carpeta.

        :param fl: Nombre del archivo a buscar
        :type fl: str

        :return: Lista de valores indicando si existe, la ubicación y la profundidad
        :rtype: list
        """

        def recursive_search_folder(l, f, d, s):
            """
            Función auxiliar que busca una carpeta f en una lista cualquiera l de forma recursiva.

            :param l: Lista a buscar
            :type l: list
            :param f: Archivo a buscar
            :type f: str
            :param d: Profundidad actual de búsqueda
            :type d: int
            :param s: Posición de cada archivo en un string
            :type s: str

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
                            k = recursive_search_folder(i, f, d + 1, s + "/" + i[0])
                            if k is not None and k[0]:
                                return k
                else:
                    if i == f and j == 0:  # Comprobación final
                        return [True, s + "/" + i + "/", d]
                j += 1
            if d == 0:
                return [False, PACKAGE_FILE_NOT_FOUND, PACKAGE_FILE_INVALID_DEPTH]

        if self._isgeneratedHierarchyFiles:
            return recursive_search_folder(self._hierarchyFiles, fl, 0, "")
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_CREATED")

    def is_folder(self, f):
        """
        Retorna un booleano indicando si el nombre mencionado corresponde o no a una carpeta.

        :param f: Nombre del archivo a buscar
        :type f: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        if self._isgeneratedHierarchyFiles:
            self._check_variable_type(f, TYPE_STR, "f")
            if len(f) > 0:
                return self._is_folder(f)[0]
            else:
                return False
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_CREATED")

    def is_valid(self):
        """
        Retorna true/false indicando si el paquete es válido o no.

        :return: Booleano indicando validación.
        :rtype: bool
        """
        return self._isValid

    def is_validated(self):
        """
        Retorna true/false indicando si el paquete está validado o no.

        :return: Booleano indicando si el paquete actual está validado o no
        :rtype: bool
        """
        return self._validated

    def _mark_as_valid(self):
        """
        Indica que la estructura del paquete es válida.
        Sólo puede hacerse a través de un validador.

        :return: void
        :rtype: None
        """
        self._isValid = True

    def _mark_as_validated(self):
        """
        Indica que el paquete ya ha sido revisado por el validador.
        Sólo puede hacerse a través de un validador.

        :return: void
        :rtype: None
        """
        self._validated = True

    def _print_file_list(self):
        """
        Imprime en consola la lista de archivos del paquete.

        :return: void
        :rtype: None
        """
        if self._isGeneratedPackageFiles:
            for pfle in self._packageFiles:
                print pfle
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_INDEXED_FILES_YET")

    def _print_hierarchy(self, tabs_left=0):
        """
        Imprime en consola la lista de archivos en forma de jerarquía.

        :param tabs_left: Número de tabs a la izquierda de los mensajes
        :type tabs_left: int

        :return: void
        :rtype: None
        """
        if self._isgeneratedHierarchyFiles:
            if len(self._packageFiles) == 0:
                print PACKAGE_FILE_NOT_FOUND
            elif self.get_number_of_elements() == 0:
                print PACKAGE_EMPTY
            else:
                print_hierachy_list(self._hierarchyFiles, 0, tabs_left)
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_CREATED")

    def _print_not_valid_hierachy_list(self, tabs_left=0):
        """
        Imprime en consola la jerarquía de los archivos no válidos del paquete.

        :param tabs_left: Número de tabs a la izquierda de los mensajes
        :type tabs_left: int

        :return: void
        :rtype: None
        """
        if self._validated:
            if self._validatedFilesHierarchyCreated:
                if len(self._notValidHierarchyFiles) > 0:
                    print_hierachy_list(self._notValidHierarchyFiles, 0, tabs_left)
            else:
                return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_INVALID_CREATED")
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_VALIDATED_YET")

    def _print_raw_files(self):
        """
        Imprime en consola la lista de archivos sin tratar del paquete.

        :return: void
        :rtype: None
        """
        print self._rawfiles

    def _print_valid_hierachy_list(self, tabs_left=0):
        """
        Imprime en consola la jerarquía de los archivos válidos del paquete.

        :param tabs_left: Número de tabs a la izquierda de los mensajes
        :type tabs_left: int

        :return: void
        :rtype: None
        """
        if self._validated:
            if self._validatedFilesHierarchyCreated:
                if len(self._validHierarchyFiles) > 0:
                    print_hierachy_list(self._validHierarchyFiles, 0, tabs_left)
            else:
                return self._throw_exception("PACKAGE_ERROR_NOT_HIERARCHY_VALID_CREATED")
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_VALIDATED_YET")

    def _print_validated_filelist(self):
        """
        Imprime en consola la lista de archivos validados del paquete.

        :return: void
        :rtype: None
        """
        if self._validated:
            for vpfle in self._validatedFiles:
                print vpfle
        else:
            return self._throw_exception("PACKAGE_ERROR_NOT_VALIDATED_YET")

    # noinspection SpellCheckingInspection
    def _set_validated_files(self, vfiles, generate_hierarchies):
        """
        Define los archivos válidos, y crea la lista de archivos no válidos del paquete.

        :param vfiles: Lista con archivos válidos.
        :type vfiles: list
        :param generate_hierarchies: Indica si crear la jerarquía de los archivos válidos e inválidos
        :type generate_hierarchies: bool

        :return: void
        :rtype: None
        """
        # Se almacenan los archivos validados
        self._check_variable_type(vfiles, TYPE_LIST, "Package._set_validated_files.vfiles")
        self._validatedFiles = vfiles

        # Se genera la lista de archivos válidos e inválidos
        for indx in range(0, len(vfiles)):
            self._validFiles.append(vfiles[indx][0])
        for pfile in self._packageFiles:
            if pfile not in self._validFiles:
                self._notvalidFiles.append(pfile)

        # Se genera la jerarquía de los archivos válidos e inválidos
        if generate_hierarchies:
            self._validHierarchyFiles = self._get_external_hierarchy_files(self._validFiles, self._packageName)
            self._notValidHierarchyFiles = self._get_external_hierarchy_files(self._notvalidFiles, self._packageName)
            self._validatedFilesHierarchyCreated = True


# Clase paquete que utiliza un filemanager
class PackageFileManager(Package):
    """
    Clase paquete. Exactamente la misma que Package salvo que utiliza un filemanager externo
    y un string indicando el nombre del archivo a analizar
    """

    def __init__(self, file_manager, package_name, generate_hierarchy=False):
        """
        Constructor de la clase.

        :param file_manager: Filemanager a utilizar
        :type file_manager: FileManager
        :param package_name: Nombre del paquete a analizar
        :type package_name: str
        :param generate_hierarchy: Generar Jerarquía automáticamente
        :type generate_hierarchy: bool

        :return: void
        :rtype: None
        """
        # Comprobación de tipos
        self._check_variable_type(file_manager, TYPE_OTHER, "PackageFileManager.__init()__.file_manager", FileManager)
        self._check_variable_type(package_name, TYPE_STR, "PackageFileManager.__init()__.package_name")

        # Se guarda el FileManager
        self._filemanager = file_manager

        # Se crea un paquete normal
        Package.__init__(self, file_manager.inspect_single_file(package_name), generate_hierarchy)

    def _delete_last_extracted_files(self):
        """
        Se eliminan los archivos resultantes de la última extracción por el fileManager.

        :return: void
        :rtype: None
        """
        self._filemanager.delete_last_extracted_files()
