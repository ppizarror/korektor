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
# noinspection PyUnresolvedReferences
from binpath import *  # @UnusedWildImport
import ctypes
from ostype import is_windows

# Importación de librerías restringidas
_IMPORTED = [1]
try:
    # noinspection PyUnresolvedReferences
    import WConio  # @UnresolvedImport
except:
    _IMPORTED[0] = 0

if not is_windows():
    import os

# Constantes
COLOR_AQUA = "3"
COLOR_BLACK = "0"
COLOR_BLUE = "1"
COLOR_GRAY = "8"
COLOR_GREEN = "2"
COLOR_LAQUA = "B"
COLOR_LBLUE = "9"
COLOR_LGREEN = "A"
COLOR_LPURPLE = "D"
COLOR_LRED = "C"
COLOR_LWHITE = "F"
COLOR_LYELLOW = "E"
COLOR_PURPLE = "5"
COLOR_RED = "4"
COLOR_WHITE = "7"
COLOR_YELLOW = "6"


def color_cmd(cmd, color):
    """
    Función que imprime un mensaje con un color.

    :param cmd: String a imprimir en consola
    :type cmd: str
    :param color: Número del color
    :type color: int

    :return: void
    :rtype: None
    """
    if _IMPORTED[0] and is_windows():
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
    else:
        if not is_windows():
            os.system('clear')


def create_color(background, text):
    """
    Función que crea un color.

    :param background: Color del fondo
    :type background: str
    :param text: Color del texto
    :type text: str

    :return: Número del color
    :rtype: int
    """
    return eval("0x" + background + text)


def single_color(color):
    """
    Establece la consola en un sólo color.

    :param color: Número del color
    :type color: int

    :return: void
    :rtype: None
    """
    if _IMPORTED[0] and is_windows():
        try:
            ct_krnl = ctypes.windll.kernel32.GetStdHandle(-11)  # @UndefinedVariable
            ctypes.windll.kernel32.SetConsoleTextAttribute(ct_krnl, color)  # @UndefinedVariable
        except:
            pass


# noinspection PyClassHasNoInit
class Colors:
    """
    Permite manejar colores en la terminal.
    """

    @staticmethod
    def bold():
        """
        Texto en negrita.

        :return: String con formato
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[1m'

    @staticmethod
    def blue():
        """
        Colors azul.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            single_color(create_color(COLOR_BLACK, COLOR_RED))
            return ''
        else:
            return '\033[94m'

    @staticmethod
    def cyan():
        """
        Colors púrpura.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            single_color(create_color(COLOR_BLACK, COLOR_LAQUA))
            return ''
        else:
            return '\033[96m'

    @staticmethod
    def dark_cyan():
        """
        Colors cian oscuro.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            single_color(create_color(COLOR_BLACK, COLOR_LBLUE))
            return ''
        else:
            return '\033[36m'

    @staticmethod
    def end():
        """
        Terminación del formato.

        :return: String con formato
        :rtype: str
        """
        if is_windows():
            single_color(create_color(COLOR_BLACK, COLOR_WHITE))
            return ''
        else:
            return '\033[0m'

    @staticmethod
    def green():
        """
        Colors verde.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            single_color(create_color(COLOR_BLACK, COLOR_GREEN))
            return ''
        else:
            return '\033[92m'

    @staticmethod
    def purple():
        """
        Colors púrpura.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            single_color(create_color(COLOR_BLACK, COLOR_PURPLE))
            return ''
        else:
            return '\033[95m'

    @staticmethod
    def red():
        """
        Colors rojo.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            single_color(create_color(COLOR_BLACK, COLOR_RED))
            return ''
        else:
            return '\033[91m'

    @staticmethod
    def underline():
        """
        Texto subrayado.

        :return: String con formato
        :rtype: str
        """
        if is_windows():
            return ''
        else:
            return '\033[4m'

    @staticmethod
    def yellow():
        """
        Colors verde.

        :return: String con color
        :rtype: str
        """
        if is_windows():
            single_color(create_color(COLOR_BLACK, COLOR_YELLOW))
            return ''
        else:
            return '\033[93m'
