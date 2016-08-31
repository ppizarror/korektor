#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from errors import exceptionBehaviour

# Tipos de variables permitidos
TYPE_BOOL = "Boolean"
TYPE_FLOAT = "Float"
TYPE_INT = "Integer"
TYPE_LIST = "List"
TYPE_OTHER = "Other"
TYPE_STR = "String"


def checkVariableType(var, clss, otherClass=None):
    """
    Chequea si una variable es de una determinada clase o no.

    :param var: Variable a revisar
    :type var: object
    :param clss: Clase a comprobar, String
    :type clss: str
    :param otherClass: Clase requerida si es que la clase a comprobar es del tipo TYPE_OTHER
    :type otherClass: object

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
        return isinstance(var, otherClass)
    else:
        return False


# noinspection PyMissingConstructor
class varTypedClass(exceptionBehaviour):
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

    def _checkVariableType(self, var, typeVar, paramName, otherClass=None):
        """
        Chequea si una variable es de una determinada clase o no.

        :param var: Variable a revisar
        :type var: object
        :param typeVar: Clase a comprobar, String
        :type typeVar: str
        :param otherClass: Clase requerida si es que la clase a comprobar es del tipo TYPE_OTHER
        :type otherClass: object

        :return: void
        :rtype: None
        """
        if not checkVariableType(var, typeVar, otherClass):
            self._throwException("ERROR_BADPARAMETERTYPE_MSG", paramName, typeVar)
