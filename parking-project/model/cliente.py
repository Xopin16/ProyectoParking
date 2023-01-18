import pickle


class Cliente:

    def __init__(self, vehiculo, plaza):
        self.__vehiculo = vehiculo
        self.__plaza = plaza

    def __str__(self):
        return '{} {}'.format(self.vehiculo, self.plaza)

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

    def guardar_cliente(self, lista):
        lista.append(self)
        clientes = open('files/clientes.pckl', 'wb')
        pickle.dump(lista, clientes)
        clientes.close()

    def cargar_clientes(self):
        clientes = open('files/clientes.pckl', 'rb')
        clientes_list = pickle.load(clientes)
        clientes.close()
        return clientes_list
