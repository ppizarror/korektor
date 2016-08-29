#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PLUGINS
Directorio de plugins.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: OCTUBRE 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
import os

__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"

# Definición de directorios
DIR_PLUGINS = __actualpath

# Main test
if __name__ == '__main__':
    print DIR_PLUGINS
