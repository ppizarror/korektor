#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Adminsitra la direccion de directorios de la aplicación
Se pueden incluir todos los directorios salvo bin/.

Autor: PABLO PIZARRO @ pgithub.com/ppizarror
Fecha: ABRIL 2015
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
import os
import sys

# Definición de directorios
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"
DIR_LIB = __actualpath

# Directorios ocultos
LIB_CONFIG = __actualpath + ".config/"

# Se agregan las carpetas actuales al path
reload(sys)
sys.path.append(DIR_LIB)
sys.path.append(__actualpath.replace("/lib/", "/"))
