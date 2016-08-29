#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ACCENTS
Este archivo provee de funciones básicas para el tratamiento de acentos [ES-LANG].

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías de sistema
import os


def delAccent(txt):
    """
    Elimina los acentos de un string.

    :param txt: String a tratar
    :type txt: str

    :return: String con acentos eliminados
    :rtype: str
    """
    txt = txt.replace("Á", "A").replace("É", "E").replace(
        "Í", "I").replace("Ó", "O").replace("Ú", "U")
    return txt.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")


def delAccentByOS(txt):
    """
    Elimina los acentos de un string sólo en Windows.

    :param txt: String a tratar
    :type txt: str

    :return: String con acentos eliminados
    :rtype: str
    """
    if isWindows():
        return delAccent(txt)
    else:
        return txt


def isWindows():
    """
    Función que retorna True/False si el sistema operativo cliente es Windows o no.

    :return: Booleano indicando pertenencia
    :rtype: bool
    """
    if os.name == "nt":
        return True
    return False
