#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/binpath TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Test
if __name__ == '__main__':

    # Importación de librerías
    from _testpath import *  # @UnusedWildImport
    from bin.binpath import _LANG_DIRCONFIG, DIR_BIN, _LANG_DIRLANGS  # @Reimport

    print DIR_BIN
    print _LANG_DIRCONFIG
    print _LANG_DIRLANGS
