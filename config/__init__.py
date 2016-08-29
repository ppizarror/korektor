#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CONFIG
Carpeta de configuraciones.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: OCTUBRE 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
import os

# Definición de directorios
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"
DIR_CONFIG = __actualpath

# Module test
if __name__ == '__main__':
    print DIR_CONFIG
