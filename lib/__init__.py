#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# LIB
# Maneja las funciones principales de korektor
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Configuración de entorno
# noinspection PyUnresolvedReferences
from libpath import *
from libpath import _LIB_CONFIG
from bin import configLoader
from lib import fileManager
from version import __version__  # @UnresolvedImport

# noinspection PyUnresolvedReferences
# noinspection PyProtectedMember
__binconfig = configLoader(_LIB_CONFIG, "lib.ini")
