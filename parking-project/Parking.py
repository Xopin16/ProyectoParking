import Cliente
from Abonado import Abonado
from Abono import Abono
from Plaza import Plaza
from _datetime import datetime, timedelta
from Vehiculo import Vehiculo
import random


class Parking:

    def __init__(self, abonados=[], num_plazas=[], clientes=[], plazas={}, registro_facturas=[]):
        self.__abonados = abonados
        self.__num_plazas = num_plazas
        self.__clientes = clientes
        self.__plazas = plazas
        self.__registro_facturas = registro_facturas

    def __str__(self):
        return '{} {} {} {} {}'.format(self.abonados, self.num_plazas, self.clientes, self.plazas,
                                       self.registro_facturas)

    @property
    def abonados(self):
        return self.__abonados

    @abonados.setter
    def abonados(self, x):
        self.__abonados = x

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

    # MÉTODOS PARA LA ZONA CLIENTE
    def depositar_vehiculo(self, cliente=None):
        print(self.plazas)
        cliente.vehiculo.matricula = input("Introduzca matrícula: ")
        cliente.vehiculo.tipo = input("Introduzca tipo de vehículo: ")
        if len(self.num_plazas) < 100:
            if cliente.vehiculo.tipo == 'Turismo':
                cliente.plaza = Plaza(id_plaza=self.num_plazas[0], pin='111111',
                                      fecha_deposito=datetime(2022, 12, 1, 10, 15, 00, 00000),
                                      fecha_salida=None)
                self.num_plazas.pop(0)
                self.plazas['Turismo'].pop(0)
            elif cliente.vehiculo.tipo == 'Motocicleta':
                cliente.plaza = Plaza(id_plaza=self.num_plazas[0], pin='111111',
                                      fecha_deposito=datetime(2022, 12, 1, 10, 15, 00, 00000),
                                      fecha_salida=None)
                self.num_plazas.pop(0)
                self.plazas['Motocicleta'].pop(0)
            else:
                cliente.plaza = Plaza(id_plaza=self.num_plazas[0], pin='111111',
                                      fecha_deposito=datetime(2022, 12, 1, 10, 15, 00, 00000),
                                      fecha_salida=None)
                self.num_plazas.pop(0)
                self.plazas['MR'].pop(0)
        return

    # FALTA PINTAR TICKET

    def retirar_vehiculo(self, cliente=None):
        matricula = input("Introduzca matricula: ")
        id_plaza = int(input("Introduzca id de la plaza: "))
        pin = input("Introduzca pin: ")
        if pin == cliente.plaza.pin and id_plaza == cliente.plaza.id_plaza \
                and matricula == cliente.vehiculo.matricula:
            if cliente.vehiculo.tipo == 'Turismo':
                self.num_plazas.insert(0, cliente.plaza.id_plaza)
                self.plazas['Turismo'].insert(0, cliente.plaza.id_plaza)
                self.clientes.remove(cliente)
            elif cliente.vehiculo.tipo == 'Motocicleta':
                self.num_plazas.insert(0, cliente.plaza.id_plaza)
                self.plazas['Motocicleta'].insert(0, cliente.plaza.id_plaza)
                self.clientes.remove(cliente)
            else:
                self.num_plazas.insert(0, cliente.plaza.id_plaza)
                self.plazas['MR'].insert(0, cliente.plaza.id_plaza)
                self.clientes.remove(cliente)
        return self.facturacion(cliente)

    def depositar_abonados(self, abonado=None):
        matricula = input("Introduzca matricula: ")
        dni = input("Introduzca dni: ")
        if dni == abonado.dni and matricula == abonado.vehiculo.matricula:
            abonado.plaza.estado('abono ocupada')
        else:
            print("No existe tal abonado")

    def retirar_abonados(self, abonado=None):
        matricula = input("Introduzca matricula: ")
        id_plaza = input("Introduce dni: ")
        pin = input("Introduce el pin")
        if matricula == abonado.vehiculo.matricula and abonado.plaza.id_plaza == id_plaza and abonado.plaza.pin == pin:
            abonado.plaza.estado('abono libre')
        else:
            print("No existe tal abonado")

    # MÉTODOS PARA LA ZONA ADMINISTRADOR
    def controlar_estado_parking(self):
        for c, v in self.plazas.items():
            print(c, v)

    def facturacion(self, cliente=None):
        factura = 0.0
        if cliente.vehiculo.tipo == 'Turismo':
            cliente.plaza.fecha_salida = datetime.now()
            diferencia = cliente.plaza.fecha_salida - cliente.plaza.fecha_deposito
            minutos_diferencia = diferencia.total_seconds() / 60
            factura = minutos_diferencia * 0.12
        elif cliente.vehiculo.tipo == 'Motocicleta':
            cliente.plaza.fecha_salida = datetime.now()
            diferencia = cliente.plaza.fecha_salida - cliente.plaza.fecha_deposito
            minutos_diferencia = diferencia.total_seconds() / 60
            factura = minutos_diferencia * 0.08
        else:
            cliente.plaza.fecha_salida = datetime.now()
            diferencia = cliente.plaza.fecha_salida - cliente.plaza.fecha_deposito
            minutos_diferencia = diferencia.total_seconds() / 60
            factura = minutos_diferencia * 0.12
        return factura

    def gestion_abonos(self):
        nombre = input("Introduzca su nombre: ")
        apellidos = input("Introduzca su apellido: ")
        num_tarjeta = input("Introduzca su número de tarjeta: ")
        email = input("Introduzca su email: ")
        dni = input("Introduzca su dni")
        v1 = Vehiculo(matricula="1111AB", tipo="Turismo")
        ab = Abonado(nombre=nombre, apellidos=apellidos, num_tarjeta=num_tarjeta, email=email,
                     dni=dni, abono=None, vehiculo=v1, plaza=None)
        self.abonados.append(ab)
        menu_abono = 1
        while menu_abono != 0:
            menu_abono = input("¿Qué desea hacer?")
            print("1. Alta de abono")
            print("2. Modificar abono")
            print("3. Baja de abono")
            print("Pulsa cualquier 0 para salir")
            if menu_abono == 1:
                ab.plaza = Plaza(id_plaza=self.num_plazas[0], pin=random.randint(100000, 999999)
                                 , fecha_deposito=None, fecha_salida=None)
                self.num_plazas.pop(0)
                tipo_abono = input("Elija el tipo de abono")
                print("1. Mensual(25€)")
                print("2. Trimestral(75€)")
                print("3. Semestral(130€)")
                print("4. Anual(200€)")
                if tipo_abono == 1:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=30)
                    ab.abono = Abono(tipo=tipo_abono, factura=25, fecha_activacion=fecha_activacion,
                                     fecha_cancelacion=fecha_cancelacion)
                    self.registro_facturas.append(ab.abono.factura)
                elif tipo_abono == 2:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=90)
                    ab.abono = Abono(tipo=tipo_abono, factura=75, fecha_activacion=fecha_activacion,
                                     fecha_cancelacion=fecha_cancelacion)
                    self.registro_facturas.append(ab.abono.factura)
                elif tipo_abono == 3:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=180)
                    ab.abono = Abono(tipo=tipo_abono, factura=130, fecha_activacion=fecha_activacion,
                                     fecha_cancelacion=fecha_cancelacion)
                    self.registro_facturas.append(ab.abono.factura)
                else:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=365)
                    ab.abono = Abono(tipo=tipo_abono, factura=200, fecha_activacion=fecha_activacion,
                                     fecha_cancelacion=fecha_cancelacion)
                    self.registro_facturas.append(ab.abono.factura)
                print(ab)
            elif menu_abono == 2:
                cambio = input("¿Que desea modificar? 1. Tipo de abono, 2.Datos Personales")
                if cambio == 1:
                    print("1. Mensual(25€)")
                    print("2. Trimestral(75€)")
                    print("3. Semestral(130€)")
                    print("4. Anual(200€)")
                    new_tipo = input("Indica el tipo de abono al que desea cambiar")
                    if new_tipo == 1:
                        fecha_activacion = datetime.now()
                        fecha_cancelacion = datetime.now() + timedelta(days=30)
                        ab.abono.tipo(new_tipo)
                        ab.abono.fecha_activacion(fecha_activacion)
                        ab.abono.fecha_cancelacion(fecha_cancelacion)
                        self.registro_facturas.append(ab.abono.factura(25))
                    elif new_tipo == 2:
                        fecha_activacion = datetime.now()
                        fecha_cancelacion = datetime.now() + timedelta(days=90)
                        ab.abono.tipo(new_tipo)
                        ab.abono.fecha_activacion(fecha_activacion)
                        ab.abono.fecha_cancelacion(fecha_cancelacion)
                        self.registro_facturas.append(ab.abono.factura(75))
                    elif new_tipo == 3:
                        fecha_activacion = datetime.now()
                        fecha_cancelacion = datetime.now() + timedelta(days=180)
                        ab.abono.tipo(new_tipo)
                        ab.abono.fecha_activacion(fecha_activacion)
                        ab.abono.fecha_cancelacion(fecha_cancelacion)
                        self.registro_facturas.append(ab.abono.factura(130))
                    else:
                        fecha_activacion = datetime.now()
                        fecha_cancelacion = datetime.now() + timedelta(days=365)
                        ab.abono.tipo(new_tipo)
                        ab.abono.fecha_activacion(fecha_activacion)
                        ab.abono.fecha_cancelacion(fecha_cancelacion)
                        self.registro_facturas.append(ab.abono.factura(200))
                else:
                    datos = input("1.Nombre, 2.Apellidos, 3.Numero de tarjeta, 4.Email, 5.Vehiculo")
                    if datos == 1:
                        ab.nombre(input("Indica el nombre"))
                    elif datos == 2:
                        ab.apellidos(input("Indica los apellidos"))
                    elif datos == 3:
                        ab.num_tarjeta(input("Indica el número de tarjeta"))
                    elif datos == 4:
                        ab.email(input("Indica el email"))
                    elif datos == 5:
                        edit_vehiculo = input("Indica 1 para cambiar la matricula y 2 para el tipo")
                        if edit_vehiculo == 1:
                            ab.vehiculo.matricula(input("Indica la matricula: "))
                        else:
                            ab.vehiculo.tipo(input("Indica el tipo de vehículo: "))

            else:
                self.abonados.remove(ab)

    def caducidad_abonos(self):
        month = int(input("Introduzca el mes del 1 al 12"))
        for abonado in self.abonados:
            if month in abonado.abono.caducidad:
                print(abonado)



