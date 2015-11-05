#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# BINPATH
# Adminsitra el path de /bin
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
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
sys.path.append(DIR_BIN + "/mechanize/")
sys.path.append(DIR_BIN + "/wconio/")

# Test
if __name__ == '__main__':
    print DIR_BIN
    print _LANG_DIRCONFIG
    print _LANG_DIRLANGS
