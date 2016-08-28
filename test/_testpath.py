#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# Adminsitra la direccion de directorios de la aplicación, se pueden incluir todos los
# directorios salvo bin/.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
import os
import sys

# Definición de directorios
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\", "/") + "/"
DIR_BIN = __actualpath.replace("/test/", "/") + "bin/"
DIR_DATA_TEST = __actualpath + ".data_tests/"
DIR_DATA_TEST_PRIVATE = __actualpath + ".data_tests_private/"
DIR_TESTS = __actualpath
DIR_TEST_RESULTS = __actualpath + ".results/"
DIR_TEST_RESULTS_LOGGING = __actualpath + ".results/log/"

# Se agregan las carpetas actuales al path
reload(sys)
sys.path.append(DIR_TESTS)
sys.path.append(__actualpath.replace("/test/", "/"))

# Main test
if __name__ == '__main__':
    print DIR_BIN
    print DIR_DATA_TEST
    print DIR_DATA_TEST_PRIVATE
    print DIR_TESTS
    print DIR_TEST_RESULTS
    print DIR_TEST_RESULTS_LOGGING
