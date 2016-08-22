#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# ACCENTS
# Este archivo provee de funciones básicas para el tratamiento de acentos [ES-LANG]
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías de sistema
import os


def delAccent(txt):
    """
    Elimina los acentos de un string
    :param txt: String
    :return: String con acentos eliminados
    """
    txt = txt.replace("�?", "A").replace("É", "E").replace(
        "�?", "I").replace("Ó", "O").replace("Ú", "U")
    return txt.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")


def delAccentByOS(txt):
    """
    Elimina los acentos de un string sólo en Windows
    :param txt: String
    :return: String con acentos eliminados
    """
    if isWindows():
        return delAccent(txt)
    else:
        return txt


def isWindows():
    """
    Función que retorna True/False si el sistema operativo cliente es Windows o no
    :return: Boolean
    """
    if os.name == "nt":
        return True
    return False
