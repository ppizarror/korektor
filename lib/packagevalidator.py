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
from bin.configloader import configLoader  # @UnresolvedImport
from bin.utils import isFolder, printHierachyBoolList, regexCompare  # @UnusedImport
from config import DIR_CONFIG  # @UnresolvedImport
# noinspection PyUnresolvedReferences
from data import DIR_DATA, DIR_STRUCTURE_FOLDERNAME  # @UnusedImport
from lib.package import *  # @UnusedWildImport
import copy

# Constantes
_VL_CHECK = 0  # No cambiar
_VL_INDEX = 1  # No cambiar
_VL_IS_SUBFOLDER = 2  # No cambiar
_VL_NOT = 10
_VL_TRUE = 11
_VL_TRUE_CHECKED = 12


class PackageValidator(varTypedClass, exceptionBehaviour):
    """
    Clase que permite validar que los paquetes tengan una estructura adecuada, para ello se instancia
    un paquete con la estructura pedida (en regex) y la función validatePackage comprueba que un
    paquete pasado por argumento.
    """

    def __init__(self):
        """
        Constructor de la clase.

        :return: void
        :rtype: None
        """
        # Se instancian los super
        exceptionBehaviour.__init__(self)
        varTypedClass.__init__(self)

        # Carga de configuraciones
        coreConfig = configLoader(DIR_CONFIG, "core.ini")
        validatorConfig = configLoader(DIR_CONFIG, "validator.ini")
        self._doCheckStructureInSubfolder = validatorConfig.isFalse("STRICT_MODE_PACKAGES")
        self._doRegexCaseInsensitive = validatorConfig.isTrue("CASE_INSENSITIVE")
        self._verbose = coreConfig.isTrue("VERBOSE")

        # Variables de estado
        self._isStructGenerated = False
        self._isValidStructureDirectories = True

        # Variables de la estructura
        self._structureBoolHierarchy = [False]
        self._structureBoolHierarchy2 = [False]
        self._structureDirectoryName = DIR_STRUCTURE_FOLDERNAME
        self._structureDirectoryRoot = DIR_DATA
        self._structurePackage = Package([])

        # Instancia un filemanager para generar la estructura
        self._fm = FileManager()
        self._fm.setDefaultWorkingDirectory(self._structureDirectoryRoot)
        self._fm.restoreWD()
        self._fm.enable_autoExtract()
        self._fm.enable_doRemoveExtractedFolders()
        self._fm.disable_removeOnExtract()
        self._fm.enable_restrictCharacters()
        self._fm.enable_structureCharacters()
        if self._verbose:
            self._fm.enable_verbose()
        else:
            self._fm.disable_verbose()

        # Variables de verificación
        self._validRegexChars = self._fm._getValidRegexChars()

    @staticmethod
    def _checkHierarchyTree(boolList):
        """
        Chequea el estado de la lista de booleanos para la jerarquía de la estructura, completa con valores true si es
        que se cumplen condiciones.

        :param boolList: Lista de booleanos a analizar y modificar
        :type boolList: list

        :return: Booleano indicando si la jerarquía es válida o no.
        :rtype: bool
        """

        def _checkSubElementBoolHierarchy(l):
            """
            Chequea los subelementos en la lista de booleanos de forma recursiva.

            :param l: Sub-lista recursiva
            :type l: list

            :return: Booleano indicando si toda la sub-lista es True
            :rtype: bool
            """
            for k in range(1, len(l)):
                if isinstance(l[k], list) and not _checkSubElementBoolHierarchy(l[k]):
                    l[0] = False
                    return False
                else:
                    if not l[k]:
                        l[0] = False
                        return False
            l[0] = True
            return True

        _checkSubElementBoolHierarchy(boolList)
        return boolList[0]

    def _createBoolHierarchyTree(self):
        """
        Función auxiliar que retorna una lista de booleanos para el hierarchy de la estructura.

        :return: Lista de booleanos en false para cada archivo
        :rtype: list
        """

        def _recursiveBoolHierarchy(l, h):
            """
            Función recursiva que comprueba el estado de lista y agrega un booleano False.

            :param l: Sección de la jerarquía de estructura a analizar
            :type l: list
            :param h: Sección de la lista de jerarquía a ser agregada
            :rtype h: list

            :return: void
            :rtype: None
            """
            k = 0
            for element in l:
                if isinstance(element, list):
                    s = []
                    _recursiveBoolHierarchy(l[k], s)
                    h.append(s)
                else:
                    h.append(False)
                k += 1

        # Si fue generada la estructura
        if self._isStructGenerated:
            boolHierarchy = []  # Lista a crear
            _recursiveBoolHierarchy(self._getStructurePackage().getHierarchyFiles(), boolHierarchy)
            return boolHierarchy
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_NOT_CREATED")

    def disable_case_sensitive(self):
        """
        Desactiva el comparar los nombres de los archivos sin importar el tipo de letra (mayúscula, minúscula).

        :return: void
        :rtype: None
        """
        self._doRegexCaseInsensitive = False

    def disable_check_structure_on_subfolder(self):
        """
        Desactiva el buscar la estructura en cada subcarpeta si estas no pertenecen a la estructura en primera instancia.

        :return: void
        :rtype: None
        """
        self._doCheckStructureInSubfolder = False

    def disable_verbose(self):
        """
        Desactiva el printing de errores y estados de sistema.

        :return: void
        :rtype: None
        """
        self._verbose = False
        self._fm.enable_verbose()

    def enable_case_sensitive(self):
        """
        Activa el comparar los nombres de los archivos sin importar el tipo de letra (mayúscula, minúscula).

        :return: void
        :rtype: None
        """
        self._doRegexCaseInsensitive = True

    def enable_check_structure_on_subfolder(self):
        """
        Activa el buscar la estructura en cada subcarpeta si estas no pertenecen a la estructura en primera instancia.

        :return: void
        :rtype: None
        """
        self._doCheckStructureInSubfolder = True

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
        Carga la configuración de la estructura requerida para cada tarea a partir del directorio de la estructura
        especificado, para cambiarlo utilice setStructureDirectory(path_to_directory).

        :return: void
        :rtype: None
        """
        if self._isValidStructureDirectories:
            self._structurePackage = PackageFileManager(self._fm, self._structureDirectoryName, True)
            self._isStructGenerated = True
            self._structureBoolHierarchy = self._createBoolHierarchyTree()
            self._structureBoolHierarchy2 = self._createBoolHierarchyTree()
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_FOLDER_DONT_EXIST")

    def _printBooleanHierachy(self, boolHierarchy):
        """
        Imprime la lista de jerarquía booleana pasada por argumento en forma de jerarquía.

        :param boolHierarchy: list
        :type boolHierarchy: list

        :return: void
        :rtype: None
        """
        self._checkVariableType(boolHierarchy, TYPE_LIST, "PackageValidator._printBooleanHierarchy.boolHierarchy")
        printHierachyBoolList(boolHierarchy, 0)

    def _printStructureHierachy(self):
        """
        Imprime la lista de los archivos de la estructura válida en forma de jerarquía.

        :return: void
        :rtype: None
        """
        if self._isStructGenerated:
            self._structurePackage._printHierarchy()
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_NOT_CREATED")

    def setStructureDirectory(self, structureDir, doLoad=True):
        """
        Define el directorio de la estructura.

        :param structureDir: Nuevo directorio para cargar la estructura
        :type structureDir: str
        :param doLoad: Carga inmediatamente la estructura
        :type doLoad: bool

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
            if doLoad:
                self.loadStructure()
        else:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_FOLDER_DONT_EXIST")

    def validatePackage(self, package, generate_hierarchies=False):
        """
        Valida un paquete, comprobando que todos los archivos del mismo cumplan con la estructura
        cargada.

        :param package: Paquete a comprobar
        :type package: Package
        :param generate_hierarchies: Indica si generar la jerarquía de los archivos válidos e inválidos de los paquetes.
        :type generate_hierarchies: bool

        :return: void
        :rtype: None
        """
        _validatedFilesPackage = []

        # noinspection PyUnusedLocal
        def _checkF(h, hi, s, ls, boolList, lboolList, checkFdepth):
            # noinspection SpellCheckingInspection
            """
            Chequea si un nombre de archivo dentro de h[hi] pertenece a la estructura en s[si] a la misma profundidad,
            si existe entonces lo marca en la jerarquía booleana b[bi].

            Esta función retorna lo siguiente: [TYPE, POSITION, NO_SUBFOLDER]

            - TYPE: Indica tipo de inclusión, _VL_NOT, _VL_TRUE y _VL_TRUE_CHECKED.
            - POSITION: Retorna la posición del elemento en el paquete estructural en donde se encontró el archivo.
            - SUBFOLDER: Retorna true/false si el elemento de la estructura en b[bi] contiene subcarpetas o no.

            :param h: Sublista de jerarquía del paquete a analizar.
            :type h: list
            :param hi: Índice del elemento de la jerarquía del paquete a analizar.
            :type hi: int
            :param s: Sublista de la estructura a analizar.
            :type s: list
            :param ls: Largo de la sublista de la estructura
            :type ls: int
            :param boolList: Sublista de la jerarquía estructural booleana a analizar.
            :type boolList: list
            :param lboolList: Largo de la sublista de la jerarquía booleana
            :type lboolList: int
            :param checkFdepth: Profundidad de búsqueda
            :type checkFdepth: int

            :return: Lista de valores denotando tipo de pertenencia
            :rtype: list
            """
            # Se obtiene el key a buscar y su tipo
            element_ToCheck = h[hi]
            element_IsList = isinstance(element_ToCheck, list)

            # Lista a retornar, 0: Tipo de búsqueda, 1: Índice del elemento encontrado, 2: Si es una carpeta
            reslt = [_VL_NOT, -1, False]

            # Se recorre cada elemento de hs_r
            for hsk in range(0, ls):
                element_inStructure = s[hsk]  # Elemento en la estructura

                # Si el elemento es una lista y el key es una lista

                # Si el elemento en el paquete y en la estructura son listas
                if isinstance(element_inStructure, list) and element_IsList:

                    # Si los nombres de las carpetas son iguales
                    if regexCompare(element_inStructure[0], element_ToCheck[0], self._validRegexChars,
                                    case_insensitive=self._doRegexCaseInsensitive):

                        # Si el elemento ya fue chequeado entonces se ignora
                        if hsk < lboolList and boolList[hsk + 1][0]:
                            reslt[_VL_CHECK] = _VL_TRUE_CHECKED

                        # Si no fue chequeado entonces retorna true y menciona que es subcarpeta
                        else:
                            reslt[_VL_CHECK] = _VL_TRUE
                            reslt[_VL_IS_SUBFOLDER] = True

                        # Se retorna el resultado
                        reslt[_VL_INDEX] = hsk
                        return reslt

                # Si el elemento en el paquete y en la estructura son strings
                if not isinstance(element_inStructure, list) and not element_IsList:

                    # Si los nombres de los archivos son iguales
                    if regexCompare(element_inStructure, element_ToCheck, self._validRegexChars,
                                    case_insensitive=self._doRegexCaseInsensitive):

                        # Si el elemento ya fue chequeado
                        if hsk < lboolList and boolList[hsk + 1]:
                            reslt[_VL_CHECK] = _VL_TRUE_CHECKED

                        # El elemento no ha sido chequeado
                        else:
                            reslt[_VL_CHECK] = _VL_TRUE

                        # Se retorna el resultado
                        reslt[_VL_INDEX] = hsk + 1
                        return reslt

            return reslt

        def _verifyInclusionRecursive(hp_r, hs_r, hs_nr, b_r, b_r_i, b_nr, rootpathi, depth, typeCheck, hsrootpath,
                                      rootpathi_nrs):
            # noinspection SpellCheckingInspection
            """
            Función auxiliar principal que recorre cada uno de los archivos de un paquete (hp_r) verificando que se
            cumpla la estructura pedida (hs_r), si se cumple entonces se marca la lista de jerarquía booleana y retorna
            true cuando _checkHierarchyTree retorna True.

            :param hp_r: Lista de jerarquía del paquete recursiva.
            :type hp_r: list
            :param hs_r: Lista de jerarquía de la estructura recursiva.
            :type hs_r: list
            :param hs_nr: Lista de jerarquía no recursiva
            :type hs_nr: list
            :param b_r: Lista de jerarquía booleana recursiva.
            :type b_r: list
            :param b_r_i: Índice de búsqueda de la jerarquía booleana
            :type b_r_i: int
            :param b_nr: Lista de jerarquía booleana no recursiva.
            :type b_nr: list
            :param rootpathi: Indica la posición de un archivo absoluta.
            :type rootpathi: str, unicode
            :param depth: Profundidad de búsqueda
            :type depth: int
            :param typeCheck: Tipo de búsqueda de archivos, 0 si es clean, 1 si es continuado
            :type typeCheck: int
            :param hsrootpath: Indica la posición de un archivo de la estructura
            :type hsrootpath: str, unicode
            :param rootpathi_nrs: Indica la posición de un archivo sin repetir carpetas
            :type rootpathi_nrs: str

            :return: Booleano indicando si se debe seguir con la búsqueda o no.
            :rtype: bool
            """
            # Se obtiene la sub lista recursiva de la jerarquía booleana
            if b_r_i > 0:
                # print "{0}==> Se cargo el índice".format("\t" * depth), b_r_i, "de la estructura jerárquica booleana"
                b_r = b_r[b_r_i]

            # Se obtienen los largos de las listas
            lhp = len(hp_r)
            lhs = len(hs_r)
            lbr = len(b_r)

            # Se recorre cada archivo de la lista recursiva del paquete
            for packageFileIndex in range(0, lhp):

                # Se obtiene la información del check
                c = _checkF(hp_r, packageFileIndex, hs_r, lhs, b_r, lbr, depth)

                # print "{0}< Resultados del análisis".format("\t" * (depth + 1)), c

                # Si el archivo no existe
                if c[_VL_CHECK] == _VL_NOT:

                    if isinstance(hp_r[packageFileIndex], list) and self._doCheckStructureInSubfolder:

                        # print "{0}<< Se buscara el structure en las subcarpetas de la carpeta fallida".format("\t" * (depth + 1)), c

                        if typeCheck == 0:
                            nhpr = hp_r[packageFileIndex][1:len(hp_r[packageFileIndex])]
                            nrootpathname = rootpathi + str(hp_r[packageFileIndex][0]) + "/"
                        else:
                            nhpr = hp_r
                            nrootpathname = rootpathi
                            typeCheck = 2

                        # Se comprueba el resto de subcarpetas
                        if numberOfSublists(nhpr) >= numberOfSublists(hs_nr):
                            if _verifyInclusionRecursive(nhpr, hs_nr[1:len(hs_nr)], hs_nr, b_nr, 0, b_nr, nrootpathname,
                                                         depth + 1, typeCheck, "", ""):
                                return False

                # Si el archivo existe pero no ha sido chequeado aún
                elif c[_VL_CHECK] == _VL_TRUE:

                    # Si el archivo es una carpeta entonces se comprueba de forma recursiva
                    if c[_VL_IS_SUBFOLDER]:

                        # Se establece la información para crear un walk recursivo
                        vIndex = c[_VL_INDEX]
                        lpfi = len(hp_r[packageFileIndex])
                        lshr = len(hs_r[vIndex])
                        rootpath_in = rootpathi + str(hp_r[packageFileIndex][0]) + "/"
                        hsrootpath_in = hsrootpath + str(hs_r[vIndex][0]) + "/"
                        if typeCheck == 2:
                            rootpathi_nrs = hsrootpath
                        else:
                            rootpathi_nrs = hsrootpath + str(hp_r[packageFileIndex][0]) + "/"

                        # Se llama de forma recursiva a dicha carpeta
                        try:
                            # print "{0}\t > Se buscara la carpeta '".format("\t" * (depth + 1)), hp_r[packageFileIndex][1], "'"
                            if not _verifyInclusionRecursive(hp_r[packageFileIndex][1:lpfi], hs_r[vIndex][1:lshr],
                                                             hs_nr, b_r, vIndex + 1, b_nr, rootpath_in, depth + 1, 1,
                                                             hsrootpath_in, rootpathi_nrs):
                                return False
                        except:
                            return self._throwException("VALIDATOR_ERROR_ON_VALIDATE_WALK_RECURSIVE")

                    # Si no entonces se marca el archivo en la lista boolena y se comprueba que
                    else:
                        # print "{0}\t > El archivo '".format("\t" * (depth + 1)), hp_r[packageFileIndex], "' se marco como valido"

                        # Se comprueba que el índice sea menor que el largo del bool, si lo es se activa
                        if c[_VL_INDEX] < lbr:
                            b_r[c[_VL_INDEX]] = True
                            _validatedFilesPackage.append(
                                [rootpathi + hp_r[packageFileIndex], hsrootpath + hs_r[c[_VL_INDEX] - 1],
                                 rootpathi_nrs + hp_r[packageFileIndex], hp_r[packageFileIndex]])

                        # Si el puntero a la estructura jerárquica no es valido
                        else:
                            # print "ERROR GRAVE!"
                            return False

                        # Se comprueba la validez booleana
                        self._checkHierarchyTree(b_nr)

                        # Si la sub carpeta esta validada se retorna
                        if b_nr[0]:
                            return False

                # El archivo fue chequeado
                elif c[_VL_CHECK] == _VL_TRUE_CHECKED:
                    pass

                # Si no corresponde a las alternativas restantes termina la ejecución
                else:
                    return False

            return True

        self._checkVariableType(package, TYPE_OTHER, "package", Package)  # Se chequea el tipo de variable

        # Se chequea si se ha generado la estructura o no
        if not self._isStructGenerated:
            return self._throwException("VALIDATOR_ERROR_STRUCTURE_NOT_CREATED")

        b = copy.deepcopy(self._structureBoolHierarchy)

        # Se obtienen las listas de jerarquía
        hp = package.getHierarchyFiles()
        hs = self._structurePackage.getHierarchyFiles()

        # Se marca el paquete ha sido validado
        package._markAsValidated()

        # Si la lista de jerarquía del paquete está vacía o no existe
        if len(hp) <= 2 and not (len(hp) == 2 and isinstance(hp[1], list)):
            if len(hp) == 2 and regexCompare(hs[1], hp[1], self._validRegexChars):
                _validatedFilesPackage.append([hp[1], hs[1], hp[1], hp[1]])
                package._markAsValid()
                package._setValidatedFiles(_validatedFilesPackage[:], generate_hierarchies)
            return

        # Se llama a la función recursiva
        try:
            _verifyInclusionRecursive(hp[1:len(hp)], hs[1:len(hs)], hs, b, 0, b, "", 0, 0, "", "")
        except:
            return self._throwException("VALIDATOR_ERROR_ON_VALIDATE_WALK")

        # Se comprueba que el paquete sea valido
        self._checkHierarchyTree(b)
        if b[0]:
            package._markAsValid()

        # Se guardan en el paquete los archivos válidos
        # print _validatedFilesPackage
        package._setValidatedFiles(_validatedFilesPackage[:], generate_hierarchies)

        del b
