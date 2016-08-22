#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PLUGINS
# Directorio de plugins
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías
import os


__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"

# Definición de directorios
DIR_PLUGINS = __actualpath

# Test
if __name__ == '__main__':
    print DIR_PLUGINS
