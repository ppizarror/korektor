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
from accents import del_accent_by_os
from colors import Colors

# Constantes
COLOR = Colors()

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
ERR_GBT = "Error al ejecutar get_between_tags"
ERR_HDNFL = "Error al ejecutar is_hidden_file_utils"
ERR_KWARGS_BAD_FALSE = "Kwargs encontró un parámetro booleano incorrecto (false)"
ERR_KWARGS_BAD_TRUE = "Kwargs encontró un parámetro booleano incorrecto (true)"
ERR_KWARGS_FOUND_INVALID_KEY = "Kwargs encontró un parámetro que no existe"
ERR_KWARGS_INVALID_VALUE = "Kwargs retorno un valor incorrecto del parámetro deseado"
ERR_NUMBER_CONVERTION = "Error al convertir el número"
ERR_REGX = "Error al ejecutar regex_compare"
ERROR_BADCONFIG = "La linea '{0}' del archivo de configuraciones '{1}' no es valida"
ERROR_BADINDEXCONFIG = "El índice seleccionado <{0}> no pertenece a las configuraciones cargadas"
ERROR_BADLAUNCHBIN = "La clase debe ser importada desde bin"
ERROR_BADPARAMETERTYPE = "Error en el tipo de un parámetro"
ERROR_BADPARAMETERTYPE_MSG = "El parámetro {0} debe ser del tipo {1}"
ERROR_BADSOURCEFOLDER = "La nueva dirección del 'Source Folder' no es una carpeta"
ERROR_BADWD = "La nueva dirección del 'Working Directory' no es una carpeta"
ERROR_CANTTRANSLATE = "El texto no se puede traducir"
ERROR_CONFIGBADEXPORT = "No se pudo guardar el archivo de configuraciones"
ERROR_CONFIGCORRUPT = "El archivo de configuraciones '{0}' está corrupto"
ERROR_CONFIGNOTEXISTENT = "El parámetro <{0}> no existe en las configuraciones"
ERROR_CREATE_MENU = "No se puede crear el menu inicial, posible error en archivo de configuraciones"
ERROR_GETTING_OS = "Ocurrió un error al obtener el tipo de sistema operativo"
ERROR_HEADER = COLOR.red() + "[ERROR] " + COLOR.end()
ERROR_IMPORTERROREXTERNAL = "Ha ocurrido un error al importar las librerías de sistema externas"
ERROR_IMPORTERRORINTERNAL = "Ha ocurrido un error al importar las librerías internas de la aplicación"
ERROR_IMPORTERRORMECHANIZE = "Ha ocurrido un error al importar la librería mechanize"
ERROR_IMPORTSYSTEMERROR = "Ha ocurrido un error al importar las librerías de sistema"
ERROR_IMPORTWCONIO = "Error al importar WConio"
ERROR_LANGBADINDEX = "El índice <{0}> debe ser un numero entero mayor o igual a 10"
ERROR_LANGNOTEXIST = "ID[{0}] no existe en el archivo de idiomas <{1}>"
ERROR_MATPLOTLIB_NOT_INSTALLED = "La librería gráfica matplotlib no esta instalada. Pruebe utilizando el comando 'pip install matplotlib' en la terminal"
ERROR_NOCONFIGFILE = "No existe archivo de configuraciones '{0}'"
ERROR_NOFILES = "No hay archivos"
ERROR_NOLANGDEFINED = "El idioma no existe y/o no ha sido definido"
ERROR_NOLANGFILE = "No existe el archivo de idiomas '{0}'"
ERROR_NOTRANSLATECONECTION = "No se pudo establecer comunicación con el servidor de traducciones"
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
ERROR_TEST_CONFIGLOADER_BAD_GET_VALUE = "Valor parámetro incorrecto"
ERROR_TKINTER_NOT_INSTALLED = "La librería Tkinter no esta instalada (python-tk)."
FILEMANAGER_ERROR_RESTORE_WD = "Restauración de WD errónea"
FILEMANAGER_ERROR_SCAN = "Escaneo de archivo erróneo"
FILEMANAGER_ERROR_WD = "WD erróneo"
NO_ERROR = "OK"
PACKAGE_ERROR_NAME_NOT_FOUND = "El código de error no existe"
PACKAGE_ERROR_NO_NAME = "El nombre del paquete aún no ha sido definido"
PACKAGE_ERROR_NOT_HIERARCHY_CREATED = "La jerarquía de archivos aun no ha sido construida"
PACKAGE_ERROR_NOT_HIERARCHY_INVALID_CREATED = "La jerarquía de los archivos no válidos no ha sido creada"
PACKAGE_ERROR_NOT_HIERARCHY_VALID_CREATED = "La jerarquía de los archivos válidos no ha sido creada"
PACKAGE_ERROR_NOT_INDEXED_FILES_YET = "Los archivos del paquete aun no han sido indexados"
PACKAGE_ERROR_NOT_VALIDATED_YET = "El paquete aun no ha sido validado"
PACKAGE_TEST_BAD_EXCEPTION_TREATMENT = "Excepción mal creada"
PACKAGE_TEST_BAD_SEARCH_DEPTH = "La profundidad del archivo ubicado no es correcta"
PACKAGE_TEST_BAD_SEARCH_LOCATION = "La ubicación del archivo ubicado no es la correcta"
PACKAGE_TEST_ERROR_COUNT_FILES = "Numero de archivos malo"
PACKAGE_TEST_ERROR_COUNT_SUBFOLDERS = "Numero de subcarpetas malas"
PACKAGE_TEST_ERROR_INVALID_NAME = "El nombre de la carpeta es invalido"
PACKAGE_TEST_FOUND_INEXISTENT_FILE = "Encontró un archivo inexistente"
PACKAGE_TEST_FOUND_NOT_CORRECT_FILE = "Encontró un archivo inexistente"
PACKAGE_TEST_FOUND_NOT_CORRECT_FOLDER = "Encontró una carpeta inexistente"
ST_ERROR = "[ERR]"
ST_INFO = "[INF]"
ST_WARNING = "[WRN]"
ST_WARNING_ID = "[ERR][{0}]"
VALIDATOR_ERROR_ON_RETRIEVE_PACKAGES = "Error al obtener los paquetes al validar"
VALIDATOR_ERROR_ON_VALIDATE_WALK = "Error al validar la estructura en forma recursiva"
VALIDATOR_ERROR_ON_VALIDATE_WALK_EXCEPTION = "Ha ocurrido un error en el walk recursivo"
VALIDATOR_ERROR_ON_VALIDATE_WALK_RECURSIVE = "Error al validar la estructura en el llamado recursivo del walk"
VALIDATOR_ERROR_STRUCTURE_FOLDER_DONT_EXIST = "El directorio definido para cargar la estructura valida no existe"
VALIDATOR_ERROR_STRUCTURE_NOT_CREATED = "La estructura aun no se ha creado"
VALIDATOR_TEST_ERROR_CHECK_HIERACHY_TREE = "Error al chequear el hierarchy tree"
VALIDATOR_TEST_ERROR_INVALIDATE_CORRECT = "Error al invalidar un paquete correcto"
VALIDATOR_TEST_ERROR_VALIDATE_EMPTY_BOTH = "Error al validar directorio y estructura vacíos"
VALIDATOR_TEST_ERROR_VALIDATE_INCORRECT = "Error al validar un paquete incorrecto"
WARNING_HEADER = COLOR.blue() + "[WARNING] " + COLOR.end()
WARNING_NOCONFIGFOUND = "No se han encontrado configuraciones en el archivo '{0}'"
WRAP_ERROR_MSG = 70


