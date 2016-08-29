#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bin/dumprar TEST
Test interno de rarfile.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Main test
if __name__ == '__main__':

    # Importación de librerías
    from _testpath import *  # @UnusedWildImport
    from bin.dumprar import *  # @UnusedWildImport

    try:
        main()
    except KeyboardInterrupt:
        pass
