#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# DATA
# En data se incluyen todos los archivos externos lógicos requeridos por korektor para
# corregir tareas. Además en data se almacenaran posibles resultados, listas, información
# externa, etc.
#
# Autor: PABLO PIZARRO @ ppigithub.com/ppizarrorFecha: OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías
import os
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"

# Definición de directorios
DIR_DATA = __actualpath
DIR_RESULTS = __actualpath + "results/"
DIR_STRUCTURE = __actualpath + "structure/"
DIR_UPLOADS = __actualpath + "uploads/"

# Module test
if __name__ == '__main__':
    print DIR_DATA
    print DIR_RESULTS
    print DIR_STRUCTURE
    print DIR_UPLOADS
