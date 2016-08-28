#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# RUN TESTS
# Este módulo corre todos los tests de la aplicación almacenados en la carpeta /test que
# cumplan como la estructura *Test.py.
# Funciona para todos los sistemas operativos.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2016
# Licencia: GPLv2

# Importación de variables
from test._testpath import DIR_TEST_RESULTS, DIR_TEST_RESULTS_LOGGING
from bin.arguments import argumentParserFactory
import datetime
import platform
import subprocess

# Configuracion de argumentos por consola
parser = argumentParserFactory("Ejecuta los tests.")
parser.add_argument('--disable-verbose', dest='verbose', action='store_false', \
                    help='Desactiva el printing en consola.')
parser.add_argument('--dont-save-log', dest='doSaveLogFile', action='store_false', \
                    help='Desactiva el guardado de resultados.')
parser.add_argument('--dont-save-results', dest='doSaveResults', action='store_false', \
                    help='Desactiva el guardado de resultados.')
args = parser.parse_args()

# Se guardan las configuraciones locales
doSaveLogFile = args.doSaveLogFile
doSaveResults = args.doSaveResults
verbose = args.verbose

# Constantes del programa
COMMANDS = "python -m unittest discover test *Test.py"
RESULT_FILE = "results.txt"

# Se ejecuta el llamado al shell
p = subprocess.Popen(COMMANDS, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# Se procesa el resultado
result = str(p.communicate()[1])
result_list = result.split("\n")
rl = len(result_list)

# Datos de los test
fl = "0"
hr = str(datetime.datetime.now())[0:19]
nr = "0"
os = platform.system()
sg = "0.0s"
msgg = hr + " " + os + " "

try:  # Se genera el mensaje de resultados
    if rl == 6:  # Resultado correcto
        msg = result_list[2].replace("\r", "").split(" ")
        nr = msg[1]
        sg = msg[4]
    else:  # Resultado fallido
        msg = result_list[rl - 4].replace("\r", "").split(" ")
        fail = result_list[rl - 2].replace("\r", "").split(" ")[1].replace("(", "").replace(")", "")
        sg = msg[4]
        fl = fail.split("=")[1]
        nr = str(int(msg[1]) - int(fl))
    msgg += sg + " " + nr + " " + fl
except:
    msgg += "ERROR"

# Se agrega el estado de ejecucion al archivo de resultados en RESULT_FILE
if doSaveResults:
    try:
        with open(DIR_TEST_RESULTS + RESULT_FILE, "a") as resfile:
            resfile.write(msgg + "\n")
    except:
        pass

if doSaveLogFile:  # Se guarda el log
    try:
        logname = msgg.replace(":", "-") + ".txt"
        logfile = open(DIR_TEST_RESULTS_LOGGING + logname, "w")
        logfile.write(result)
        logfile.close()
    except:
        pass

if verbose:  # Se imprime el consola el estado final
    print result
