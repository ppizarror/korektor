#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__ = 'ppizarror'

# UTILS
# Este archivo provee de funciones básicas que son globalmente usadas
#
# Autor: PABLO PIZARRO @ ppizarror.com
# Fecha: SEPTIEMBRE-OCTUBRE 2015
# Licencia: GPLv2

# Importación de librerías de entorno
# noinspection PyUnresolvedReferences
from binpath import *  # @UnusedWildImport
from accents import delAccent, delAccentByOS  # @UnusedImport
import errors

# Importación de librerías de sistema
_IMPORTED = [1, 1]
try:
    from datetime import date
    from random import choice
    from urllib import urlencode
    from urllib2 import urlopen, Request
    import ctypes
    import os  # @Reimport
    import signal
    import string
    import time
    import types
except:
    errors.throw(errors.ERROR_IMPORTSYSTEMERROR)

# Importación de librerías externas
try:
    # noinspection PyUnresolvedReferences
    import WConio
except:
    _IMPORTED[0] = 0
try:
    import mechanize  # @UnusedImport @UnresolvedImport
except:
    _IMPORTED[1] = 0

# Constantes
_CMD_COLORS = {"blue": 0x10,
               "gray": 0x80,
               "green": 0x20,
               "lblue": 0x90,
               "lgray": 0x70,
               "lgreen": 0xA0,
               "lred": 0xC0,
               "purple": 0x50,
               "white": 0xF0,
               "yellow": 0x60,
               "lpurple": 0xD0,
               "lyellow": 0xE0,
               "red": 0x40
               }
_CONSOLE_WRAP = -25
_MSG_LOADINGFILE = "Cargando archivo '{0}' ..."
_MSG_OK = "[OK]"
LINK_PROJECT = "https://github.com/ppizarror/korektor/"
LINK_UPDATES = "http://projects.ppizarror.com/version?product=KR"


def compareVersion(ver1, ver2):
    """
    Se compara entre dos versiones y se retorna el ganador
    :param ver1: Versión actual
    :param ver2: Versión de sistema
    :return: ver1 or ver2
    """
    ver1 = ver1.split(".")
    ver2 = ver2.split(".")
    for i in range(3):
        if int(ver1[i]) > int(ver2[i]):
            return 1
        elif int(ver1[i]) < int(ver2[i]):
            return 2
    return 0


def colorcmd(cmd, color):
    """
    Función que imprime un mensaje con un color
    :param cmd: command
    :param color: Color
    :return: void
    """
    if color in _CMD_COLORS and _IMPORTED[0]:
        color = _CMD_COLORS[color]
        try:
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11),  # @UndefinedVariable
                                                           color)  # @UndefinedVariable
        except:
            pass
        print cmd,
        try:
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11),  # @UndefinedVariable
                                                           0x07)  # @UndefinedVariable
        except:
            pass
    else:
        print cmd,


def delMatrix(matrix):
    """
    Borrar una matriz
    :param matrix: Matriz
    :return: void
    """
    a = len(matrix)
    if a > 0:
        for k in range(a):  # @UnusedVariable
            matrix.pop(0)


def clrscr():
    """
    Limpia la pantalla
    :return: void
    """
    if _IMPORTED[0]:
        try:
            WConio.clrscr()  # @UndefinedVariable
        except:
            pass


def destroyProcess():
    """
    Destruye el proceso del programa
    :return: void
    """
    if os.name == "nt":
        os.system("taskkill /PID " + str(os.getpid()) + " /F")
    else:
        os.kill(os.getpid(), signal.SIGKILL)  # @UndefinedVariable


def generateRandom6():
    """
    Genera un string de 6 carácteres aleatorios
    :return: String
    """
    return ''.join(choice(string.ascii_uppercase) for i in range(6))  # @UnusedVariable


def generateRandom12():
    """
    Genera un string de 12 carácteres aleatorios
    :return: String
    """
    return ''.join(choice(string.ascii_uppercase) for i in range(12))  # @UnusedVariable


def getBetweenTags(html, tagi, tagf):
    """
    Función que retorna un valor entre dos tagss
    :param html: Contenido html
    :param tagi: Tag inicial
    :param tagf: Tag final
    :return: String
    """
    tagi = tagi.strip()
    tagf = tagf.strip()
    try:
        posi = html.index(tagi)
        if ("<" in tagi) and (">" not in tagi):
            c = 1
            while True:
                try:
                    if html[posi + c] == ">":
                        posi += (c + 1)
                        break
                    c += 1
                except:
                    return errors.ERROR_TAG_INITNOTCORRECTENDING
        else:
            posi += len(tagi)
        posf = html.index(tagf, posi)
        return html[posi:posf]
    except:
        return False


