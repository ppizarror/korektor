#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# BINPATH
# Adminsitra el path de /bin.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: OCTUBRE 2015 - 2016
# Licencia: GPLv2

# Importación de librerías
import os
import sys

# Definición de directorios
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"
DIR_BIN = __actualpath

# Directorios ocultos
_DIR_CONFIG = __actualpath + ".config/"
_LANG_DIRCONFIG = __actualpath + "langeditor/config/"
_LANG_DIRLANGS = __actualpath.replace("/bin/", "/resources/langs/")

reload(sys)
sys.path.append(DIR_BIN)
sys.path.append(DIR_BIN + "/easyprocess/")
sys.path.append(DIR_BIN + "/mechanize/")
sys.path.append(DIR_BIN + "/pyunpack/")
sys.path.append(DIR_BIN + "/wconio/")
