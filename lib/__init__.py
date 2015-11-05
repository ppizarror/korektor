#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = "ppizarror"

# LIB
# Maneja las funciones principales de korektor
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: OCTUBRE 2015
# Licencia: GPLv2

# Configuración de entorno
# noinspection PyUnresolvedReferences
from bin import configLoader
# noinspection PyUnresolvedReferences
from libpath import DIR_LIB
import libpath

# noinspection PyProtectedMember
__binconfig = configLoader(libpath._LIB_CONFIG, "lib.ini")
