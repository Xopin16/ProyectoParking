from _datetime import datetime


class Plaza:

    def __init__(self, id_plaza, pin, fecha_deposito, fecha_salida):
        self.__fecha_deposito = fecha_deposito
        self.__fecha_salida = fecha_salida
        self.__id_plaza = id_plaza
        self.__estado = "libre"
        self.__pin = pin

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id_plaza, self.estado, self.pin, self.fecha_deposito,
                                       self.fecha_salida)

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, x):
        self.__id_plaza = x

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, x):
        self.__estado = x

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, x):
        self.__pin = x

    @property
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, x):
        self.__fecha_deposito = x

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, x):
        self.__fecha_salida = x
