#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CONFIGLOADER
Permite cargar configuraciones dado un archivo dado por parámetro.
Formato de archivo:

   # Comentario
   CONFIG_1 = VALUE
   CONFIG_2 = VALUE2

Autor: PABLO PIZARRO @ github.com/ppizarror
Fecha: ABRIL 2015 - 2016
Licencia: GPLv2
"""
__author__ = "ppizarror"

# Importación de librerías
from kwargsutils import kwargIsTrueParam
from utils import convertToNumber, string2list
import errors

# Definición de constantes
CONFIG_COMMENT = "#"
CONFIG_LOAD = "El archivo de configuraciones '{0}' ha sido cargado correctamente"
CONFIG_PRINTNOCONFIG = "No se encontraron configuraciones"
CONFIG_PRINTPARAM = "\t${0} : {1}"
# noinspection SpellCheckingInspection
CONFIG_PRINTPARAMETER = "Parametros cargados:"
CONFIG_PRINTPARAMSIMPLE = "\t{0}"
CONFIG_SAVED = "El archivo de configuraciones '{0}' ha sido guardado exitosamente"
CONFIG_SEPARATOR = " = "
FALSE = "FALSE"
TRUE = "TRUE"


class configLoader:
    """
    Carga configuraciones y retorna sus elementos.
    """

    # noinspection PyUnboundLocalVariable
    def __init__(self, directory, conffile, **kwargs):
        """
        Función constructora de la clase.

        Keywords:
            - verbose (bool) = Indica si se imprime el estado de ejecución o no en consola

        :param directory: Ubicación del archivo de configuraciones
        :type directory: str
        :param conffile: Nombre del archivo de configuraciones
        :type conffile: str
        :param kwargs: Parámetros adicionales
        :type kwargs: list

        :return: void
        """
        # Se carga el archivo de configuraciones
        filename = directory + conffile
        try:
            # noinspection PyShadowingBuiltins
            file = open(filename.replace("\\", "/"), "r")  # @ReservedAssignment
        except:
            errors.throw(errors.ERROR_NOCONFIGFILE, filename)

        # Variables
        self.config_single = []
        self.configs = {}
        self.filename = filename
        self.filename_title = conffile
        self.totalconfigs = 0

        # Se cargan las configuraciones
        for configline in file:
            if configline[0] != CONFIG_COMMENT and configline != "\n":
                config = string2list(configline, CONFIG_SEPARATOR)
                if len(config) == 1:
                    self.config_single.append(config[0])
                elif len(config) == 2:
                    self.totalconfigs += 1
                    self.configs[config[0]] = config[1]
                else:
                    errors.throw(errors.ERROR_BADCONFIG, configline, filename)
        if kwargIsTrueParam(kwargs, "verbose"):
            self.verbose = True
            if not (self.totalconfigs + len(self.config_single)):
                errors.warning(errors.WARNING_NOCONFIGFOUND, filename)
            else:
                print CONFIG_LOAD.format(filename)
        else:
            self.verbose = False
        file.close()

    def export(self, replace=True, name=None):
        """
        Función que exporta las configuraciones a un directorio.

        :param replace: Reemplaza el archivo anterior
        :type replace: bool
        :param name: Nombre del archivo nuevo
        :rtype name: str

        :return: void
        :rtype: None
        """
        try:
            if replace:
                name = self.filename
            f = open(name, "w")
            # Se escriben las configuraciones unarias
            for conf in self.config_single:
                f.write(str(conf) + "\n")
            # Se escriben las configuraciones complejas
            for key in self.configs.keys():
                f.write(str(key) + CONFIG_SEPARATOR + self.configs[key] + "\n")
            # Se cierra el archivo
            f.close()
            if self.verbose: print CONFIG_SAVED.format(name)
        except:
            if self.verbose: errors.throw(errors.ERROR_CONFIGBADEXPORT)

    def isFalse(self, param):
        """
        Función que retorna true si el parámetro del archivo es falso.

        :param param: Parámetro a buscar
        :type param: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        if param in self.getParameters():
            if self.configs[param].upper() == FALSE or self.configs[param] == "0":
                return True
            else:
                return False
        else:
            errors.warning(errors.ERROR_CONFIGNOTEXISTENT, param)

    def isTrue(self, param):
        """
        Función que retorna true si el parámetro del archivo es verdadero.

        :param param: Parámetro a buscar
        :type param: str

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        if param in self.getParameters():
            if self.configs[param].upper() == TRUE or self.configs[param] == "1":
                return True
            else:
                return False
        else:
            errors.warning(errors.ERROR_CONFIGNOTEXISTENT, param)

    def getParameters(self):
        """
        Retorna una lista con todos los parámetros cargados.

        :return: Lista de parámetros
        :rtype: list
        """
        allconfigs = []
        for i in self.config_single:
            allconfigs.append(i)
        for j in self.configs.keys():
            allconfigs.append(j)
        return allconfigs

    # noinspection SpellCheckingInspection
    def getValue(self, param, **kwargs):
        """
        Retorna el valor del parámetro param.

        Keywords:
            - autoNumberify (bool) = Activa la auto-conversión a números

        :param param: Parámetro a obtener valor
        :type param: object
        :param kwargs: Keywords

        :return: Valor del parámetro
        :rtype: object
        """
        if str(param).isdigit():
            param = int(param)
            if 0 <= param < len(self.config_single):
                paramValue = str(self.config_single[param])

                # noinspection PyTypeChecker
                if kwargIsTrueParam(kwargs, "autoNumberify"):  # Auto-conversión a números
                    return convertToNumber(paramValue)
                # El resultado se entrega sin convertir
                else:
                    return paramValue

            else:
                errors.throw(errors.ERROR_BADINDEXCONFIG, str(param))
        else:
            if param in self.getParameters():
                paramValue = self.configs[param]

                # noinspection PyTypeChecker
                if kwargIsTrueParam(kwargs, "autoNumberify"):  # Auto-conversión a números
                    return convertToNumber(paramValue)
                # El resultado se entrega sin convertir
                else:
                    return paramValue

            else:
                errors.warning(errors.ERROR_CONFIGNOTEXISTENT, param)
        return None

    def getValueListed(self, param, split=";"):
        """
        Retorna una lista con los valores de una configuración.

        :param param: Parámetro
        :type param: str
        :param split: String de separación
        :type split: str

        :return: Lista de valores
        :rtype: list
        """
        value = self.getValue(param)
        if value is not None:
            value = str(value).split(split)
            valueNewList = []
            for d in value:
                valueNewList.append(d.strip())
            return valueNewList
        else:
            return []

    def paramExists(self, param):
        """
        Retorna true/false si es que el parámetro <param> existe.

        :param param: Parámetro a buscar
        :type param: str, unicode

        :return: Booleano indicando pertenencia
        :rtype: bool
        """
        return param in self.getParameters()

    def printParameters(self):
        """
        Imprime una lista con todos los parámetros cargados.

        :return: void
        :rtype: None
        """
        if self.totalconfigs + len(self.config_single) > 0:
            print CONFIG_PRINTPARAMETER
            if self.totalconfigs > 0:
                for parameter in self.getParameters():
                    try:
                        print CONFIG_PRINTPARAM.format(parameter, self.configs[parameter])
                    except:
                        errors.throw(errors.ERROR_CONFIGCORRUPT, self.filename_title)
            for config in self.config_single:
                print CONFIG_PRINTPARAMSIMPLE.format(config)
        else:
            print CONFIG_PRINTNOCONFIG
        return

    def setParameter(self, paramName, paramValue):
        """
        Define un parámetro.

        :param paramName: Nombre del parámetro
        :type paramName: str
        :param paramValue: Valor del parámetro
        :type paramValue: object

        :return: void
        :rtype: None
        """
        self.configs[str(paramName)] = str(paramValue)
