import pickle


class Vehiculo:

    def __init__(self, matricula, tipo):
        self.matricula = matricula
        self.tipo = tipo

    def __str__(self):
        return '{} {}'.format(self.matricula, self.tipo)

    def guardar_vehiculo(self, lista):
        lista.append(self)
        vehiculos = open('files/vehiculos.pckl', 'wb')
        pickle.dump(lista, vehiculos)
        vehiculos.close()
