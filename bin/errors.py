# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ERRORS
Tratamiento de errores.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: OCTUBRE 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from accents import delAccentByOS
from colors import Color

# Códigos de errores
BAD_ERROR_CODE = "BAD_ERROR_CODE"
BR_ERRORxERROR_SET_FORM = 8
BR_ERRORxERROR_SET_SUBMIT = 9
BR_ERRORxNO_ACCESS_WEB = 1
BR_ERRORxNO_FORM = 3
BR_ERRORxNO_FORMID = 2
BR_ERRORxNO_OPENED = 0
BR_ERRORxNO_SELECTED_FORM = 5
BR_ERRORxNO_VALID_SUBMIT_EMPTY = 6
BR_ERRORxNO_VALID_SUBMIT_NOT_EQUAL = 7
BR_ERRORxNO_VALIDID = 4
ERR_CHECKTYPE = "Error al chequear un tipo de variable"
ERR_GBT = "Error al ejecutar getBetweenTags"
ERR_HDNFL = "Error al ejecutar isHiddenFile"
ERR_KWARGS_BAD_FALSE = "Kwargs encontro un parametro booleano incorrecto (false)"
ERR_KWARGS_BAD_TRUE = "Kwargs encontro un parametro booleano incorrecto (true)"
ERR_KWARGS_FOUND_INVALID_KEY = "Kwargs encontro un parametro que no existe"
ERR_KWARGS_INVALID_VALUE = "Kwargs retorno un valor incorrecto del parametro deseado"
ERR_NUMBER_CONVERTION = "Error al convertir el número"
ERR_REGX = "Error al ejecutar regexCompare"
ERROR_BADCONFIG = "La linea '{0}' del archivo de configuraciones '{1}' no es valida"
ERROR_BADINDEXCONFIG = "El indice seleccionado <{0}> no pertenece a las configuraciones cargadas"
ERROR_BADLAUNCHBIN = "La clase debe ser importada desde bin"
ERROR_BADPARAMETERTYPE = "Error en el tipo de un parametro"
ERROR_BADPARAMETERTYPE_MSG = "El parametro {0} debe ser del tipo {1}"
ERROR_BADSOURCEFOLDER = "La nueva dirección del 'Source Folder' no es una carpeta"
ERROR_BADWD = "La nueva dirección del 'Working Directory' no es una carpeta"
ERROR_CANTTRANSLATE = "El texto no se puede traducir"
ERROR_CONFIGBADEXPORT = "No se pudo guardar el archivo de configuraciones"
ERROR_CONFIGCORRUPT = "El archivo de configuraciones '{0}' está corrupto"
ERROR_CONFIGNOTEXISTENT = "El parametro <{0}> no existe en las configuraciones"
ERROR_CREATE_MENU = "No se puede crear el menu inicial, posible error en archivo de configuraciones"
ERROR_HEADER = Color.RED + "[ERROR] " + Color.END
ERROR_IMPORTERROREXTERNAL = "Ha ocurrido un error al importar las librerias de sistema externas"
ERROR_IMPORTERRORINTERNAL = "Ha ocurrido un error al importar las librerias internas de la aplicacion"
ERROR_IMPORTERRORMECHANIZE = "Ha ocurrido un error al importar la libreria mechanize"
ERROR_IMPORTSYSTEMERROR = "Ha ocurrido un error al importar las librerias de sistema"
ERROR_IMPORTWCONIO = "Error al importar WConio"
ERROR_LANGBADINDEX = "El indice <{0}> debe ser un numero entero mayor o igual a 10"
ERROR_LANGNOTEXIST = "ID[{0}] no existe en el archivo de idiomas <{1}>"
ERROR_MATPLOTLIB_NOT_INSTALLED = "La libreria grafica matplotlib no esta instalada. Pruebe utilizando el comando 'pip install matplotlib' en la terminal"
ERROR_NOCONFIGFILE = "No existe archivo de configuraciones '{0}'"
ERROR_NOFILES = "No hay archivos"
ERROR_NOLANGDEFINED = "El idioma no existe y/o no ha sido definido"
ERROR_NOLANGFILE = "No existe el archivo de idiomas '{0}'"
ERROR_NOTRANSLATECONECTION = "No se pudo establecer comunicacion con el servidor de traducciones"
ERROR_RARNOTINSTALLED_NOTWIN = "Se requieren de algunas librerías para poder descomprimir archivos RAR. Pruebe utilizando el comando 'pip install pyunpack, easyprocess, patool' en la terminal"
ERROR_RARNOTINSTALLED_WIN = "Librería rarfile no instalada. Pruebe utilizando el comando 'pip install rarfile' en la CMD de Windows"
ERROR_RARUNCOMPRESS = "Error al descomprimir el archivo RAR"
ERROR_RARUNCOMPRESS_LINUX = "Error al descomprimir el archivo RAR. Compruebe si tiene los permisos necesarios para ejecutar el programa o pruebe reinstalando unrar con el comando 'sudo apt-get install unrar' en Linux o 'brew install unrar' en OSX"
ERROR_RUNTESTS_CREATE_PLOT = "Ha ocurrido un error al crear el plot de los resultados"
ERROR_RUNTESTS_SAVE_LOG = "Ha ocurrido un error al guardar el log del test"
ERROR_RUNTESTS_SAVE_RESULTS = "Ha ocurrido un error al guardar el resultado de los tests"
ERROR_TAG_CANTRETRIEVEHTML = 16
ERROR_TAG_INITNOTCORRECTENDING = 14
ERROR_TAG_INITNOTFINDED = 13
ERROR_TAG_LASTNOTFINDED = 15
ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE = "Valor parametro incorrecto"
ERROR_TKINTER_NOT_INSTALLED = "La libreria Tkinter no esta instalada (python-tk)."
FILEMANAGER_ERROR_RESTORE_WD = "Restauracion de WD erronea"
FILEMANAGER_ERROR_SCAN = "Escaneo de archivo erroneo"
FILEMANAGER_ERROR_WD = "WD erroneo"
NO_ERROR = "OK"
PACKAGE_ERROR_NAME_NOT_FOUND = "El código de error no existe"
PACKAGE_ERROR_NO_NAME = "El nombre del paquete aún no ha sido definido"
PACKAGE_ERROR_NOT_HIERACHY_CREATED = "La jerarquía de archivos aún no ha sido construida"
PACKAGE_ERROR_NOT_INDEXED_FILES_YET = "Los archivos del paquete aún no han sido indexados"
PACKAGE_TEST_BAD_EXCEPTION_TREATMENT = "Excepcion mal creada"
PACKAGE_TEST_BAD_SEARCH_DEPTH = "La profundidad del archivo ubicado no es correcta"
PACKAGE_TEST_BAD_SEARCH_LOCATION = "La ubicacion del archivo ubicado no es la correcta"
PACKAGE_TEST_ERROR_COUNT_FILES = "Numero de archivos malo"
PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS = "Numero de subcarpetas malas"
PACKAGE_TEST_ERROR_INVALID_NAME = "El nombre de la carpeta es invalido"
PACKAGE_TEST_FOUND_INEXISTENT_FILE = "Encontro un archivo inexistente"
PACKAGE_TEST_FOUND_NOT_CORRECT_FILE = "Encontro un archivo inexistente"
PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER = "Encontro una carpeta inexistente"
ST_ERROR = "[ERR]"
ST_INFO = "[INF]"
ST_WARNING = "[WRN]"
ST_WARNING_ID = "[ERR][{0}]"
VALIDATOR_ERROR_STRUCTURE_FOLDER_DONT_EXIST = "El directorio definido para cargar la estructura valida no existe"
VALIDATOR_ERROR_STRUCTURE_NOT_CREATED = "La estructura aun no se ha creado"
VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE = "Error al chequear el hierachy tree"
WARNING_HEADER = Color.BLUE + "[WARNING] " + Color.END
WARNING_NOCONFIGFOUND = "No se han encontrado configuraciones en el archivo '{0}'"
WRAP_ERROR_MSG = 70


