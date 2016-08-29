#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lib/libpath TEST
Test que prueba el manejo de carpetas del paquete lib/.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Main test
if __name__ == '__main__':
    # Importación de librerías
    from _testpath import *  # @UnusedWildImport
    from lib.libpath import *  # @UnusedWildImport

    print DIR_LIB
