from _datetime import datetime


class Abono:

    def __init__(self, tipo, factura, fecha_activacion=datetime, fecha_cancelacion=datetime):
        self.__tipo = tipo
        self.__factura = factura
        self.__fecha_activacion = fecha_activacion
        self.__fecha_cancelacion = fecha_cancelacion

    def __str__(self):
        return '{} {} {} {}'.format(self.tipo, self.factura, self.fecha_activacion, self.fecha_cancelacion)

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, x):
        self.__tipo = x

    @property
    def factura(self):
        return self.__factura

    @factura.setter
    def factura(self, x):
        self.__factura = x

    @property
    def fecha_activacion(self):
        return self.__fecha_activacion

    @fecha_activacion.setter
    def fecha_activacion(self, x):
        self.__fecha_activacion = x

    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion

    @fecha_cancelacion.setter
    def fecha_cancelacion(self, x):
        self.__fecha_cancelacion = x

