#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
KWARGSUTILS
Funciones utilitarias para tratar los argumentos del tipo **kwargs

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    from binpath import *  # @UnusedWildImport


def kwargExistsKey(kwargs, keyParam):
    """
    Retorna true/false indicando si una llave existe en el kwargs.

    :param kwargs: Keywords list
    :type kwargs: list, dict
    :param keyParam: Nombre del parámetro
    :type keyParam: str

    :return: Booleano indicando pertenencia
    :rtype: bool
    """

    try:
        return keyParam in kwargs
    except:
        return False


def kwargGetValue(kwargs, keyParam, valueIfNotFound=None):
    """
    Retorna el valor de un parámetro.

    :param kwargs: Keywords list
    :type kwargs: list, dict
    :param keyParam: Nombre del parámetro
    :type keyParam: str
    :param valueIfNotFound: Valor si es que no se encuentra la llave
    :type valueIfNotFound: object

    :return: Objeto almacenado con la llave
    :rtype: object
    """

    if kwargExistsKey(kwargs, keyParam):
        return kwargs[keyParam]
    return valueIfNotFound


# noinspection PyTypeChecker
def kwargIsFalseParam(kwargs, keyParam):
    """
    Comprueba si una llave en kwargs es True.

    :param kwargs: Keywords list
    :type kwargs: list, dict
    :param keyParam: Nombre del parámetro
    :type keyParam: str

    :return: Booleano indicando pertenencia
    :rtype: bool
    """

    if kwargExistsKey(kwargs, keyParam):
        val = kwargs[keyParam]
        if isinstance(val, bool):
            return not val
        else:
            val = str(val).strip()
            if val.lower() == "false" or val == "0":
                return True
    return False


# noinspection PyTypeChecker
def kwargIsTrueParam(kwargs, keyParam):
    """
    Comprueba si una llave en kwargs es True.

    :param kwargs: Keywords list
    :type kwargs: list, dict
    :param keyParam: Nombre del parámetro
    :type keyParam: str

    :return: Booleano indicando pertenencia
    :rtype: bool
    """

    if kwargExistsKey(kwargs, keyParam):
        val = kwargs[keyParam]
        if isinstance(val, bool):
            return val
        else:
            val = str(val).strip()
            if val.lower() == "true" or val == "1":
                return True
    return False
