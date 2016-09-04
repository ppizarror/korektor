#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
UTILS
Este archivo provee de funciones básicas que son globalmente usadas.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: SEPTIEMBRE-OCTUBRE 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías de entorno
# noinspection PyUnresolvedReferences
from binpath import *  # @UnusedWildImport
# noinspection PyUnresolvedReferences
from accents import delAccentByOS  # @UnusedImport
from browser import Browser
from kwargsutils import kwargIsTrueParam
import errors

# Importación de librerías de sistema
_IMPORTED = [1]
try:
    from datetime import date
    from random import choice
    from urllib import urlencode
    from urllib2 import urlopen, Request
    import os  # @Reimport
    import signal
    import string
    import time
    import types
except:
    errors.throw(errors.ERROR_IMPORTSYSTEMERROR)

# Importación de librerías externas
try:
    import mechanize  # @UnusedImport @UnresolvedImport
except:
    _IMPORTED[0] = 0

# Constantes
_CONSOLE_WRAP = -25
_MSG_LOADINGFILE = "Cargando archivo '{0}' ..."
_MSG_OK = "[OK]"
_REGEX_CHARS_LIST = ["*", "#"]


def appendListToList(origin, l):
    """
    Añade los elementos de la lista l a la lista origin.

    :param origin: Lista a añadir elementos
    :type origin: list
    :param l: Lista con elementos a ser agregados
    :type l: list

    :return: void
    :type: None
    """
    for i in l:
        origin.append(i)


def compareVersion(ver1, ver2):
    """
    Se compara entre dos versiones y se retorna el ganador.

    :param ver1: Versión actual
    :type ver1: str
    :param ver2: Versión de sistema
    :type ver2: str

    :return: ver1 or ver2
    :rtype: int
    """
    ver1 = ver1.split(".")
    ver2 = ver2.split(".")
    for i in range(3):
        if int(ver1[i]) > int(ver2[i]):
            return 1
        elif int(ver1[i]) < int(ver2[i]):
            return 2
    return 0


def convertToNumber(s):
    """
    Función que convierte un objeto a diversos tipos de números.

    :param s: String a convertir
    :type s: object

    :return: Número convertido
    :rtype: object
    """
    try:
        s = str(s)
    except:
        return s
    if s.isdigit():  # Es un entero
        return int(s)
    else:
        if "." in s and s.replace(".", "").isdigit():  # Es un flotante
            return float(s)
        else:
            try:  # Es un hexadecimal
                return int(s, 16)
            except ValueError:
                pass
    return s


def delMatrix(matrix):
    """
    Borrar una matriz.

    :param matrix: Matriz
    :type matrix: list

    :return: void
    :rtype: None
    """
    a = len(matrix)
    if a > 0:
        for k in range(a):  # @UnusedVariable
            matrix.pop(0)


# noinspection PyUnresolvedReferences
def destroyProcess():
    """
    Destruye el proceso del programa.

    :return: void
    :rtype: None
    """
    if os.name == "nt":
        os.system("taskkill /PID " + str(os.getpid()) + " /F")
    else:
        os.kill(os.getpid(), signal.SIGKILL)  # @UndefinedVariable


def equalLists(list1, list2):
    """
    Comprueba si dos listas son idénticas en elementos.

    :param list1: Lista 1
    :type list1: list
    :param list2: Lista 2
    :type list2: list

    :return: Booleano indicando comparación
    :rtype: bool
    """
    if len(list1) != len(list2):
        return False
    else:
        for i in range(0, len(list1)):
            if list1[i] != list2[i]:
                return False
        return True


# noinspection PyUnusedLocal
def generateRandom6():
    """
    Genera un string de 6 caracteres aleatorios.

    :return: String
    :rtype: str
    """
    return ''.join(choice(string.ascii_uppercase) for i in range(6))  # @UnusedVariable


# noinspection PyUnusedLocal
def generateRandom12():
    """
    Genera un string de 12 caracteres aleatorios.

    :return: String
    :rtype: str
    """
    return ''.join(choice(string.ascii_uppercase) for i in range(12))  # @UnusedVariable


# noinspection SpellCheckingInspection
def getBetweenTags(html, tagi, tagf):
    """
    Función que retorna un valor entre dos tags.

    :param html: Contenido html
    :type html: str
    :param tagi: Tag inicial
    :type tagi: str
    :param tagf: Tag final
    :type tagf: str

    :return: String entre dos tags
    :rtype: str
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
    Función que retorna la hora de sistema.

    :return: String con la hora del sistema
    :rtype: str
    """
    return time.ctime(time.time())[11:16]


