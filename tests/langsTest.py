#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# bin/langs TEST
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de librerías
if __name__ == '__main__':
    from testpath import *  # @UnusedWildImport
from bin.langs import *  # @UnusedWildImport
from bin.langs import _LANG_DIRCONFIG, _LANG_DIRLANGS

# Test
if __name__ == '__main__':
    print _LANG_DIRCONFIG
    print _LANG_DIRLANGS
    lang = langLoader("TEST", verbose=True)
    langconfig.printParameters()
    print langconfig.getParameters()
    langavaiable.printParameters()
    langtranslateconfig.printParameters()
    print langselfconfig.getParameters()
    print langselfconfig.isTrue("TRANSLATIONS")
    print lang.get(10)
    print lang.get(12)
    print lang.get("a")
    # print lang.translate(11, "eng")
    lang.printAll()
    print lang.get(14, 1, 2, 3)
    print lang.get(14, 1, 2, 3, noformat=True)
    print lang.get(12, "pablo")
    print lang.get(13, "pablo", "pizarro")