#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noinspection SpellCheckingInspection
"""
OSTYPE
Permite manejar el tipo de sistema operativo huésped, comprobando el tipo, versión, etc.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
import platform

# Constantes del programa
_PLATFORM_CYGWIN = "cygwin"
_PLATFORM_JAVA = "java"
_PLATFORM_LINUX = "linux"
_PLATFORM_WINDOWS = "windows"


def is_cygwin():
    """
    Verifica que el sistema operativo huésped sea Cygwin.

    :return: Booleano indicando pertenencia
    :rtype: bool
    """
    return _PLATFORM_CYGWIN in str(platform.system()).lower()


def is_java():
    """
    Verifica que el sistema operativo huésped sea Java.

    :return: Booleano indicando pertenencia
    :rtype: bool
    """
    return _PLATFORM_JAVA in str(platform.system()).lower()


def is_linux():
    """
    Verifica que el sistema operativo huésped sea Linux.

    :return: Booleano indicando pertenencia
    :rtype: bool
    """
    return _PLATFORM_LINUX in str(platform.system()).lower()


def is_windows():
    """
    Verifica que el sistema operativo huésped sea Windows.

    :return: Booleano indicando pertenencia
    :rtype: bool
    """
    return _PLATFORM_WINDOWS in str(platform.system()).lower()
