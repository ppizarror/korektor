#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# bin/langs TEST
# Test visual al módulo encargado de cargar los idiomas.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Main test
if __name__ == '__main__':
    # Importación de librerías
    from _testpath import *  # @UnusedWildImport
    from bin.langs import *  # @UnusedWildImport
    from bin.langs import _LANG_DIRCONFIG, _LANG_DIRLANGS

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
