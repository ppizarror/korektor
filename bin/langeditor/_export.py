#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EXPORT
Permite adaptar un archivo a un texto normal para ser traducido correctamente en google

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: 2014-2015
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
import os
import sys

reload(sys)
# noinspection PyUnresolvedReferences
sys.setdefaultencoding('UTF8')  # @UndefinedVariable

DL = " // "

try:
    namearchive = raw_input("Ingrese el nombre del archivo que desea transformar: ").replace(".txt", "")
    # noinspection PyArgumentEqualDefault
    archivo = open(namearchive + ".txt", "r")
except:
    print "El archivo no existe!"
    exit()

# noinspection PyUnboundLocalVariable
archivo2 = open(namearchive + "_exported" + ".txt", "w")
# noinspection PyUnboundLocalVariable
for linea in archivo:
    linea = linea.strip().split(DL)
    nwlinea = linea[1].replace("|", " ") + "\n"
    archivo2.write("{" + linea[0] + "}\n")
    archivo2.write(nwlinea)
archivo.close()
archivo2.close()
print "Archivo generado correctamente"

try:
    os.remove("_export.pyc")
except:
    pass