# noinspection SpellCheckingInspection
def getDate():
    """
    Obtiene la fecha del dia actual.

    :return: String dd/mm/aaaa
    :rtype: str
    """
    fecha = date.today()
    return str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)


def getTerminalSize():
    """
    Devuelve el tamaño de la consola.

    :return: tupla
    :rtype: tuple
    """
    env = os.environ

    # noinspection PyShadowingNames,PyUnresolvedReferences

    def ioctl_GWINSZ(fd):
        """
        Entrega el tamaño de la consola
        :param fd: Numero de STD
        :type fd: int

        :return: buffer
        :rtype: object
        """
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


# noinspection PyUnresolvedReferences,PyIncorrectDocstring
def getVersion(label, headers, linkUpdates):
    """
    Obtener la versión del programa de forma local.

    :param label: Label del programa
    :type label: str
    :param headers: Web headers
    :type headers: str

    :return: String con la versión del programa según la web
    :rtype: str
    """
    if _IMPORTED[0]:
        browser = Browser()  # @UndefinedVariable
        browser.addHeaders(headers)
        browser.abrirLink(linkUpdates)
        html = browser.getHtml()
    else:
        http_headers = {"User-Agent": headers}
        request_object = Request(linkUpdates, None, http_headers)
        response = urllib2.urlopen(request_object)  # @UndefinedVariable
        html = response.read()
    html = getBetweenTags(getBetweenTags(
        html, "<" + label + ">", "</" + label + ">"), "<version>", "</version>")
    return html.strip()


# noinspection PyUnresolvedReferences
def googleTranslate(text, translate_lang, header, web, source_lang=None):
    """
    Traduce una linea usando el motor de traducciones de google.

    :param text: Texto a traducir
    :type text: str
    :param translate_lang: Idioma destino
    :type translate_lang: str
    :param header: Header web
    :type header: str
    :param web: Web de traducción
    :type web: str
    :param source_lang: Idioma origen
    :type source_lang: str

    :return: String traducido
    :rtype: str
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
    Función que retorna true en el caso de que el archivo sea una carpeta, False si no.

    :param path: Directorio del archivo
    :type path: str
    :param filename: Archivo
    :type filename: str

    :return: Booleano indicando pertenencia
    :rtype: bool
    """
    try:
        _abspath = (path + "/" + filename).replace("//", "/").replace("//", "/")
        os.listdir(_abspath)
        return True
    except:
        return False


# noinspection PyTypeChecker,PyUnresolvedReferences
def isHiddenFile(filename):
    """
    Función que retorna True en el caso de que el archivo empieza por un punto.

    :param filename: Nombre del archivo
    :type filename: object

    :return: Booleano indicando pertenencia
    :rtype: bool
    """
    if isinstance(filename, types.StringType):
        if len(filename) > 0:
            if filename[0] is not ".":
                return False
    return True


def isIn(termino, matriz):
    """
    Función que comprueba si un elemento esta en una matriz (no completamente).

    :param termino: Elemento
    :type termino: object
    :param matriz: Matriz
    :type matriz: list

    :return: Booleano indicando pertenencia
    :rtype: bool
    """
    if termino is not None:
        for elem in matriz:
            if elem in termino:
                return True
    return False


def isTrue(a):
    """
    Función que devuelve True/False si a es "True" o a es igual a "False".

    :param a: String
    :type a: str

    :return: Booleano indicando igualdad
    :rtype: bool
    """
    if a == "True":
        return True
    else:
        return False


def makeCallable(function):
    """
    Función que crea una función llamable.

    :param function: Puntero a función
    :type function: object

    :return: Función misma con un nombre callable
    :rtype: object
    """
    try:
        function.__name__ = generateRandom6()
    except:
        pass
    return function


def numberOfSublists(l):
    """
    Retorna el numero de sublistas que contiene una lista.

    :param l: Lista a calcular
    :type l: list

    :return: Número de sublistas
    :rtype: int
    """
    count = 0
    for i in l:
        if isinstance(i, list):
            count = count + 1 + numberOfSublists(i)
    return count