def createMSG(message, *args):
    """
    Función que crea un mensaje de error dado argumentos iniciales.

    :param message: Código de error
    :type message: str
    :param args: Argumentos adicionales
    :type args: list

    :return: Mensaje de error
    :rtype: str
    """
    return message.format(*args)


def st_error(msg, callExit=False, module=None, errname=None):
    """
    Muestra un mensaje de error en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param callExit: Booleano, indica si el programa debe cerrarse o no
    :type callExit: bool
    :param module: String indicando el nombre del modulo que produjo el error
    :type module: str
    :param errname: Excepcion
    :type errname: Exception

    :return: void
    :type: None
    """
    if module is None:
        print delAccentByOS(Color.RED + ST_ERROR + Color.END + " {0}".format(msg))
    else:
        print delAccentByOS(Color.RED + ST_ERROR + Color.END + " {0} ".format(msg) + \
                            "[" + Color.UNDERLINE + module + Color.END + "]")
    if errname is not None:
        print delAccentByOS("      {0}".format(str(errname)))
    if callExit:
        exit()


def st_info(msg, callExit=False):
    """
    Muestra un mensaje de información en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param callExit: Booleano, indica si el programa debe cerrarse o no
    :type callExit: bool

    :return: void
    :rtype: None
    """
    print delAccentByOS(Color.DARKCYAN + ST_INFO + Color.END + " {0}".format(msg))
    if callExit:
        exit()