def getHour():
    """
    Función que retorna la hora de sistema
    :return: String
    """
    return time.ctime(time.time())[11:16]


def getDate():
    """
    Obtiene la fecha del dia actual
    :return: String dd/mm/aaaa
    """
    fecha = date.today()
    return str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)


def getTerminalSize():
    """
    Devuelve el tamaño de la consola
    :return: tupla
    """
    env = os.environ

    # noinspection PyShadowingNames

    def ioctl_GWINSZ(fd):
        try:
            import fcntl  # @UnresolvedImport
            import termios  # @UnresolvedImport
            import struct  # @UnresolvedImport
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
                                                 '1234'))
        except:
            return
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)  # @UndefinedVariable
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])


# noinspection PyUnresolvedReferences
def getVersion(label, headers):
    """
    Obtener la versión del programa de forma local
    :param label: Label del programa
    :param headers: Web headers
    :return:
    """
    if _IMPORTED[1]:
        browser = Browser()  # @UndefinedVariable
        browser.addHeaders(headers)
        browser.abrirLink(LINK_UPDATES)
        html = browser.getHtml()
    else:
        http_headers = {"User-Agent": headers}
        request_object = Request(LINK_UPDATES, None, http_headers)
        response = urllib2.urlopen(request_object)  # @UndefinedVariable
        html = response.read()
    html = getBetweenTags(getBetweenTags(
        html, "<" + label + ">", "</" + label + ">"), "<version>", "</version>")
    return html.strip()


# noinspection PyUnresolvedReferences
def googleTranslate(text, translate_lang, header, web, source_lang=None):
    """
    Traduce una linea usando el motor de traducciones de google
    :param text: Texto a traducir
    :param translate_lang: Idioma destino
    :param header: Header web
    :param web: Web de traduccion
    :param source_lang: Idioma origen
    :return: String traducido
    """
    if source_lang is None:
        source_lang = 'auto'
    params = urlencode({'client': 't', 'tl': translate_lang,
                        'q': text.encode('utf-8'), 'sl': source_lang})
    http_headers = {"User-Agent": header}
    request_object = Request(web + params, None, http_headers)
    response = urlopen(request_object)
    # @UndefinedVariable
    return json.loads(re.sub(',,,|,,', ',"0",', response.read()))[0][0][0]  # @UndefinedVariable


def isFolder(path, filename):
    """
    Función que retorna true en el caso de que el archivo sea una carpeta, False si no
    :param path: Directorio del archivo
    :param filename: Archivo
    :return: Boolean
    """
    _abspath = (path + "/" + filename).replace("//", "/")

    try:
        os.listdir(_abspath)
        return True
    except:
        return False


def isHiddenFile(filename):
    """
    Función que retorna True en el caso de que el archivo empieza por .
    :param filename: Nombre del archivo
    :return: Boolean
    """
    if isinstance(filename, types.StringType):
        if len(filename) > 0:
            if filename[0] is not ".":
                return False
    return True


def isIn(termino, matriz):
    """
    Función que comprueba si un elemento esta en una matriz (no completamente)
    :param termino: Elemento
    :param matriz: Matriz
    :return: booleano
    """
    if termino is not None:
        for elem in matriz:
            if elem in termino:
                return True
    return False


def isTrue(a):
    """
    Función que devuelve True/False si a es "True" o a es igual a "False"
    :param a: String
    :return: Boolean
    """
    if a == "True":
        return True
    else:
        return False


def isWindows():
    """
    Función que retorna True/False si el sistema operativo cliente es Windows o no
    :return: Boolean
    """
    if os.name == "nt":
        return True
    return False


def makeCallable(function):
    """
    Función que crea una función llamable
    :param function: Puntero a función
    :return: Función
    """
    try:
        function.__name__ = generateRandom6()
    except:
        pass
    return function