def create_msg(message, *args):
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


def st_error(msg, call_exit=False, module=None, errname=None):
    """
    Muestra un mensaje de error en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param call_exit: Booleano, indica si el programa debe cerrarse o no
    :type call_exit: bool
    :param module: String indicando el nombre del modulo que produjo el error
    :type module: str
    :param errname: Excepción
    :type errname: Exception

    :return: void
    :type: None
    """
    if module is None:
        print del_accent_by_os(COLOR.red() + ST_ERROR + COLOR.end() + " {0}".format(msg))
    else:
        print del_accent_by_os(
            COLOR.red() + ST_ERROR + COLOR.end() + " {0} ".format(
                msg) + "[" + COLOR.underline() + module + COLOR.end() + "]")
    if errname is not None:
        print del_accent_by_os("      {0}".format(str(errname)))
    if call_exit:
        exit()


def st_info(msg, call_exit=False):
    """
    Muestra un mensaje de información en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param call_exit: Booleano, indica si el programa debe cerrarse o no
    :type call_exit: bool

    :return: void
    :rtype: None
    """
    print del_accent_by_os(COLOR.dark_cyan() + ST_INFO + COLOR.end() + " {0}".format(msg))
    if call_exit:
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
    st_error(create_msg(errcode, *args), True)


def st_warning(msg, call_exit=False, module=None, errname=None):
    """
    Muestra un mensaje de precaución en pantalla.

    :param msg: String del mensaje
    :type msg: str
    :param call_exit: Booleano, indica si el programa debe cerrarse o no
    :type call_exit: bool
    :param module: String indicando el nombre del modulo que produjo el error
    :type module: str
    :param errname: Excepción
    :type errname: Exception

    :return: void
    :rtype: None
    """
    if module is None:
        print del_accent_by_os(COLOR.blue() + ST_WARNING + COLOR.end() + " {0}".format(msg))
    else:
        print del_accent_by_os(
            COLOR.blue() + ST_ERROR + COLOR.end() + " {0} ".format(
                msg) + "[" + COLOR.underline() + module + COLOR.end() + "]")
    if errname is not None:
        print del_accent_by_os("      {0}".format(str(errname)))
    if call_exit:
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
    warcode = create_msg(warcode, args)
    st_warning(warcode)


