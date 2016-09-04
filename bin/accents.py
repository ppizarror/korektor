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

# Importación de librerías
from ostype import is_windows


def del_accent(txt):
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


def del_accent_by_os(txt):
    """
    Elimina los acentos de un string sólo en Windows.

    :param txt: String a tratar
    :type txt: str

    :return: String con acentos eliminados
    :rtype: str
    """

    if is_windows():
        return del_accent(txt)
    else:
        return txt
