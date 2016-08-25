#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/configLoader TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from bin.configLoader import *  # @UnusedWildImport

# Test
if __name__ == '__main__':
    binconfig = configLoader(DIR_BIN + ".config/", "bin.ini", verbose=True)
    binconfig.isTrue("DONT_WRITE_BYTECODE")
    binconfig.getParameters()
    binconfig.printParameters()
    binconfig.setParameter("PARAM1", "VALUE1")
    binconfig.setParameter("PARAM2", "VALUE2")
    binconfig.setParameter("PARAM3", "VALUE3")
    binconfig.setParameter("SET_DEFAULT_ENCODING", "W-850")
    binconfig.printParameters()
    # binconfig.export(False, "test.ini")
    print binconfig.getValue(binconfig.getParameters()[1])
    print binconfig.getValue("DONT_WRITE_BYTECODE")
    print binconfig.getValue("SET_DEFAULT_ENCODING")
