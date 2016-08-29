#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DATA
En data se incluyen todos los archivos externos lógicos requeridos por korektor para
corregir tareas. Además en data se almacenaran posibles resultados, listas, información
externa, etc.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: OCTUBRE 2015
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
import os

__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"

# Constantes
DIR_STRUCTURE_FOLDERNAME = "structure/"

# Definición de directorios
DIR_DATA = __actualpath
DIR_RESULTS = __actualpath + "results/"
DIR_STRUCTURE = __actualpath + DIR_STRUCTURE_FOLDERNAME
DIR_UPLOADS = __actualpath + "uploads/"

# Main test
if __name__ == '__main__':
    print DIR_DATA
    print DIR_RESULTS
    print DIR_STRUCTURE
    print DIR_UPLOADS
