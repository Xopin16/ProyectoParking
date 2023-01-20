import pickle


class Plaza:

    def __init__(self, id_plaza=None, estado=None, fecha_deposito=None):
        self.__id_plaza = id_plaza
        self.__estado = estado
        self.__fecha_deposito = fecha_deposito

    def __str__(self):
        return '{} {}'.format(self.id_plaza, self.estado, self.fecha_deposito)

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
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, x):
        self.__fecha_deposito = x

    def guardar_plaza(self, lista):
        lista.append(self)
        plazas = open('files/plazas.pckl', 'wb')
        pickle.dump(lista, plazas)
        plazas.close()




