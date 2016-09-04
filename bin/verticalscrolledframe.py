#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noinspection SpellCheckingInspection
"""
VERTICALSCROLLEDFRAME
Este archivo provee una clase para administrar ventanas con barras de deslizamiento en Tkinter.

Autor: http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame
"""

# Importación de librerías
from Tkinter import Frame, Scrollbar, Canvas, NW, BOTH, TRUE, LEFT, RIGHT, VERTICAL, FALSE, Y


# noinspection PyUnusedLocal,PyArgumentList
class VerticalScrolledFrame(Frame):
    """
    Ventanas con barra de desplazamiento en Tkinter (python-tk).
    """

    def __init__(self, parent, *args, **kw):
        """
        Constructor de la clase
        :param parent: Ventana padre
        :type parent: object
        :param args: Argumentos opcionales
        :type args: list
        :param kw: Keywords
        :type kw: list

        :return: void
        :rtype: None
        """
        Frame.__init__(self, parent, *args, **kw)
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)
        self.canv = canvas  # @UndefinedVariable
        self.scroller = vscrollbar

        def _configure_interior(event):
            """
            Configura un evento al hacer scroll en la ventana interior
            :param event: Evento
            :type event: object

            :return: void
            :rtype: None
            """
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            """
            Configura el ítem en el canvas
            :param event: Evento
            :type event: object

            :return: void
            :rtype: None
            """
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)
