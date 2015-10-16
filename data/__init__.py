#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DATA
# En data se incluyen todos los archivos externos lógicos requeridos por korektor para
# corregir tareas. Además en data se almacenaran posibles resultados, listas, información
# externa, etc.
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías
import os

__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"

# Definición de directorios
DIR_DATA = __actualpath

# Test
if __name__ == '__main__':
    print DIR_DATA