def parse_lang_error(msg):
    """
    Formatea un código de error.

    :param msg: Mensaje de error
    :type msg: str

    :return: String con mensaje de error
    :rtype: str
    """

    def insert_each(string, each, every):
        """
        Inserta el string -each- cada -every- caracteres en el string -string-.

        :param string: String a formatear
        :type string: str
        :param each: String a insertar
        :type each: str
        :param every: Cantidad de caracteres
        :type every: int

        :return: string formateado
        :rtype: str
        """
        return each.join(string[i:i + every] for i in xrange(0, len(string), every))

    data = msg.split("::")
    code = data[0].strip().split("[")[1]
    code = code.replace("]", "")
    msg = data[1].strip()
    msg = insert_each(msg, "-\n\t    ", WRAP_ERROR_MSG)
    return COLOR.red() + ST_WARNING_ID.format(code) + COLOR.end() + " " + msg


class ExceptionBehaviour:
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
        self._exceptionMsgCode = False
        self._exceptionsDisabled = False
        self._exceptionStrBehaviour = False
        self._isEnabledExceptionThrowable = False

    def disable_exception_as_string(self):
        """
        Desactiva el retornar los errores como String.

        :return: void
        :rtype: None
        """
        self._exceptionStrBehaviour = False

    def disable_exception_code(self):
        """
        Desactiva el retornar el mensaje de cada excepción como un código de error.

        :return: void
        :rtype: None
        """
        self._exceptionMsgCode = False

    def disable_exceptions(self):
        """
        Desactiva todas las excepciones.

        :return: void
        :rtype: None
        """
        self.disable_exception_as_string()
        self.disable_exception_throw()
        self._exceptionsDisabled = True

    def disable_exception_throw(self):
        """
        Desactiva el lanzamiento de excepciones en python en vez de la función throw que imprime un mensaje
        de error.

        :return: void
        :rtype: None
        """
        self._isEnabledExceptionThrowable = False

    def enable_exception_as_string(self):
        """
        Activa el retornar los errores como String.

        :return: void
        :rtype: None
        """
        self._exceptionStrBehaviour = True
        self.disable_exception_throw()
        self.enable_exceptions()

    def enable_exception_code(self):
        """
        Activa el retornar el mensaje de cada excepción como un código de error.

        :return: void
        :rtype: None
        """
        self._exceptionMsgCode = True

    def enable_exceptions(self):
        """
        Activa las excepciones.

        :return: void
        :rtype: None
        """
        self._exceptionsDisabled = False

    def enable_exception_throw(self):
        """
        Activa el lanzamiento de excepciones en python en vez de la función throw que imprime un mensaje
        de error.

        :return: void
        :rtype: None
        """
        self._isEnabledExceptionThrowable = True
        self.disable_exception_as_string()
        self.enable_exceptions()

    # noinspection PyUnusedLocal
    def _throw_exception(self, e, *format_args):
        """
        Función que lanza una excepción según comportamiento.

        :param e: Error string
        :type e: str
        :param format_args: Argumentos opcionales de los errores
        :type format_args: list

        :return: String o void
        :rtype: object
        """
        # Si no se han deshabilitado las excepciones
        if not self._exceptionsDisabled:

            # Se obtiene el mensaje a retornar (string o código de error)
            err = ""
            if self._exceptionMsgCode:  # Como código
                try:  # Se comprueba que el código exista
                    eval(e)
                    err = e
                except:
                    err = "BAD_ERROR_CODE"
            else:  # Como string (mensaje)
                try:  # Se comprueba que el código exista
                    err = del_accent_by_os(eval(e))
                except:
                    err = BAD_ERROR_CODE

            # Si la excepción se retorna como un string
            if self._exceptionStrBehaviour:
                return err

            # Si la excepción lanza error o Exception
            else:

                # Lanzar excepción
                if self._isEnabledExceptionThrowable:
                    raise Exception(err)

                # Lanzar error
                else:
                    throw(err)
