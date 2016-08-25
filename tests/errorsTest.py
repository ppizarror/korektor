#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/errors TEST
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from bin.errors import *  # @UnusedWildImport

# Test
if __name__ == '__main__':
    st_error("Este es un error grave", False)
    st_info("Esta es una información")
    st_warning("Esta es una advertencia")