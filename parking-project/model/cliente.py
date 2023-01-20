import pickle


class Cliente:

    def __init__(self, vehiculo=None, plaza=None, pin=None):
        self.__vehiculo = vehiculo
        self.__plaza = plaza
        self.__pin = pin

    def __str__(self):
        return '{} {} {}'.format(self.vehiculo, self.plaza, self.pin)

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, valor):
        self.__vehiculo = valor

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, valor):
        self.__plaza = valor

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, valor):
        self.__pin = valor

    def guardar_cliente(self, lista):
        lista.append(self)
        clientes = open('files/clientes.pckl', 'wb')
        pickle.dump(lista, clientes)
        clientes.close()

