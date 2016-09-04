#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BIN
Posee módulos utilitarios y programas externos.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: OCTUBRE 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías iniciales
from binpath import DIR_BIN, sys
from configloader import ConfigLoader
from _version import __version__
import binpath
import errors

# Configuración de entorno
# noinspection PyProtectedMember
__binconfig = ConfigLoader(binpath._DIR_CONFIG, "bin.ini")
# noinspection PyUnresolvedReferences
sys.setdefaultencoding(__binconfig.get_value("SET_DEFAULT_ENCODING"))  # @UndefinedVariable
# noinspection SpellCheckingInspection
if __binconfig.is_true("DONT_WRITE_BYTECODE"):
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
        from nostdout import NoStdOut
        import langs
        import utils
    except:
        errors.throw(errors.ERROR_IMPORTERRORINTERNAL)
    from colors import clrscr

    clrscr()
    __binconfig.print_parameters()
    print DIR_BIN
    print __version__
