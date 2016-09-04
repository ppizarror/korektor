#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noinspection SpellCheckingInspection
"""
DELSPECIAL
Elimina caracteres especiales

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2014-2015
Licencia: GPLv2
"""
__author__ = "ppizarror"

# importación de librerías
import sys

reload(sys)
# noinspection PyUnresolvedReferences
sys.setdefaultencoding('UTF8')  # @UndefinedVariable

if len(sys.argv) > 1:  # si el argumento existe
    # noinspection PyArgumentEqualDefault
    archive = open(sys.argv[1], "r")
    text = []
    for i in archive:
        text.append(i)
        for j in i:
            print unicode(j)
