#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DELSPECIAL
Elimina carácteres especiales

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2014-2015
Licencia: GPLv2
"""
__author__ = "ppizarror"

# importación de librerias
import sys

reload(sys)
# noinspection PyUnresolvedReferences
sys.setdefaultencoding('UTF8')  # @UndefinedVariable

if len(sys.argv) > 1:  # si el argumento existe
    archive = open(sys.argv[1], "r")
    text = []
    for i in archive:
        text.append(i)
        for j in i:
            print unicode(j)
