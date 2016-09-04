#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BROWSER
Sencillo navegador web.

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: ABRIL-OCTUBRE 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    from binpath import *  # @UnusedWildImport
import cookielib
import htmlentitydefs
import re
import errors
import mechanize


# Funciones de clase
# noinspection SpellCheckingInspection
def unescape(text):
    """
    Reemplaza los caracteres html.

    :param text: HTML
    :type text: str

    :return: HTML sin caracteres
    :rtype: str
    """

    # noinspection PyShadowingNames,PyUnresolvedReferences
    def fixup(m):
        """
        Elimina caracteres no unicode en un string.

        :param m: String a tratar
        :type m: str

        :return: String con caracteres tratados
        :rtype: str
        """
        text = m.group(0)
        if text[:2] == "&#":
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text

    return re.sub('&#?\w+;', fixup, text)


class Browser:
    """
    Navegador web.
    """

    def __init__(self):
        """
        Función constructora.

        :return: void
        :rtype: None
        """
        self.br = mechanize.Browser()  # navegador
        self.cookies = cookielib.LWPCookieJar()  # cookies
        self.br.set_cookiejar(self.cookies)
        self.opened = False  # define si una páginas se ha cargado
        self.selectedForm = False  # define si se ha definido un formulario

        # Opciones del navegador
        self.br.set_handle_equiv(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_refresh(False)
        self.br.set_handle_robots(False)
        # noinspection PyProtectedMember
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    def abrir_link(self, web):
        """
        Ingresar a una dirección web.

        :param web: Link a web
        :type web: str

        :return: void
        :rtype: None
        """
        try:  # Intento cargar la web
            self.br.open(web)
            self.opened = True
            self.selectedForm = False
        except:
            return errors.BR_ERRORxNO_ACCESS_WEB

    def add_headers(self, header):
        """
        Agregar headers al navegador.

        :param header: String de browser header
        :type header: str

        :return: void
        :rtype: None
        """
        self.br.addheaders = [('User-agent', header)]

    def clear_cookies(self):
        """
        Elimina las cookies.

        :return: void
        :rtype: None
        """
        self.cookies.clear_session_cookies()

    def get_html(self):
        """
        Obtener el código HTML.

        :return: String con el código HTML
        :rtype: str
        """
        if self.opened:
            return self.br.response().read()
        else:
            return errors.BR_ERRORxNO_OPENED

    def get_title(self):
        """
        Obtener el título.

        :return: String con el título de la página web
        :rtype: str
        """
        if self.opened:
            return self.br.title()
        else:
            return errors.BR_ERRORxNO_OPENED

    def get_headers(self):
        """
        Obtener los headers.

        :return: String con los headers
        :rtype: str
        """
        if self.opened:
            return self.br.response().info()
        else:
            return errors.BR_ERRORxNO_OPENED

    def get_forms(self):
        """
        Obtener una lista con los formularios de la página web.

        :return: Lista de nombres de formulario
        :rtype: list
        """
        if self.opened:
            return self.br.forms()
        else:
            return errors.BR_ERRORxNO_OPENED

    def play_browser(self):
        """
        Obtener el browser.

        :return: Browser instanciado
        :rtype: Browser
        """
        return self.br

    # noinspection SpellCheckingInspection
    def select_form_by_id(self, formid):
        """
        Definir un formulario como activo mediante un id.

        :param formid: ID del formulario
        :type formid: str

        :return: void
        :rtype: None
        """
        formid = str(formid)
        if formid != "":  # Si el id no está vacío
            if formid.isdigit():  # Si es un dígito
                try:
                    self.selectedForm = True
                    return self.br.select_form(nr=int(formid))
                except:
                    return errors.BR_ERRORxERROR_SET_FORM
            else:
                return errors.BR_ERRORxNO_VALIDID
        else:
            return errors.BR_ERRORxNO_FORMID

    # noinspection SpellCheckingInspection
    def select_form_by_name(self, formname):
        """
        Definir un formulario como activo mediante un ID.
        :param formname: ID del formulario.

        :return: void
        :rtype: None
        """
        if formname != "":  # Si el id no está vacío
            try:
                self.selectedForm = True
                return self.br.select_form(name=formname)
            except:
                return errors.BR_ERRORxERROR_SET_FORM
        else:
            return errors.BR_ERRORxNO_FORMID

    def submit_form(self, form, values):
        """
        Enviar un formulario.

        :param form: Formulario
        :type form: list
        :param values: Valores
        :type values: list

        :return: void
        :rtype: None
        """
        if self.selectedForm:
            if len(form) > 0 and len(values) > 0:
                if len(form) == len(values):
                    try:
                        for i in range(len(form)):
                            self.br.form[form[i]] = values[i]
                        self.br.submit()
                    except:
                        return errors.BR_ERRORxERROR_SET_SUBMIT
                else:
                    return errors.BR_ERRORxNO_VALID_SUBMIT_NOT_EQUAL
            else:
                return errors.BR_ERRORxNO_VALID_SUBMIT_EMPTY
        else:
            return errors.BR_ERRORxNO_SELECTED_FORM
