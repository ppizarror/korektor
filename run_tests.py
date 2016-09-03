#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
RUN TESTS
Este módulo corre todos los tests de la aplicación almacenados en la carpeta /test que
cumplan como la estructura *Test.py.
Funciona para todos los sistemas operativos.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from test._testpath import DIR_TEST_RESULTS, DIR_TEST_RESULTS_LOGGING
from bin.arguments import argumentParserFactory
from bin.configLoader import configLoader
from bin.errors import ERROR_MATPLOTLIB_NOT_INSTALLED, ERROR_RUNTESTS_CREATE_PLOT, \
    ERROR_RUNTESTS_SAVE_LOG, ERROR_RUNTESTS_SAVE_RESULTS, st_error
from bin.utils import wipeFile
from config import DIR_CONFIG
import datetime
import math
import platform
import subprocess

# Configuracion de argumentos por consola
parser = argumentParserFactory("Ejecuta todos los tests.")
parser.add_argument('-p', '--create-plot', dest='doPlot', action='store_true', \
                    help='Crea un grafico con todos los resultados en funcion del tiempo')
parser.add_argument('--disable-verbose', dest='verbose', action='store_false', \
                    help='Desactiva el printing en consola.')
parser.add_argument('--dont-save-log', dest='doSaveLogFile', action='store_false', \
                    help='Desactiva el guardado de resultados.')
parser.add_argument('--dont-save-results', dest='doSaveResults', action='store_false', \
                    help='Desactiva el guardado de resultados.')
parser.add_argument('--reset', dest='doReset', action='store_true', \
                    help='Reinicia los resultados a cero.')
args = parser.parse_args()

# Se guardan las configuraciones locales
doPlot = args.doPlot
doReset = args.doReset
doSaveLogFile = args.doSaveLogFile
doSaveResults = args.doSaveResults
verbose = args.verbose

# Constantes del programa
COMMANDS = "python -m unittest discover -s test -p *Test.py"
RESULT_FILE = "results.txt"
RESULT_PLOT_CORRECT = "results-plot.png"
RESULT_PLOT_TIME = "results-plot-time.png"

# Se comprueban comandos críticos
if doReset:
    wipeFile(DIR_TEST_RESULTS + RESULT_FILE)

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

# Mensaje de los resultados
msgg = hr + " " + os + " "

try:  # Se genera el mensaje de resultados
    if rl == 6:  # Resultado correcto
        msg = result_list[2].replace("\r", "").split(" ")
        nr = msg[1]
        sg = msg[4]
    else:  # Resultado fallido
        msg = result_list[rl - 4].replace("\r", "").split(" ")
        fail = result_list[rl - 2].replace("\r", "").split(" ")[1].replace("(", "").replace(")", "").replace(",", "")
        sg = msg[4]
        fl = fail.split("=")[1]
        nr = str(int(msg[1]) - int(fl))
    msgg += sg + " " + nr + " " + fl
except:
    msgg += "ERROR"

# Se agrega el estado de ejecucion al archivo de resultados en RESULT_FILE
if doSaveResults:
    try:
        x = ""
        rsltFile = open(DIR_TEST_RESULTS + RESULT_FILE, "r")
        for line in rsltFile:
            x = line
        tstNumber = str(int(x.split(" ")[0]) + 1)
    except Exception, e:
        tstNumber = "1"
    msgg = tstNumber + " " + msgg
    try:
        with open(DIR_TEST_RESULTS + RESULT_FILE, "a") as resfile:
            resfile.write(msgg + "\n")
    except Exception, e:
        if verbose:
            st_error(ERROR_RUNTESTS_SAVE_RESULTS, False, "run_tests.py", e)

if doSaveLogFile:  # Se guarda el log
    try:
        logname = msgg.replace(":", "-") + ".txt"
        logfile = open(DIR_TEST_RESULTS_LOGGING + logname, "w")
        logfile.write(result)
        logfile.close()
    except Exception, e:
        if verbose:
            st_error(ERROR_RUNTESTS_SAVE_LOG, False, "run_tests.py", e)

if verbose:  # Se imprime el consola el estado final
    print result

