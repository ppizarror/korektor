#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# BIN
# Posee módulos utilitarios y programas externos
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías iniciales
from binpath import DIR_BIN, sys
import binpath
from configLoader import configLoader
import errors

# Configuración de entorno
# noinspection PyProtectedMember
__binconfig = configLoader(binpath._DIR_CONFIG, "bin.ini")
sys.setdefaultencoding(__binconfig.getValue("SET_DEFAULT_ENCODING"))  # @UndefinedVariable
if __binconfig.isTrue("DONT_WRITE_BYTECODE"):
    reload(sys)
    sys.dont_write_bytecode = True

# Test
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
