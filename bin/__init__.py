#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# BIN
# Posee módulos utilitarios y programas externos.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: OCTUBRE 2015 - 2016
# Licencia: GPLv2

# Importación de librerías iniciales
from binpath import DIR_BIN, sys
from configLoader import configLoader
from bin._version import __version__
import binpath
import errors

# Configuración de entorno
# noinspection PyProtectedMember
__binconfig = configLoader(binpath._DIR_CONFIG, "bin.ini")
sys.setdefaultencoding(__binconfig.getValue("SET_DEFAULT_ENCODING"))  # @UndefinedVariable
if __binconfig.isTrue("DONT_WRITE_BYTECODE"):
    reload(sys)
    sys.dont_write_bytecode = True

# Module test
if __name__ == '__main__':
    try:
        import mechanize
    except:
        errors.throw(errors.ERROR_IMPORTERRORMECHANIZE)
    try:
        from hashdir import md5file, path_checksum
        from noStdOut import noStdOut
        import langs
        import utils
    except:
        errors.throw(errors.ERROR_IMPORTERRORINTERNAL)
    utils.clrscr()
    __binconfig.printParameters()
    print DIR_BIN
    print __version__
