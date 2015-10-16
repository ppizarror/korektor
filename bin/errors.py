# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRORS
# Tratamiento de errores
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías
from colors import Color

# Constantes
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
ERROR_BADCONFIG = "La linea '{0}' del archivo de configuraciones '{1}' no es valida"
ERROR_BADINDEXCONFIG = "El indice seleccionado <{0}> no pertenece a las configuraciones cargadas"
ERROR_BADLAUNCHBIN = "La clase debe ser importada desde bin"
ERROR_CANTTRANSLATE = "El texto no se puede traducir"
ERROR_CONFIGBADEXPORT = "No se pudo guardar el archivo de configuraciones"
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
ERROR_NOLANGDEFINED = "El idioma no existe y/o no ha sido definido"
ERROR_NOLANGFILE = "No existe el archivo de idiomas '{0}'"
ERROR_NOTRANSLATECONECTION = "No se pudo establecer comunicacion con el servidor de traducciones"
ERROR_TAG_CANTRETRIEVEHTML = 16
ERROR_TAG_INITNOTCORRECTENDING = 14
ERROR_TAG_INITNOTFINDED = 13
ERROR_TAG_LASTNOTFINDED = 15
NO_ERROR = "OK"
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
        print Color.RED + ST_ERROR + Color.END + " {0}".format(msg)
    else:
        print Color.RED + ST_ERROR + Color.END + " {0} ".format(msg) + "[" + Color.UNDERLINE + module + Color.END + "]"
    if errname is not None:
        print "      {0}".format(str(errname))
    if callExit:
        exit()


def st_info(msg, callExit=False):
    """Muestra un mensaje de información en pantalla"""
    print Color.DARKCYAN + ST_INFO + Color.END + " {0}".format(msg)
    if callExit:
        exit()


def throw(errcode, *args):
    """
    Lanza un error terminal
    """
    errcode = createMSG(errcode, args)
    st_error(errcode, True)


def st_warning(msg, callExit=False):
    """Muestra un mensaje de precaución en pantalla"""
    print Color.BLUE + ST_WARNING + Color.END + " {0}".format(msg)
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
    ct = 0
    ci = 0
    msg = Color.RED + ST_WARNING_ID.format(code) + Color.END + " " + msg
    return msg


# Test
if __name__ == '__main__':
    st_error("Este es un error grave", False)
    st_info("Esta es una información")
    st_warning("Esta es una advertencia")
