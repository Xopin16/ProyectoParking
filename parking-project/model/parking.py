import pickle
from model.plaza import Plaza


class Parking:

    def __init__(self, plazas_totales, registro_facturas=[]):
        self.__plazas_totales = plazas_totales
        self.__registro_facturas = registro_facturas

    def __str__(self):
        return '{} {}'.format(self.plazas_totales, self.registro_facturas)

    @property
    def plazas_totales(self):
        return self.__plazas_totales

    @plazas_totales.setter
    def plazas_totales(self, x):
        self.__plazas_totales = x

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, x):
        self.__clientes = x

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, x):
        self.__plazas = x

    @property
    def registro_facturas(self):
        return self.__registro_facturas

    @registro_facturas.setter
    def registro_facturas(self, x):
        self.__registro_facturas = x

    def mostrar_plazas(self, lista):
        for p in lista:
            print("Id de la plaza: ", p.id_plaza, ", Estado: ", p.estado)

    def mostrar_ticket(self, cliente):
        print("\nFACTURA")
        print("---------------------------------------")
        print("Matricula: ", cliente.vehiculo.matricula)
        print("Fecha de depósito: ", cliente.plaza.fecha_deposito)
        print("Identificador de la plaza: ", cliente.plaza.id_plaza)
        print("Pin: ", cliente.pin)
        print("---------------------------------------\n")

    def rellenar_plazas(self, lista):
        cont = len(lista)
        while cont < self.plazas_totales:
            cont += 1
            new_plaza = Plaza(id_plaza=cont, estado='libre')
            lista.append(new_plaza)

    def mostrar_plazas_tipo(self, lista_clientes):
        tipos = ["Turismo", "Motocicleta", "Movilidad reducida"]
        n_plazas = [self.plazas_totales * 0.7, self.plazas_totales * 0.15, self.plazas_totales * 0.15]
        plazas = dict(zip(tipos, n_plazas))
        for c in lista_clientes:
            if c.vehiculo.tipo == tipos[0]:
                plazas['Turismo'] -= 1
            elif c.vehiculo.tipo == tipos[1]:
                plazas['Motocicleta'] -= 1
            else:
                plazas['Movilidad reducida'] -= 1
        for k, v in plazas.items():
            print("Tipo de plaza: ", k, "| Numero de plazas", round(v))

    def guardar_factura_cliente(self, lista):
        lista.append(self)
        facturas_cliente = open('files/facturas_cliente.pckl', 'wb')
        pickle.dump(lista, facturas_cliente)
        facturas_cliente.close()