def loadFile(archive, lang=_MSG_LOADINGFILE, **kwargs):
    """
    Carga un archivo y retorna una lista con las líneas del archivo.

    Keywords:
        - show_state (bool) = Muestra el estado de ejecución en la pantalla

    :param archive: Archivo
    :type archive: str
    :param lang: Idioma
    :type lang: str
    :param kwargs: Parámetros adicionales
    :type kwargs: list

    :return: Lista con las líneas del archivo
    :rtype: list
    """
    show_state = kwargIsTrueParam(kwargs, "show_state")
    if show_state:
        print lang.format("(...)" + archive[_CONSOLE_WRAP:].replace("//", "/")).replace("\"", ""),
    try:
        l = list()
        archive = open(archive, "r")
        for i in archive:
            l.append(i.decode('utf-8').strip())
        archive.close()
        if show_state:
            print _MSG_OK
    except:
        if show_state:
            print "error"
        l = []
    return l


def obtenerFecha():
    """
    Obtiene la fecha del dia actual.

    :return: Fecha en formato dd/mm/aa
    :rtype: str
    """
    fecha = date.today()
    return str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)


def printBarsConsole(s, tabs=0):
    """
    Función que imprime unas barras en un mensaje.

    :param s: String a imprimir
    :type s: str
    :param tabs: Número de tabs a imprimir a la izquierda
    :type tabs: int

    :return: void
    :rtype: None
    """
    l = len(s)
    u = "{0}".format("\t" * tabs)
    for i in range(l):  # @UnusedVariable
        u += "-"
    print u
    print "{0} {1}".format("\t" * tabs, delAccentByOS(s))
    print u


def printMatrix(matrix):
    """
    Función que imprime una matriz en pantalla.

    :param matrix: Matriz
    :type matrix: list

    :return: void
    :rtype: None
    """
    for j in matrix:
        for k in j:
            print k,
        print "\n"


def printHierachyBoolList(lst, level=0):
    """
    Función que imprime una lista booleana de jerarquía.
    Obtenida desde: http://stackoverflow.com/questions/30521991/

    :param lst: Lista de jerarquía booleana de jerarquía
    :type lst: list
    :param level: Nivel de profundidad
    :type level: int

    :return: void
    :rtype: None
    """
    print('  ' * (level - 1) + '+-' * (level > 0) + str(lst[0]))
    for l in lst[1:]:
        if type(l) is list:
            printHierachyBoolList(l, level + 1)
        else:
            print('  ' * level + '+-' + str(l))


def printHierachyList(lst, level, tabsLeft):
    """
    Función que imprime una lista de jerarquía.
    Obtenida desde: http://stackoverflow.com/questions/30521991/

    :param lst: Lista de jerarquía
    :type lst: list
    :param level: Nivel de profundidad
    :type level: int
    :param tabsLeft: Número de tabs a la izquierda
    :type tabsLeft: int

    :return: void
    :rtype: None
    """
    print('\t' * tabsLeft + '    ' * (level - 1) + '+---' * (level > 0) + lst[0])
    for l in lst[1:]:
        if type(l) is list:
            printHierachyList(l, level + 1, tabsLeft)
        else:
            print('\t' * tabsLeft + '    ' * level + '+---' + l)


