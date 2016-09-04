#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bin/Langs TEST
Test visual al módulo encargado de cargar los idiomas.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Main test
if __name__ == '__main__':
    # Importación de librerías
    # noinspection PyUnresolvedReferences
    from _testpath import *  # @UnusedWildImport
    from bin.langs import *  # @UnusedWildImport
    from bin.langs import _LANG_DIRCONFIG, _LANG_DIRLANGS

    print _LANG_DIRCONFIG
    print _LANG_DIRLANGS
    lang = LangLoader("TEST", verbose=True)
    langconfig.print_parameters()
    print langconfig.get_parameters()
    langavaiable.print_parameters()
    langtranslateconfig.print_parameters()
    print langselfconfig.get_parameters()
    print langselfconfig.is_true("TRANSLATIONS")
    print lang.get(10)
    print lang.get(12)
    # noinspection PyTypeChecker
    print lang.get("a")
    # print lang.translate(11, "eng")
    lang.print_all()
    print lang.get(14, 1, 2, 3)
    print lang.get(14, 1, 2, 3, noformat=True)
    print lang.get(12, "pablo")
    print lang.get(13, "pablo", "pizarro")