def loadFile(archive, lang=_MSG_LOADINGFILE, **kwargs):
    """
    Carga un archivo y retorna una matriz
    :param archive: Archivo
    :param lang: Idioma
    :param kwargs: Parámetros adicionales
    :return: Lista
    """
    if kwargs.get("show_state"):
        print lang.format("(...)" + archive[_CONSOLE_WRAP:].replace("//", "/")).replace("\"", ""),
    try:
        l = list()
        archive = open(archive, "r")
        for i in archive:
            l.append(i.decode('utf-8').strip())
        archive.close()
        if kwargs.get("show_state"):
            print _MSG_OK
    except:
        if kwargs.get("show_state"):
            print "error"
        l = []
    return l


def obtenerFecha():
    """
    Obtiene la fecha del dia actual
    :return: String
    """
    fecha = date.today()
    return str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)


def printBarsConsole(s):
    """
    Función que imprime unas barras en un mensaje
    :param s: String a imprimir
    :return: void
    """
    l = len(s)
    u = ""
    for i in range(l):  # @UnusedVariable
        u+="-"
    print "\n"
    print u
    print s
    print u


def printMatrix(matrix):
    """
    Función que imprime una matriz en pantalla
    :param matrix: Matriz
    :return: void
    """
    for j in matrix:
        for k in j:
            print k,
        print "\n"


def regexCompare(regString, currString, validRegexChars=None):
    """
    Compara dos strings el cual regString posee regex
    :param regString: String regex
    :param currString: String a comparar
    :return: Boolean
    """

    def _comp(i, j):
        """
        Compara los carácteres de regString y currString en las posiciones
        i y j respectivamente
        """
        return regString[i] == currString[j]

    lr = len(regString)
    lc = len(currString)
    if lr > 0 and lc > 0:
        if "*" not in regString:
            return regString == currString
        else:
            i = 0
            j = 0
            while i < lr and j < lc:
                if regString[i] is not "*":
                    if not _comp(i, j):
                        return False
                    i += 1
                    j += 1
                else:
                    if i == lr - 1:
                        break
                    else:
                        i += 1
                        nextc = regString[i]
                    for k in range(0, lc):
                        try:
                            if currString[j + k] == nextc:
                                j += k
                                break
                            else:
                                if validRegexChars is not None:
                                    if currString[j + k] not in validRegexChars:
                                        return False
                        except:
                            return False
                        if j + k >= lc:
                            return False
            return True
    else:
        return False


# noinspection PyShadowingBuiltins
def sortAndUniq(input):  # @ReservedAssignment
    """
    Función que elimina datos repetidos
    :param input: Lista
    :return: Lista modificada
    """
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    output.sort()
    return output


# noinspection PyShadowingNames
def string2list(string, separator):
    """
    Función que divide un string en una lista usando un separador
    :param string: String inicial
    :param separator: Separador
    :return: String
    """
    return string.strip().split(separator)


def sumMatrix(matrix):
    """
    Función que suma lista de listas
    :param matrix: Matrices
    :return: Double
    """
    suma = 0
    try:
        for j in matrix:
            for k in j:
                suma += k
        return suma
    except:
        return -1


# Test
if __name__ == '__main__':
    printBarsConsole("Test funciones varias")
    print string2list("foo bar", " ")
    print getDate()
    print getHour()
    colorcmd("test in purple\n", "purple")
    print generateRandom6()
    print getTerminalSize()
    # noinspection PyTypeChecker
    print loadFile("__init__.ini")
    print sortAndUniq([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 10, 5])
    printBarsConsole("GetBetweenTags Test")
    print getBetweenTags("<player>Username<title></title></player>", "<player>", "</player>")
    print getBetweenTags("<player>Username</player><title>Altername</title>", "<player>", "</player>")
    print getBetweenTags("<player>Username</player><title>Altername</title>", "<title>", "</title>")
    printBarsConsole("Is Hidden File Test")
    print isHiddenFile(".file")
    print isHiddenFile("file")
    print isHiddenFile(1)
    printBarsConsole("Regex Test")
    print regexCompare("korektor test", "korektor test")
    print regexCompare("korektor is nice", "korektor is not nice")
    print regexCompare("*_*", "pablo.pizarro")
    print regexCompare("*regex *", "regex are  korektor")
    print regexCompare("cc3001/tarea2/*_*/Parte1.java", "cc3001/tarea2/pablo_pizarro*/Parte1.java")
    print regexCompare("cc3001/tarea2/*_*/Parte1.java", "cc3001/tarea2/pablo_pizarro*/Parte1.java",
                       "abcdefghijklmnopqrstuvwxyz")
