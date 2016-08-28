#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# bin/binpath TEST
# Test del manejo de carpetas en el paquete bin.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Main test
if __name__ == '__main__':

    # Importación de librerías
    from _testpath import *  # @UnusedWildImport
    from bin.binpath import _LANG_DIRCONFIG, DIR_BIN, _LANG_DIRLANGS  # @Reimport

    print DIR_BIN
    print _LANG_DIRCONFIG
    print _LANG_DIRLANGS
