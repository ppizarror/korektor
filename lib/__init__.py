#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# LIB
# Maneja las funciones principales de korektor.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Configuración de entorno
# noinspection PyUnresolvedReferences
from libpath import *
from bin import configLoader, __version__
from lib import fileManager

# noinspection PyUnresolvedReferences
# noinspection PyProtectedMember
__binconfig = configLoader(LIB_CONFIG, "lib.ini")
