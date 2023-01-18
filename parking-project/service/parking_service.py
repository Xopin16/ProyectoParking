from datetime import datetime, timedelta
import random

from model.abonado import Abonado
from model.abono import Abono
from model.cliente import Cliente
from model.plaza import Plaza
from model.vehiculo import Vehiculo


class ParkingService:

    def depositar_vehiculo(self, parking=None, cliente=None, lista=None):
        parking.mostrar_plazas_tipo()
        if len(parking.num_plazas) < 41:
            if cliente.vehiculo.tipo == 'Turismo':
                parking.num_plazas.pop(0)
                parking.plazas[cliente.plaza.id_plaza] = 'ocupada'
                # parking.clientes.append(c1)
            elif cliente.vehiculo.tipo == 'Motocicleta':
                parking.num_plazas.pop(0)
                parking.plazas[cliente.plaza.id_plaza] = 'ocupada'
                # parking.clientes.append(c1)
            else:
                parking.num_plazas.pop(0)
                parking.plazas[cliente.plaza.id_plaza] = 'ocupada'
        return parking.mostrar_ticket(cliente)

    def retirar_vehiculo(self, parking=None, lista=None):
        cliente = Cliente(vehiculo=None, plaza=None)
        matricula = input("Introduzca matricula: ")
        id_plaza = int(input("Introduzca id de la plaza: "))
        pin = int(input("Introduzca pin: "))
        for c in parking.clientes:
            if pin == c.plaza.pin and id_plaza == c.plaza.id_plaza \
                    and matricula == c.vehiculo.matricula:
                cliente = c
        if cliente in parking.clientes:
            if pin == cliente.plaza.pin and id_plaza == cliente.plaza.id_plaza \
                    and matricula == cliente.vehiculo.matricula:
                if cliente.vehiculo.tipo == 'Turismo':
                    parking.plazas[cliente.plaza.id_plaza] = 'libre'
                    parking.num_plazas.insert(0, cliente.plaza.id_plaza)
                    parking.clientes.remove(cliente)
                elif cliente.vehiculo.tipo == 'Motocicleta':
                    parking.num_plazas.insert(0, cliente.plaza.id_plaza)
                    parking.plazas['Motocicleta'].insert(0, cliente.plaza.id_plaza)
                    parking.clientes.remove(cliente)
                else:
                    parking.num_plazas.insert(0, cliente.plaza.id_plaza)
                    parking.plazas['MR'].insert(0, cliente.plaza.id_plaza)
                    parking.clientes.remove(cliente)
            parking.registro_facturas[cliente.plaza.fecha_salida] = self.cobrar(cliente)
            return self.cobrar(cliente)
        else:
            return None

    def depositar_abonados(self, parking=None, lista=None):
        abonado = 0
        matricula = input("Introduzca matricula: ")
        dni = input("Introduzca dni: ")
        for c in parking.clientes:
            if isinstance(c, Abonado):
                if matricula == c.vehiculo.matricula and dni == c.dni:
                    abonado = c
        if abonado in parking.clientes:
            parking.plazas[abonado.plaza.id_plaza] = 'abono ocupada'
        else:
            print("No existe tal abonado")

    def retirar_abonados(self, parking=None, lista=None):
        abonado = 0
        matricula = input("Introduzca matricula: ")
        id_plaza = int(input("Introduce el id_plaza: "))
        pin = int(input("Introduce el pin: "))
        for c in parking.clientes:
            if matricula == c.vehiculo.matricula and id_plaza == c.plaza.id_plaza and pin == c.plaza.pin:
                abonado = c
        if abonado in parking.clientes:
            parking.plazas[abonado.plaza.id_plaza] = 'abono libre'
        else:
            print("No existe tal abonado")

    # MÉTODOS PARA LA ZONA ADMINISTRADOR
    def controlar_estado_parking(self, parking=None, lista=None):
        parking.mostrar_plazas()

    def cobrar(self, cliente=None):
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
        return round(factura, 2)

    def mostrar_facturacion(self, parking=None, lista=None):
        print("Indique la primera fecha: ")
        fecha1 = datetime(int(input("Año: ")), int(input("Mes: ")), int(input("Dia: ")), int(input("Hora: ")))
        print("Indique la segunda fecha: ")
        fecha2 = datetime(int(input("Año: ")), int(input("Mes: ")), int(input("Dia: ")), int(input("Hora: ")))
        for k, v in parking.registro_facturas.items():
            if fecha1 < k < fecha2:
                print("Fecha: ", k, "Cobro: ", v, "€")

    def consular_abonados(self, parking=None, lista=None):
        for a in parking.clientes:
            if isinstance(a, Abonado):
                print("Tipo de abono: ", a.abono.tipo, ", Cobro total: ", a.abono.factura, "€")

    def gestion_abonos(self, parking=None, lista=None):
        menu_abono = 1
        cambio = 1
        while menu_abono != 0:
            print("1. Alta de abono")
            print("2. Modificar abono")
            print("3. Baja de abono")
            print("Pulsa cualquier 0 para salir")
            menu_abono = int(input("¿Qué desea hacer?: "))
            if menu_abono == 1:
                nombre = input("Introduzca su nombre: ")
                apellidos = input("Introduzca su apellido: ")
                num_tarjeta = input("Introduzca su número de tarjeta: ")
                email = input("Introduzca su email: ")
                dni = input("Introduzca su dni: ")
                v1 = Vehiculo(matricula="1111AB", tipo="Turismo")
                ab = Abonado(nombre=nombre, apellidos=apellidos, num_tarjeta=num_tarjeta, email=email,
                             dni=dni, abono=None, vehiculo=v1, plaza=Plaza(id_plaza=parking.num_plazas[0],
                                                                           pin=random.randint(100000, 999999),
                                                                           fecha_deposito=None, fecha_salida=None,
                                                                           estado='abono ocupada'))
                parking.clientes.append(ab)
                parking.plazas[ab.plaza.id_plaza] = ab.plaza.estado
                parking.num_plazas.pop(0)
                print("1. Mensual(25€)")
                print("2. Trimestral(75€)")
                print("3. Semestral(130€)")
                print("4. Anual(200€)")
                print("0. Para salir")
                tipo_abono = int(input("Elija el tipo de abono: "))
                if tipo_abono == 1:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=30)
                    ab.abono = Abono(tipo=tipo_abono, factura=25, fecha_activacion=fecha_activacion,
                                     fecha_cancelacion=fecha_cancelacion)
                elif tipo_abono == 2:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=90)
                    ab.abono = Abono(tipo=tipo_abono, factura=75, fecha_activacion=fecha_activacion,
                                     fecha_cancelacion=fecha_cancelacion)
                elif tipo_abono == 3:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=180)
                    ab.abono = Abono(tipo=tipo_abono, factura=130, fecha_activacion=fecha_activacion,
                                     fecha_cancelacion=fecha_cancelacion)
                else:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=365)
                    ab.abono = Abono(tipo=tipo_abono, factura=200, fecha_activacion=fecha_activacion,
                                     fecha_cancelacion=fecha_cancelacion)
                print(ab)
            elif menu_abono == 2:
                ab = 0
                dni = input("Indique su dni: ")
                pin = int(input("Indique su pin: "))
                tipo_abono = ['Mensual', 'Trimestral', 'Semestral', 'Anual']
                for a in parking.clientes:
                    if a.plaza.pin == pin and a.dni == dni:
                        ab = a
                if isinstance(ab, Abonado):
                    while cambio != 0:
                        print("1.Modificar tipo de abono.")
                        print("2.Modificar datos personales.")
                        cambio = int(input("¿Que desea modificar?: "))
                        if cambio == 1:
                            print("1. Mensual(25€)")
                            print("2. Trimestral(75€)")
                            print("3. Semestral(130€)")
                            print("4. Anual(200€)")
                            new_tipo = int(input("Indica el tipo de abono al que desea cambiar: "))
                            if new_tipo == 1:
                                ab.abono.tipo = tipo_abono[0]
                                ab.abono.factura = 25
                                ab.abono.fecha_activacion = datetime.now()
                                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=30)
                            elif new_tipo == 2:
                                ab.abono.tipo = tipo_abono[1]
                                ab.abono.factura = 70
                                ab.abono.fecha_activacion = datetime.now()
                                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=90)
                            elif new_tipo == 3:
                                ab.abono.tipo = tipo_abono[2]
                                ab.abono.factura = 130
                                ab.abono.fecha_activacion = datetime.now()
                                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=180)
                            else:
                                ab.abono.tipo = tipo_abono[3]
                                ab.abono.factura = 200
                                ab.abono.fecha_activacion = datetime.now()
                                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=365)
                        elif cambio == 2:
                            print("1.Nombre\n2.Apellidos\n3.Numero de tarjeta\n.Email")
                            datos = int(input("Que desea modificar: "))
                            if datos == 1:
                                ab.nombre = (input("Indica el nombre: "))
                            elif datos == 2:
                                ab.apellidos = (input("Indica los apellidos: "))
                            elif datos == 3:
                                ab.num_tarjeta = (input("Indica el número de tarjeta: "))
                            elif datos == 4:
                                ab.email = (input("Indica el email: "))
                        else:
                            print("Saliendo...")
                else:
                    print("No existe tal abonado")
            elif menu_abono == 3:
                ab = 0
                dni = input("Indique su dni: ")
                pin = int(input("Indique su pin: "))
                for a in parking.clientes:
                    if a.plaza.pin == pin and a.dni == dni:
                        ab = a
                if isinstance(ab, Abonado):
                    parking.num_plazas.pop(0)
                    parking.plazas[ab.plaza.id_plaza] = 'libre'
                    parking.clientes.remove(ab)
                else:
                    print("No existe tal abonado.")
            else:
                print("Saliendo...")

    def caducidad_abonos(self, parking=None, lista=None):
        opcion = 1
        lista_caducidad = []
        while opcion != 0:
            print("1. Consultar caducidad de un mes."
                  "\n2. Consultar caducidad de abonos de los últimos 10 días.\n0. Salir")
            opcion = int(input("¿Qué desea hacer?: "))
            if opcion == 1:
                mes = int(input("Indica el mes que desea consultar: "))
                for a in parking.clientes:
                    if isinstance(a, Abonado) and mes == a.abono.fecha_cancelacion.month:
                        lista_caducidad.append(a)
                if len(lista_caducidad) == 0:
                    print("No caduca ningún abono en los últimos 10 días.")
                else:
                    for a in lista_caducidad:
                        print(a)
            elif opcion == 2:
                hoy = datetime.now()
                ultimos_dias = datetime.now() + timedelta(days=10)
                for a in parking.clientes:
                    if isinstance(a, Abonado) and hoy < a.abono.fecha_cancelacion < ultimos_dias:
                        lista_caducidad.append(a)
                if len(lista_caducidad) == 0:
                    print("No caduca ningún abono en los últimos 10 días.")
                else:
                    for a in lista_caducidad:
                        print(a)
            else:
                print("Saliendo...")
