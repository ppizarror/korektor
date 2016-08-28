#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# RUN TESTS
# Este módulo corre todos los tests de la aplicación almacenados en la carpeta /test que
# cumplan como la estructura *Test.py.
# Funciona para todos los sistemas operativos.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de variables
import subprocess

# Constantes del programa
COMMANDS = "python -m unittest discover test *Test.py"

# Se ejecuta el llamado al shell
p = subprocess.Popen(COMMANDS, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# Se procesa el resultado
result = str(p.communicate()[1])
result_list = result.split("\n")
print result_list

# Resultado correcto
if len(result_list) == 6:
    pass

# Resultado fallido
else:
    pass

# Se guarda el resultado en test/.results/results.txt
pass
