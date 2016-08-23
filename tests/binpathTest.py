#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/binpath TEST
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from bin.binpath import _LANG_DIRCONFIG, DIR_BIN, _LANG_DIRLANGS

if __name__ == '__main__':
    print DIR_BIN
    print _LANG_DIRCONFIG
    print _LANG_DIRLANGS
