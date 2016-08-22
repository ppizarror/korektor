#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CONFIG
# Carpeta de configuraciones
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías
import os


# Definición de directorios
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"
DIR_CONFIG = __actualpath

# Test
if __name__ == '__main__':
    print DIR_CONFIG
