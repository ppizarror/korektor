#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "ppizarror"

# ARGUMENTS
# Maneja los argumentos de las aplicaciones.
#
# Autor: PABLO PIZARRO @ github.com/ppizarror
# Fecha: AGOSTO 2015 - 2016
# Licencia: GPLv2

# Importación de librerías
import argparse

# Constantes del programa
_TITLE_AUTHOR = "Autor del software o modulo."
_TITLE_HELP = "Muestra este mensaje de ayuda."
_TITLE_OPTIONALS = "Argumentos opcionales"
_TITLE_POSITIONALS = "Argumentos posicionales"
_TITLE_VERBOSE = "Activa el verbose."
_TITLE_VERSION = "Muestra la version del programa."

def argumentParserFactory(descripcion="", **kwargs):
    """
    Crea un parser de argumentos
    :param descripcion: Descripcion de la bateria de argumentos
    :param kwargs: Parametros opcionales:
        author = Autor del archivo
        show_author = Activa mostrar el comando --author
        title_author = Mensaje de ayuda al mostrar el autor del software
        title_help = Mensaje del comando -h, -help
        title_optionals = Titulo de los argumentos opcionales
        title_positionals = Titulo de los argumentos posicionales
        title_verbose = Mensaje de ayuda al activar o desactivar el verbose
        title_version = Mensaje de ayuda al mostrar la versión del programa
        verbose = Activa el verbose en la línea de comandos
        version = Activa el version en la línea de comandos
    :return: ArgumentParser
    """

    # Langs
    title_author = _TITLE_AUTHOR
    title_help = _TITLE_HELP
    title_optionals = _TITLE_POSITIONALS
    title_positionals = _TITLE_POSITIONALS
    title_verbose = _TITLE_VERBOSE
    title_version = _TITLE_VERSION

    # Estados internos
    from _author import __author__ as author
    show_author = True
    show_author_software = True
    verbose = False
    version = True

    # Se revisan argumentos opcionales
    if "title_positionals" in kwargs:  # Título de los argumentos posicionales
        title_positionals = kwargs["title_positionals"]
    if "title_optional" in kwargs:  # Título de los argumentos opcionales
        title_optionals = kwargs["title_optionals"]
    if "title_author" in kwargs:  # Título del argumento del autor del software/módulo
        title_author = kwargs["title_author"]
    if "title_help" in kwargs:  # Título del argumento de la ayuda
        title_help = kwargs["title_help"]
    if "title_verbose" in kwargs:  # Título del argumento del verbose
        title_verbose = kwargs["title_verbose"]
    if "title_version" in kwargs:  # Título del argumento del version
        title_version = kwargs["title_version"]
    if "version" in kwargs and kwargs["version"]:  # Mostrar comando version
        if str(kwargs["version"]).lower() == "true":
            version = True
        else:
            version = False
    if "verbose" in kwargs:  # Mostrar comando verbose
        if str(kwargs["verbose"]).lower() == "true":
            verbose = True
        else:
            verbose = False
    if "show_author" in kwargs:  # Mostrar el comando author
        if str(kwargs["show_author"]).lower() == "true":
            show_author = True
        else:
            show_author = False
    if "author" in kwargs:  # Definir el autor del software
        author = kwargs["author"]
        show_author_software = False

    # Se crea el parser
    if descripcion != "":
        parser = argparse.ArgumentParser(description=descripcion, add_help=False)
    else:
        parser = argparse.ArgumentParser(add_help=False)
    parser._positionals.title = title_positionals
    parser._optionals.title = title_optionals
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help=title_help)

    # Se agrega el autor del software
    if show_author:
        if show_author_software:
            from _author import __author__ as softwareAuthor
            from _author import __email__
            author = softwareAuthor + " | " + __email__
        else:
            author = "%(prog)s " + author
        parser.add_argument('--author', dest='version', action='version', version=author, help=title_author)

    # Se agrega el verbose
    if verbose:
        parser.add_argument('--verbose', dest='verbose', action='store_true', help=title_verbose)

    # Se agrega la version
    if version:
        from bin._version import __version__
        parser.add_argument('--version', dest='version', action='version', version='%(prog)s ' + __version__, help=title_version)

    return parser
