#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ARGUMENTS
Maneja los argumentos de las aplicaciones.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: AGOSTO 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from argparse import ArgumentParser, SUPPRESS
from accents import del_accent_by_os
from kwargsutils import *  # @UnusedWildImport

# Constantes del programa
_TITLE_AUTHOR = "Autor del software o módulo."
_TITLE_HELP = "Muestra este mensaje de ayuda."
_TITLE_OPTIONALS = "Argumentos opcionales"
_TITLE_POSITIONALS = "Argumentos posicionales"
_TITLE_SKIPPED = "Activa los tests pesados"
_TITLE_VERBOSE = "Activa el verbose."
_TITLE_VERSION = "Muestra la versión del programa."


# noinspection PyTypeChecker,PyProtectedMember
def argument_parser_factory(descripcion="", **kwargs):
    # noinspection SpellCheckingInspection
    """
    Crea un parser de argumentos para ser tratados en consola.

    Keywords booleanos:
        - author = Autor del archivo.
        - enable_skipped_test = Mostrar el comando --enable-skipped para activar los tests pesados.
        - show_author = Activa mostrar el comando --author.
        - verbose = Activa el verbose en la línea de comandos.
        - version = Activa el version en la línea de comandos.

    Keywords strings:
        - title_author = Mensaje de ayuda al mostrar el autor del software.
        - title_help = Mensaje del comando -h, -help.
        - title_optionals = Titulo de los argumentos opcionales.
        - title_positionals = Titulo de los argumentos posicionales.
        - title_verbose = Mensaje de ayuda al activar o desactivar el verbose.
        - title_skipped_test = Mensaje de ayuda de la función --enable-skipped
        - title_version = Mensaje de ayuda al mostrar la versión del programa.

    :param descripcion: Descripción de la batería de argumentos
    :type descripcion: str
    :param kwargs: Keywords
    :type kwargs: list
    :return: Objeto ArgumentParser
    :rtype: ArgumentParser
    """

    # Estados internos
    from _author import __author__ as author
    show_author_software = True

    # Se revisan argumentos opcionales, str
    title_positionals = del_accent_by_os(kwarg_get_value(kwargs, "title_positionals", _TITLE_POSITIONALS))
    title_optionals = del_accent_by_os(kwarg_get_value(kwargs, "title_optionals", _TITLE_OPTIONALS))
    title_author = del_accent_by_os(kwarg_get_value(kwargs, "title_author", _TITLE_AUTHOR))
    title_help = del_accent_by_os(kwarg_get_value(kwargs, "title_help", _TITLE_HELP))
    title_skipped = del_accent_by_os(kwarg_get_value(kwargs, "title_skipped", _TITLE_SKIPPED))
    title_verbose = del_accent_by_os(kwarg_get_value(kwargs, "title_verbose", _TITLE_VERBOSE))
    title_version = del_accent_by_os(kwarg_get_value(kwargs, "title_version", _TITLE_VERSION))

    # Argumentos booleanos
    skipped = kwarg_is_true_param(kwargs, "enable_skipped_test")  # Mostrar el comando enable-skipped
    version = kwarg_is_true_param(kwargs, "version")  # Mostrar comando version
    verbose = kwarg_is_true_param(kwargs, "verbose")  # Mostrar el comando verbose
    show_author = kwarg_is_true_param(kwargs, "show_author")  # Mostrar el comando author

    # Definir el autor del software
    if "author" in kwargs:
        author = del_accent_by_os(kwargs["author"])
        show_author_software = False

    # Se crea el parser
    if descripcion != "":
        parser = ArgumentParser(description=del_accent_by_os(descripcion), add_help=False)
    else:
        parser = ArgumentParser(add_help=False)
    parser._positionals.title = title_positionals
    parser._optionals.title = title_optionals
    parser.add_argument('-h', '--help', action='help', default=SUPPRESS, help=title_help)

    # Se agrega el autor del software
    if show_author:
        if show_author_software:
            from _author import __author__ as software_author
            from _author import __email__
            author = software_author + " | " + __email__
        else:
            author = "%(prog)s " + author
        parser.add_argument('--author', dest='version', action='version', version=del_accent_by_os(author),
                            help=title_author)

    # Se agrega el skipped
    if skipped:
        parser.add_argument('-skp', '--enable-skipped', dest='enableHeavyTest', action='store_false',
                            help=title_skipped)

    # Se agrega el verbose
    if verbose:
        parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help=title_verbose)

    # Se agrega la version
    if version:
        from bin._version import __version__
        parser.add_argument('--version', dest='version', action='version', version='%(prog)s ' + __version__,
                            help=title_version)

    return parser