def throw(errcode, *args):
    """
    Lanza un error terminal.

    :param errcode: Código de error
    :type errcode: str
    :param args: Argumentos
    :type args: list

    :return: void
    :rtype: None
    """
    st_error(createMSG(errcode, *args), True)


def st_warning(msg, callExit=False, module=None, errname=None):
    """
    Muestra un mensaje de precaución en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param callExit: Booleano, indica si el programa debe cerrarse o no
    :type callExit: bool
    :param module: String indicando el nombre del modulo que produjo el error
    :type module: str
    :param errname: Excepcion
    :type errname: Exception

    :return: void
    :rtype: None
    """
    if module is None:
        print delAccentByOS(Color.BLUE + ST_WARNING + Color.END + " {0}".format(msg))
    else:
        print delAccentByOS(Color.BLUE + ST_ERROR + Color.END + " {0} ".format(msg) + \
                            "[" + Color.UNDERLINE + module + Color.END + "]")
    if errname is not None:
        print delAccentByOS("      {0}".format(str(errname)))
    if callExit:
        exit()


def warning(warcode, *args):
    """
    Lanza una advertencia

    :param warcode: Código de la advertencia
    :type warcode: str
    :param args: Argumentos
    :type args: list

    :return: void
    :rtype: None
    """
    warcode = createMSG(warcode, args)
    st_warning(warcode, False)


def parseLangError(msg):
    """
    Formatea un código de error.

    :param msg: Mensaje de error
    :type msg: str

    :return: String con mensaje de error
    :rtype: str
    """

    def insertEach(string, each, every):
        """
        Inserta el string -each- cada -every- caracteres en el string -string-.

        :param string: String a formatear
        :type string: str
        :param each: String a insertar
        :type each: str
        :param every: Cantidad de carácteres
        :type every: int

        :return: string formateado
        :rtype: str
        """
        return each.join(string[i:i + every] for i in xrange(0, len(string), every))

    data = msg.split("::")
    code = data[0].strip().split("[")[1]
    code = code.replace("]", "")
    msg = data[1].strip()
    msg = insertEach(msg, "-\n\t    ", WRAP_ERROR_MSG)
    return Color.RED + ST_WARNING_ID.format(code) + Color.END + " " + msg


class exceptionBehaviour:
    """
    Clase que permite manejar clases de error
    """

    def __init__(self):
        """
        Constructor de la clase.

        :return: void
        :rtype: None
        """

        # Variables de clase
        self._exceptionStrBehaviour = False
        self._isEnabledExceptionThrowable = False

    def disable_exceptionAsString(self):
        """
        Desactiva el retornar los errores como String.

        :return: void
        :rtype: None
        """
        self._exceptionStrBehaviour = False

    def disable_exceptionThrow(self):
        """
        Desactiva el lanzamiento de excepciones en python en vez de la funcion thow que imprime un mensaje
        de error.

        :return: void
        :rtype: None
        """
        self._isEnabledExceptionThrowable = False

    def enable_exceptionAsString(self):
        """
        Activa el retornar los errores como String.

        :return: void
        :rtype: None
        """
        self._exceptionStrBehaviour = True
        self.disable_exceptionThrow()

    def enable_exceptionThrow(self):
        """
        Activa el lanzamiento de excepciones en python en vez de la funcion thow que imprime un mensaje
        de error.

        :return: void
        :rtype: None
        """
        self._isEnabledExceptionThrowable = True
        self.disable_exceptionAsString()

    def _throwException(self, e, *formatArgs):
        """
        Función que lanza una excepción según comportamiento.

        :param e: Error string
        :type e: str

        :return: String o void
        :rtype: object
        """
        if self._exceptionStrBehaviour:
            return e
        else:
            try:
                err = eval(e)
                err = str(err).format(*formatArgs)
            except:
                err = BAD_ERROR_CODE
            if self._isEnabledExceptionThrowable:
                err_no_accents = delAccentByOS(err)
                raise Exception(err_no_accents)
            else:
                throw(err)
