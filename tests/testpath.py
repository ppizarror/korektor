#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# Adminsitra la direccion de directorios de la aplicación
# Se pueden incluir todos los directorios salvo bin/
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
import os
import sys

# Definición de directorios
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"
DIR_DATA_TEST = __actualpath + ".data_tests/"
DIR_DATA_TEST_PRIVATE = __actualpath + ".data_tests_private/"
DIR_TESTS = __actualpath
DIR_BIN = __actualpath.replace("/tests/", "/") + "bin/"

# Se agregan las carpetas actuales al path
reload(sys)
sys.path.append(DIR_TESTS)
sys.path.append(__actualpath.replace("/tests/", "/"))

# Test
if __name__ == '__main__':
    print DIR_BIN
    print DIR_DATA_TEST
    print DIR_DATA_TEST_PRIVATE
    print DIR_TESTS
