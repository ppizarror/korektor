# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# ERRORS
# Tratamiento de errores.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: OCTUBRE 2015 - 2016
# Licencia: GPLv2

# Importación de librerías
from accents import delAccentByOS
from colors import Color
# from langs import langLoader  # @UnusedImport

# Constantes
BR_ERRORxERROR_SET_FORM = 8
BR_ERRORxERROR_SET_SUBMIT = 9
BR_ERRORxNO_ACCESS_WEB = 1
BR_ERRORxNO_FORM = 3
BR_ERRORxNO_FORMID = 2
BR_ERRORxNO_OPENED = 0
BR_ERRORxNO_SELECTED_FORM = 5
BR_ERRORxNO_VALIDID = 4
BR_ERRORxNO_VALID_SUBMIT_EMPTY = 6
BR_ERRORxNO_VALID_SUBMIT_NOT_EQUAL = 7
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
ERROR_NOCONFIGFILE = "No existe archivo de configuraciones '{0}'"
ERROR_NOFILES = "No hay archivos"
ERROR_NOLANGDEFINED = "El idioma no existe y/o no ha sido definido"
ERROR_NOLANGFILE = "No existe el archivo de idiomas '{0}'"
ERROR_NOTRANSLATECONECTION = "No se pudo establecer comunicacion con el servidor de traducciones"
ERROR_RARNOTINSTALLED_NOTWIN = "Error, se requieren de algunas librerías para poder descomprimir archivos RAR. Pruebe utilizando el comando 'pip install pyunpack, easyprocess, patool' en la terminal"
ERROR_RARNOTINSTALLED_WIN = "Error, librería rarfile no instalada. Pruebe utilizando el comando 'pip install rarfile' en la CMD de Windows"
ERROR_RARUNCOMPRESS = "Error al descomprimir el archivo RAR"
ERROR_RARUNCOMPRESS_LINUX = "Error al descomprimir el archivo RAR. Compruebe si tiene los permisos necesarios para ejecutar el programa o pruebe reinstalando unrar con el comando 'sudo apt-get install unrar' en Linux o 'brew install unrar' en OSX"
ERROR_TAG_CANTRETRIEVEHTML = 16
ERROR_TAG_INITNOTCORRECTENDING = 14
ERROR_TAG_INITNOTFINDED = 13
ERROR_TAG_LASTNOTFINDED = 15
ERROR_TKINTER_NOT_INSTALLED = "Error, la libreria Tkinter no esta instalada (python-tk)."
ERR_CHECKTYPE = "Error al chequear un tipo de variable"
ERR_GBT = "Error al ejecutar getBetweenTags"
ERR_HDNFL = "Error al ejecutar isHiddenFile"
ERR_REGX = "Error al ejecutar regexCompare"
FILEMANAGER_ERROR_RESTORE_WD = "Restauracion de WD erronea"
FILEMANAGER_ERROR_SCAN = "Escaneo de archivo erroneo"
FILEMANAGER_ERROR_WD = "WD erroneo"
NO_ERROR = "OK"
PACKAGE_ERROR_NAME_NOT_FOUND = "El código de error no existe"
PACKAGE_ERROR_NOT_HIERACHY_CREATED = "La jerarquía de archivos aún no ha sido construida"
PACKAGE_ERROR_NOT_INDEXED_FILES_YET = "Los archivos del paquete aún no han sido indexados"
PACKAGE_ERROR_NO_NAME = "El nombre del paquete aún no ha sido definido"
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
WARNING_HEADER = Color.BLUE + "[WARNING] " + Color.END
WARNING_NOCONFIGFOUND = "No se han encontrado configuraciones en el archivo '{0}'"
WRAP_ERROR_MSG = 70

def createMSG(message, *args):
    """
    Función que crea un mensaje de error dado argumentos iniciales
    :param message: Código de error
    :param args: Mensaje
    :return: void
    """
    return message.format(*args)


def st_error(msg, callExit=False, module=None, errname=None):
    """Muestra un mensaje de error en pantalla"""
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
    """Muestra un mensaje de información en pantalla"""
    print delAccentByOS(Color.DARKCYAN + ST_INFO + Color.END + " {0}".format(msg))
    if callExit:
        exit()


def throw(errcode, *args):
    """
    Lanza un error terminal
    """
    st_error(createMSG(errcode, *args), True)


def st_warning(msg, callExit=False):
    """Muestra un mensaje de precaución en pantalla"""
    print delAccentByOS(Color.BLUE + ST_WARNING + Color.END + " {0}".format(msg))
    if callExit:
        exit()


def warning(warcode, *args):
    """
    Lanza un error terminal
    """
    warcode = createMSG(warcode, args)
    st_warning(warcode, False)


def parseLangError(msg):
    """
    Formatea un código de error
    :param msg:
    :return:
    """

    def insertEach(string, each, every):
        """
        Inserta el string -each- cada -every- caracteres en el string -string-
        :param string: String a formatear
        :param each: String a insertar
        :param every: Cantidad de carácteres
        :return: string formateado
        """
        return each.join(string[i:i + every] for i in xrange(0, len(string), every))

    data = msg.split("::")
    code = data[0].strip().split("[")[1]
    code = code.replace("]", "")
    msg = data[1].strip()
    msg = insertEach(msg, "-\n\t    ", WRAP_ERROR_MSG)
    return Color.RED + ST_WARNING_ID.format(code) + Color.END + " " + msg