if doPlot:  # Se crea un grafico de los resultados en función del tiempo
    _continue = False
    try:
        import matplotlib.pyplot as plt  # @UnresolvedImport @UnusedImport

        _continue = True
    except Exception, e:
        if verbose:
            st_error(ERROR_MATPLOTLIB_NOT_INSTALLED, False, "run_tests.py", e)
    if _continue:
        try:
            # Se obtienen las configuraciones
            plotConfig = configLoader(DIR_CONFIG, "plot.ini")
            dpi_result = int(plotConfig.getValue("DPI", autoNumberify=True))
            max_data = int(plotConfig.getValue("NUMBER_OF_X_DATA", autoNumberify=True))
            max_range_var = float(plotConfig.getValue("MAX_RANGE_VAR", autoNumberify=True))
            y_range_max_coeff = float(plotConfig.getValue("Y_RANGE_COEF_FROM_MAX_VALUE", autoNumberify=True))

            # Se cargan los datos
            vec_time = []
            vec_test = []
            vec_ok = []
            vec_fail = []
            vec_x = []
            testdata = open(DIR_TEST_RESULTS + RESULT_FILE, "r")
            counter = 0
            for ln in testdata:
                if "ERROR" not in ln:
                    nln = str(ln).strip().split(" ")
                    vec_fail.append(int(nln[6]))
                    vec_ok.append(int(nln[5]))
                    vec_test.append(nln[1] + " " + nln[1])
                    vec_time.append(float(nln[4].replace("s", "")))
                    vec_x.append(int(nln[0]))
            testdata.close()
            counter = len(vec_x)

            # Se aplica la restricción de datos
            if counter > max_data:
                vec_fail = vec_fail[counter - max_data:counter]
                vec_ok = vec_ok[counter - max_data:counter]
                vec_test = vec_test[counter - max_data:counter]
                vec_time = vec_time[counter - max_data:counter]
                vec_x = vec_x[counter - max_data:counter]

            # Se calcula el tiempo medio
            tme = 0.0
            nlen = len(vec_x)
            for i in range(0, nlen):
                tme += vec_time[i]
            tme /= nlen

            # Se calcula la desviación típica
            tdesv = 0.0
            for i in range(0, nlen):
                tdesv += pow((vec_time[i] - tme), 2)
            tdesv = math.sqrt(tdesv / nlen)

            # Se eliminan los valores alejados del promedio
            tme_dsv = 0.0
            ttl_dns = 0
            for i in range(0, nlen):
                tm_t = vec_time[i]
                if tm_t < tme * (1 + max_range_var):
                    tme_dsv += tm_t
                    ttl_dns += 1
            tme_dsv /= ttl_dns

            # Se genera el gráfico temporal
            fig, ax = plt.subplots(nrows=1, ncols=1)
            ax.plot(vec_x, vec_time, 'c', label='Tiempo de prueba')
            ax.plot([vec_x[0], vec_x[nlen - 1]], [tme, tme], 'r--', label='Tiempo medio (tme)')
            ax.plot([vec_x[0], vec_x[nlen - 1]], [tme_dsv, tme_dsv], 'b--', label='Tiempo normalizado (tmn)')
            ax.legend()

            # Se crean los label
            ax.set_xlabel("Número del test")
            ax.set_ylabel("Tiempo medio en segundos")
            ax.set_title('Tiempo de las pruebas (tme={0:.3f}s, '.format(tme) + 'tmn=0.334s)')

            # Se ajusta el eje de resultados
            ax.set_xlim([vec_x[0], vec_x[nlen - 1]])
            ax.set_ylim([0, (1 + y_range_max_coeff) * max(vec_time)])

            # Se guarda la figura al archivo
            fig.savefig(DIR_TEST_RESULTS + RESULT_PLOT_TIME, dpi=dpi_result)
            plt.close(fig)

            # Se genera el gráfico de resultados
            fig, ax = plt.subplots(nrows=1, ncols=1)
            ax.plot(vec_x, vec_ok, 'b', label='Pruebas correctas')
            ax.plot(vec_x, vec_fail, 'r', label='Pruebas incorrectas')
            ax.legend()

            # Se crean los label
            ax.set_xlabel("Número del test")
            ax.set_ylabel("Numero de pruebas realizadas")
            ax.set_title("Pruebas correctas / incorrectas")

            # Se ajusta el eje de resultados
            ax.set_xlim([vec_x[0], vec_x[nlen - 1]])
            ax.set_ylim([0, (1 + y_range_max_coeff) * max(max(vec_ok), max(vec_fail))])

            # Se guarda la figura al archivo
            fig.savefig(DIR_TEST_RESULTS + RESULT_PLOT_CORRECT, dpi=dpi_result)
            plt.close(fig)
        except Exception, e:
            if verbose:
                st_error(ERROR_RUNTESTS_CREATE_PLOT, False, "run_tests.py", e)
