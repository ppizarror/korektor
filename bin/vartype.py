#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noinspection SpellCheckingInspection
"""
VARTYPE
Maneja los tipos de variables.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    from binpath import *  # @UnusedWildImport
from errors import ExceptionBehaviour

# Tipos de variables permitidos
TYPE_BOOL = "Boolean"
TYPE_FLOAT = "Float"
TYPE_INT = "Integer"
TYPE_LIST = "List"
TYPE_OTHER = "Other"
TYPE_STR = "String"


# noinspection SpellCheckingInspection
def check_variable_type(var, clss, other_class=None):
    """
    Chequea si una variable es de una determinada clase o no.

    :param var: Variable a revisar
    :type var: object
    :param clss: Clase a comprobar, String
    :type clss: str
    :param other_class: Clase requerida si es que la clase a comprobar es del tipo TYPE_OTHER
    :type other_class: object

    :return: Booleano resultante de la comparación
    :rtype: bool
    """
    if clss == TYPE_FLOAT:
        return isinstance(var, float)
    elif clss == TYPE_INT:
        return isinstance(var, int)
    elif clss == TYPE_LIST:
        return isinstance(var, list)
    elif clss == TYPE_STR:
        return isinstance(var, basestring)
    elif clss == TYPE_BOOL:
        return isinstance(var, bool)
    elif clss == TYPE_OTHER:
        return isinstance(var, other_class)
    else:
        return False


# noinspection PyMissingConstructor,PyTypeChecker
class VarTypedClass(ExceptionBehaviour):
    """
    Clase asociada al manejo de tipos de variable.
    """

    def __init__(self):
        """
        Constructor de la clase

        :return: void
        :rtype: None
        """
        pass

    # noinspection SpellCheckingInspection
    def _check_variable_type(self, var, type_var, param_name, other_class=None):
        """
        Chequea si una variable es de una determinada clase o no.

        :param var: Variable a revisar
        :type var: object
        :param type_var: Clase a comprobar, String
        :type type_var: str
        :param param_name: Nombre del parámetro erróneo
        :type param_name: str, unicode
        :param other_class: Clase requerida si es que la clase a comprobar es del tipo TYPE_OTHER
        :type other_class: object

        :return: void
        :rtype: None
        """
        if not check_variable_type(var, type_var, other_class):
            self._throw_exception("ERROR_BADPARAMETERTYPE_MSG", param_name, type_var)
