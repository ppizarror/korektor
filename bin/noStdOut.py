#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# NOSTDOUT
# Desactiva el standard output de python.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

class noStdOut:
    """Desactiva print"""

    def __init__(self): pass

    def write(self, data): pass

    def read(self, data): pass

    def flush(self): pass

    def close(self): pass
