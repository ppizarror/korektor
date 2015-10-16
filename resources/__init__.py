#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RESOURCES
# Posee todos los recursos binarios utilizados por la aplicación, como imágenes, iconos
# etc.
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías
import os

__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"

# Definición de directorios
# \
DIR_DOC = __actualpath + "doc/"
DIR_ICONS = __actualpath + "icons/"
DIR_IMAGES = __actualpath + "images/"
DIR_LANGS = __actualpath + "langs/"
DIR_RESOURCES = __actualpath

# \..\
DIR_CHANGELOG = DIR_DOC + "changelog/"
DIR_DEV = DIR_DOC + "dev/"
DIR_DOCUMENTATION = DIR_DOC + "documentation"
DIR_HELP = DIR_DOC + "help"
DIR_LICENSE = DIR_DOC + "licence"

# Test
if __name__ == '__main__':
    print DIR_CHANGELOG
    print DIR_DEV
    print DIR_DOC
    print DIR_DOCUMENTATION
    print DIR_HELP
    print DIR_ICONS
    print DIR_IMAGES
    print DIR_LICENSE
    print DIR_RESOURCES
