from Model.Abonado import Abonado


class Parking:

    def __init__(self, num_plazas=[], clientes=[], registro_facturas={}):
        self.__num_plazas = num_plazas
        self.__clientes = clientes
        self.__plazas = self.rellenar_plazas()
        self.__registro_facturas = registro_facturas

    def __str__(self):
        return '{} {} {} {}'.format(self.num_plazas, self.clientes, self.plazas,
                                    self.registro_facturas)

    @property
    def num_plazas(self):
        return self.__num_plazas

    @num_plazas.setter
    def num_plazas(self, x):
        self.__num_plazas = x

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

    def mostrar_ticket(self, cliente=None):
        print("---------------------------------------")
        print("FACTURA")
        print("---------------------------------------")
        print("Matricula: ", cliente.vehiculo.matricula)
        print("Fecha de depósito: ", cliente.plaza.fecha_deposito)
        print("Identificador de la plaza: ", cliente.plaza.id_plaza)
        print("Pin: ", cliente.plaza.pin)

    def mostrar_clientes(self):
        for c in self.clientes:
            print(c.vehiculo, c.plaza)
            if isinstance(c, Abonado):
                print(c)

    def mostrar_plazas(self, pk):
        for e, p in self.plazas.items():
            print("Id de la plaza: ", e, ", Estado: ", p)

    def rellenar_plazas(self):
        plazas = list(range(1, 41))
        state = 'libre'
        cont = 1
        pl = dict()
        for p in plazas:
            if len(self.clientes) > len(pl):
                salir = True
                for c in self.clientes:
                    while salir and c.plaza.id_plaza not in pl.keys():
                        if c.plaza.id_plaza not in pl.keys():
                            pl[p] = c.plaza.estado
                            cont += 1
                            self.num_plazas.pop(0)
                            salir = False
            else:
                pl[cont] = state
                cont += 1
        return pl

    def mostrar_registro(self):
        for k, v in self.registro_facturas.items():
            print("Fecha: ", k, ", Cobro: ", v, "€")

    def rellenar_plazas_tipo(self):
        tipos = ["Turismo", "Motocicleta", "Movilidad reducida"]
        n_plazas = [28, 6, 6]
        plazas = dict(zip(tipos, n_plazas))
        for c in self.clientes:
            if c.vehiculo.tipo == tipos[0]:
                plazas['Turismo'] -= 1
            elif c.vehiculo.tipo == tipos[1]:
                plazas['Motocicleta'] -= 1
            else:
                plazas['Movilidad reducida'] -= 1
        return plazas

    def mostrar_plazas_tipo(self):
        plazas = self.rellenar_plazas_tipo()
        for k, v in plazas.items():
            print("Tipo de plaza: ", k, "| Numero de plazas", v)