# noinspection SpellCheckingInspection
def regexCompare(regString, currString, validRegexChars=None, regexChars=_REGEX_CHARS_LIST, **kwargs):
    """
    Compara dos strings el cual regString posee regex.

    Keywords:
        - case_insensitive (bool) = Si este parámetro es True la comparación se hace ignorando el tipo de letra.

    :param regString: String regex
    :type regString: str, unicode
    :param currString: String a comparar
    :type currString: str, unicode
    :param validRegexChars: String de caracteres válidos
    :type validRegexChars: str, unicode
    :param regexChars: Lista de caracteres inválidos
    :type regexChars: list
    :param kwargs: Keywords
    :type kwargs: dict

    :return: Booleano indicando resultado de la comparación
    :rtype: bool
    """

    def _charListNotIn(charList, word):
        """
        Comprueba que una lista de caracteres no esté en una palabra <word>.

        :param charList: Lista de caracteres
        :type charList: list
        :param word: Palabra a analizar
        :type word: str, unicode

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        for cha in charList:
            if cha in word:
                return False
        return True

    # Se tratan los strings
    regString = str(regString)
    currString = str(currString)

    # Se obtienen parámetros de ejecución
    if kwargIsTrueParam(kwargs, "case_insensitive"):
        regString = regString.lower()
        currString = currString.lower()

    if validRegexChars is not None:
        try:
            validRegexChars = str(validRegexChars)
        except:
            print validRegexChars

        # Se comprueba que todos los caracteres de currString sean válidos
        for ch in list(currString):
            if ch not in validRegexChars:
                return False

    # Se eliminan # o * seguidos
    regStringBuilder = ""
    for regxlc in regString:
        if regxlc in regexChars:
            if not regStringBuilder[-1:] in regexChars:
                regStringBuilder += regxlc
        else:
            regStringBuilder += regxlc
    regString = regStringBuilder

    # Largos de los strings
    lr = len(regString)
    lc = len(currString)

    # Si ambos strings existen
    if lr > 0 and lc > 0:

        # Si no hay elementos regex entonces se comparan como si fuesen simples strings
        if _charListNotIn(regexChars, regString):
            return regString == currString

        # Si hay regex
        else:

            # Se inicializan los punteros walk al principio de cada string
            i = 0
            j = 0

            # Se recorren ambos indices comprobando uno a uno (i con j), si hay un regex j salta hasta que se iguale con
            # i.
            while i < lr and j < lc:

                # Si el carácter en regString no es un carácter regex
                if regString[i] not in regexChars:

                    # Si difieren i y j entonces los caracteres son falsos
                    if not regString[i] == currString[j]:
                        return False

                    # Si no difieren ambos avanzan en 1 posición
                    i += 1
                    j += 1

                # Si el carácter es un regex
                else:

                    # Lista de caracteres que continúan
                    nextl = []
                    ni = i + 1

                    # Si es el carácter final entonces retorna True
                    if i == lr - 1:
                        return True

                    # Si no es un carácter final entonces se agregan los caracteres de regString que continúan a nextl
                    else:
                        for p in regString[i + 1:lr]:
                            if p not in regexChars:
                                nextl.append(p)
                            else:
                                break
                        lnextl = len(nextl)

                    # Si lo que queda de currString no alcanza para hacer el match con la lista de caracteres entonces
                    # los strings son diferentes y la función retorna False.
                    if (lc - j) < lnextl:
                        return False

                    # Se recorre cada carácter de currString hasta que se completa toda la lista de nextl, si se pasa
                    # entonces las listas difieren y la función retorna False.
                    while True:

                        # Se recorre cada carácter de nextl y se comprueba igualdad, si se cumplen todas entonces el
                        # puntero j se actualiza y se sigue con la comprobación
                        areEquals = True
                        for m in range(0, lnextl):

                            # Si los caracteres difieren entonces no son iguales
                            if currString[j + m] != nextl[m]:
                                j += m
                                i += m
                                areEquals = False
                                break

                        # Si eran iguales
                        if areEquals:
                            if j + m == lc - 1 and ni + m == lr - 1:
                                return True
                            else:
                                j += 1
                                i += 2
                                break

                        # Si no eran iguales se comprueba que no se haya pasado el límite del string
                        else:

                            # Si no se avanzó en la búsqueda de lnextl entonces se avanza en 1 el puntero j
                            if m == 0:
                                j += 1

                            # Si se salió del string o el resto de currString no alcanza para comprobar igualdad retorna
                            # False.
                            if j + lnextl > lc or j >= lc:
                                return False

            # Si pasó el while de i-j entonces los strings son idénticos
            return True

    # Si son strings vacíos
    elif lr == lc == 0:
        return True

    # Los strings son distintos por lo que retorna False
    else:
        return False


# noinspection PyShadowingBuiltins
def sortAndUniq(input):  # @ReservedAssignment
    """
    Función que elimina datos repetidos.

    :param input: Lista
    :type input: list

    :return: Lista modificada
    :rtype: list
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
    Función que divide un string en una lista usando un separador.

    :param string: String inicial
    :type string: str
    :param separator: Separador
    :type separator: str

    :return: Lista proveniente de la separación del string
    :rtype: list
    """
    return string.strip().split(separator)


def sumMatrix(matrix):
    """
    Función que suma lista de listas.

    :param matrix: Matrices
    :type matrix: list

    :return: Valor de la suma
    :rtype: float
    """
    suma = 0.0
    try:
        for j in matrix:
            for k in j:
                suma += k
        return suma
    except:
        return -1


def wipeFile(filename):
    """
    Elimina todo el contenido del archivo pasado por argumento.

    :param filename: Ubicación del archivo
    :type filename: str

    :return: void
    :rtype: None
    """
    try:
        open(filename, 'w').close()
    except:
        pass
