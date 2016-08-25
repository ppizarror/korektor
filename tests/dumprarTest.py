#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/dumprar TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
from _testpath import *  # @UnusedWildImport
from bin.dumprar import *  # @UnusedWildImport

# Test
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass