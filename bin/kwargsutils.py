#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noinspection SpellCheckingInspection
"""
KWARGSUTILS
Funciones utilitarias para tratar los argumentos del tipo **kwargs

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"


def kwarg_exists_key(kwargs, key_param):
    """
    Retorna true/false indicando si una llave existe en el kwargs.

    :param kwargs: Keywords list
    :type kwargs: list, dict
    :param key_param: Nombre del parámetro
    :type key_param: str

    :return: Booleano indicando pertenencia
    :rtype: bool
    """

    try:
        return key_param in kwargs
    except:
        return False


def kwarg_get_value(kwargs, key_param, value_if_not_found=None):
    """
    Retorna el valor de un parámetro.

    :param kwargs: Keywords list
    :type kwargs: list, dict
    :param key_param: Nombre del parámetro
    :type key_param: str
    :param value_if_not_found: Valor si es que no se encuentra la llave
    :type value_if_not_found: object

    :return: Objeto almacenado con la llave
    :rtype: object
    """

    if kwarg_exists_key(kwargs, key_param):
        return kwargs[key_param]
    return value_if_not_found


# noinspection PyTypeChecker
def kwarg_is_false_param(kwargs, key_param):
    """
    Comprueba si una llave en kwargs es True.

    :param kwargs: Keywords list
    :type kwargs: list, dict
    :param key_param: Nombre del parámetro
    :type key_param: str

    :return: Booleano indicando pertenencia
    :rtype: bool
    """

    if kwarg_exists_key(kwargs, key_param):
        val = kwargs[key_param]
        if isinstance(val, bool):
            return not val
        else:
            val = str(val).strip()
            if val.lower() == "false" or val == "0":
                return True
    return False


# noinspection PyTypeChecker
def kwarg_is_true_param(kwargs, key_param):
    """
    Comprueba si una llave en kwargs es True.

    :param kwargs: Keywords list
    :type kwargs: list, dict
    :param key_param: Nombre del parámetro
    :type key_param: str

    :return: Booleano indicando pertenencia
    :rtype: bool
    """

    if kwarg_exists_key(kwargs, key_param):
        val = kwargs[key_param]
        if isinstance(val, bool):
            return val
        else:
            val = str(val).strip()
            if val.lower() == "true" or val == "1":
                return True
    return False
