#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LIB
Maneja las funciones principales de korektor.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: OCTUBRE 2015
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Configuración de entorno
# noinspection PyUnresolvedReferences
from libpath import *
# noinspection PyUnresolvedReferences
from bin import ConfigLoader, __version__
# noinspection PyUnresolvedReferences
from lib import filemanager

# noinspection PyUnresolvedReferences
# noinspection PyProtectedMember
__binconfig = ConfigLoader(LIB_CONFIG, "lib.ini")
