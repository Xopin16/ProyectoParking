from datetime import datetime, timedelta
import random
from model.abonado import Abonado
from model.abono import Abono
from model.vehiculo import Vehiculo
from view.view import *


class AdminService:

    def controlar_estado_parking(self, parking, lista):
        parking.mostrar_plazas(lista)

    def mostrar_facturacion(self, lista_facturas):
        print("Indique la primera fecha: ")
        fecha1 = datetime(int(input("Año: ")), int(input("Mes: ")), int(input("Dia: ")), int(input("Hora: ")))
        print("Indique la segunda fecha: ")
        fecha2 = datetime(int(input("Año: ")), int(input("Mes: ")), int(input("Dia: ")), int(input("Hora: ")))
        cont = 0
        for cobro in lista_facturas:
            for k, v in cobro.items():
                if fecha1 < v < fecha2:
                    cont += 1
                    print("Total pagado: ", k, "€, Fecha de salida: ", v)
        if cont == 0:
            print("No hay resgistro de facturas entre esas fechas.")

    def consular_abonados(self, lista_clientes):
        total_tipo = [0, 0, 0, 0]
        tipo_abono = ['Mensual', 'Trimestral', 'Semestral', 'Anual']
        factura_abonos = dict(zip(tipo_abono, total_tipo))
        for a in lista_clientes:
            if isinstance(a, Abonado):
                if a.abono.tipo == 'Mensual':
                    factura_abonos['Mensual'] += a.abono.factura
                elif a.abono.tipo == 'Trimestral':
                    factura_abonos['Trimestral'] += a.abono.factura
                elif a.abono.tipo == 'Semestral':
                    factura_abonos['Semestral'] += a.abono.factura
                else:
                    factura_abonos['Anual'] += a.abono.factura
        for k, v in factura_abonos.items():
            print("Tipo de abono: ", k, ", Cobro total: ", v, "€")

    def gestion_abonos(self, lista_clientes, lista_plazas, lista_abonos):
        menu_abono = 1
        cambio = 1
        tipo_abono = ['Mensual', 'Trimestral', 'Semestral', 'Anual']
        while menu_abono != 0:
            imprimir_menu_abono()
            menu_abono = int(input("¿Qué desea hacer?: "))
            if menu_abono == 1:
                nombre = input("Introduzca su nombre: ")
                apellidos = input("Introduzca su apellido: ")
                num_tarjeta = input("Introduzca su número de tarjeta: ")
                email = input("Introduzca su email: ")
                dni = input("Introduzca su dni: ")
                v1 = Vehiculo(matricula="1111AB", tipo="Turismo")
                ab = Abonado(nombre=nombre, apellidos=apellidos, num_tarjeta=num_tarjeta, email=email,
                             dni=dni, abono=None, vehiculo=v1, plaza=None, pin=random.randint(100000, 999999))
                for p in lista_plazas:
                    if p.estado == 'libre':
                        ab.plaza = p
                imprimir_tipos_abono()
                opcion_abono = int(input("Elija el tipo de abono: "))
                if opcion_abono == 1:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=30)
                    a = Abono(tipo=tipo_abono[0], factura=25, fecha_activacion=fecha_activacion,
                              fecha_cancelacion=fecha_cancelacion)
                    ab.abono = a
                elif tipo_abono == 2:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=90)
                    a = Abono(tipo=tipo_abono[1], factura=70, fecha_activacion=fecha_activacion,
                              fecha_cancelacion=fecha_cancelacion)
                    ab.abono = a
                elif tipo_abono == 3:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=180)
                    a = Abono(tipo=tipo_abono[2], factura=130, fecha_activacion=fecha_activacion,
                              fecha_cancelacion=fecha_cancelacion)
                    ab.abono = a
                else:
                    fecha_activacion = datetime.now()
                    fecha_cancelacion = datetime.now() + timedelta(days=365)
                    a = Abono(tipo=tipo_abono[3], factura=200, fecha_activacion=fecha_activacion,
                              fecha_cancelacion=fecha_cancelacion)
                    ab.abono = a
                lista_clientes.append(ab)
                ab.plaza.estado = 'abono ocupada'
                lista_abonos.append(a)
            elif menu_abono == 2:
                ab = 0
                dni = input("Indique su dni: ")
                pin = int(input("Indique su pin: "))
                for a in lista_clientes:
                    if a.pin == pin and a.dni == dni:
                        ab = a
                if isinstance(ab, Abonado):
                    while cambio != 0:
                        print("1.Modificar tipo de abono.")
                        print("2.Modificar datos personales.")
                        cambio = int(input("¿Que desea modificar?: "))
                        if cambio == 1:
                            imprimir_tipos_abono()
                            new_tipo = int(input("Indica el tipo de abono al que desea cambiar: "))
                            if new_tipo == 1:
                                ab.abono.tipo = tipo_abono[0]
                                ab.abono.factura += 25
                                ab.abono.fecha_activacion = datetime.now()
                                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=30)
                            elif new_tipo == 2:
                                ab.abono.tipo = tipo_abono[1]
                                ab.abono.factura += 70
                                ab.abono.fecha_activacion = datetime.now()
                                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=90)
                            elif new_tipo == 3:
                                ab.abono.tipo = tipo_abono[2]
                                ab.abono.factura += 130
                                ab.abono.fecha_activacion = datetime.now()
                                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=180)
                            else:
                                ab.abono.tipo = tipo_abono[3]
                                ab.abono.factura += 200
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
                for a in lista_clientes:
                    if a.pin == pin and a.dni == dni:
                        ab = a
                if isinstance(ab, Abonado):
                    ab.plaza.estado = 'libre'
                    lista_clientes.remove(ab)
                else:
                    print("No existe tal abonado.")
            else:
                print("Saliendo...")

    def caducidad_abonos(self, lista_clientes):
        opcion = 1
        lista_caducidad = []
        while opcion != 0:
            print("1. Consultar caducidad de un mes."
                  "\n2. Consultar caducidad de abonos de los últimos 10 días.\n0. Salir")
            opcion = int(input("¿Qué desea hacer?: "))
            if opcion == 1:
                mes = int(input("Indica el mes que desea consultar: "))
                for a in lista_clientes:
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
                for a in lista_clientes:
                    if isinstance(a, Abonado) and hoy < a.abono.fecha_cancelacion < ultimos_dias:
                        lista_caducidad.append(a)
                if len(lista_caducidad) == 0:
                    print("No caduca ningún abono en los últimos 10 días.")
                else:
                    for a in lista_caducidad:
                        print(a)
            else:
                print("Saliendo...")
