#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
COLORS
Maneja los colores en la consola.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    from binpath import *  # @UnusedWildImport
import ctypes
import os  # @Reimport

# Importación de librerías restringidas
_IMPORTED = [1, 1]
try:
    # noinspection PyUnresolvedReferences
    import WConio  # @UnresolvedImport
except:
    _IMPORTED[0] = 0

# Constantes
_CMD_COLORS = {"blue": 0x10,
               "gray": 0x80,
               "green": 0x20,
               "lblue": 0x90,
               "lgray": 0x70,
               "lgreen": 0xA0,
               "lred": 0xC0,
               "purple": 0x50,
               "white": 0xF0,
               "yellow": 0x60,
               "lpurple": 0xD0,
               "lyellow": 0xE0,
               "red": 0x40
               }


def color_cmd(cmd, color):
    """
    Función que imprime un mensaje con un color.

    :param cmd: String a imprimir en consola
    :type cmd: str
    :param color: Color
    :type color: str

    :return: void
    :rtype: None
    """
    if color in _CMD_COLORS and _IMPORTED[0]:
        color = _CMD_COLORS[color]
        try:
            ct_krnl = ctypes.windll.kernel32.GetStdHandle(-11)  # @UndefinedVariable
            ctypes.windll.kernel32.SetConsoleTextAttribute(ct_krnl, color)  # @UndefinedVariable
        except:
            pass
        print cmd,
        try:
            ct_krnl = ctypes.windll.kernel32.GetStdHandle(-11)  # @UndefinedVariable
            ctypes.windll.kernel32.SetConsoleTextAttribute(ct_krnl, 0x07)  # @UndefinedVariable
        except:
            pass
    else:
        print cmd,


def clrscr():
    """
    Limpia la pantalla.

    :return: void
    :rtype: None
    """
    if _IMPORTED[0]:
        try:
            WConio.clrscr()  # @UndefinedVariable
        except:
            pass


def single_color(color):
    """
    Establece la consola en un sólo color.

    :param color: String del color
    :type color: str

    :return: void
    :rtype: None
    """
    if color in _CMD_COLORS and _IMPORTED[0]:
        color = _CMD_COLORS[color]
        try:
            ct_krnl = ctypes.windll.kernel32.GetStdHandle(-11)  # @UndefinedVariable
            ctypes.windll.kernel32.SetConsoleTextAttribute(ct_krnl, color)  # @UndefinedVariable
        except:
            pass


# noinspection PyClassHasNoInit
class Color:
    """
    Permite manejar colores en la terminal.
    """

    if os.name != "nt":
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    else:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERLINE = ''
        END = ''
