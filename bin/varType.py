#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# VARTYPE
# Maneja los tipos de variables.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == "__main__": from binpath import *  # @UnusedWildImport

# Tipos de variables permitidos
TYPE_BOOL = "Boolean"
TYPE_FLOAT = "Float"
TYPE_INT = "Integer"
TYPE_LIST = "List"
TYPE_OTHER = "Other"
TYPE_STR = "String"


def checkVariableType(var, clss, otherClass=None):
    """
    Chequea si una variable es de una determinada clase o no
    :param var: Variable a revisar
    :param clss: Clase a comprobar, String
    :param otherClass: Clase requerida si es que la clase a comprobar es del tipo TYPE_OTHER
    :return: void
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
