from datetime import datetime, timedelta
import random
from model.abonado import Abonado
from model.abono import Abono
from model.vehiculo import Vehiculo
from view.view import *


class AdminService:

    def controlar_estado_parking(self, parking, lista):
        parking.mostrar_plazas(lista)

    def comprobar_facturacion(self, lista_facturas, fecha1, fecha2):
        registro = False
        cont = 0
        for cobro in lista_facturas:
            for k, v in cobro.items():
                if fecha1 < v < fecha2:
                    cont += 1
        if cont != 0:
            registro = True
            return registro
        else:
            return registro

    def consultar_abonados(self, lista_clientes):
        cont = 0
        registrado = False
        for a in lista_clientes:
            if isinstance(a, Abonado):
                cont += 1
        if cont != 0:
            registrado = True
            return registrado
        else:
            return registrado

    def alta_abonado(self, parking, ab, lista_cliente, lista_abonos, lista_plazas, opcion_abono):
        alta = False
        tipo_abono = ['Mensual', 'Trimestral', 'Semestral', 'Anual']
        salir = False
        it = 0
        while not salir:
            if ab.vehiculo.tipo == 'Turismo':
                if lista_plazas[it].estado == 'libre' \
                        and parking.plazas_disponibles['Turismo'] > 0:
                    ab.plaza = lista_plazas[it]
                    # parking.plazas_disponibles['Turismo'] -= 1
                    salir = True
            elif ab.vehiculo.tipo == 'Motocicleta'\
                    and parking.plazas_disponibles['Motocicleta'] > 0:
                if lista_plazas[it].estado == 'libre':
                    ab.plaza = lista_plazas[it]
                    # parking.plazas_disponibles['Motocicleta'] -= 1
                    salir = True
            else:
                if lista_plazas[it].estado == 'libre'\
                        and parking.plazas_disponibles['Movilidad reducida'] > 0:
                    ab.plaza = lista_plazas[it]
                    # parking.plazas_disponibles['Movilidad reducida'] -= 1
                    salir = True
            lista_plazas[it].fecha_deposito = datetime.now()
            it += 1
        if opcion_abono == 1:
            fecha_activacion = datetime.now()
            fecha_cancelacion = datetime.now() + timedelta(days=30)
            a = Abono(tipo=tipo_abono[0], factura=25, fecha_activacion=fecha_activacion,
                      fecha_cancelacion=fecha_cancelacion)
            lista_cliente.append(ab)
            ab.plaza.estado = 'abono ocupada'
            lista_abonos.append(a)
            ab.abono = a
            alta = True
        elif opcion_abono == 2:
            fecha_activacion = datetime.now()
            fecha_cancelacion = datetime.now() + timedelta(days=90)
            a = Abono(tipo=tipo_abono[1], factura=70, fecha_activacion=fecha_activacion,
                      fecha_cancelacion=fecha_cancelacion)
            ab.abono = a
            lista_cliente.append(ab)
            ab.plaza.estado = 'abono ocupada'
            lista_abonos.append(a)
            alta = True
        elif opcion_abono == 3:
            fecha_activacion = datetime.now()
            fecha_cancelacion = datetime.now() + timedelta(days=180)
            a = Abono(tipo=tipo_abono[2], factura=130, fecha_activacion=fecha_activacion,
                      fecha_cancelacion=fecha_cancelacion)
            ab.abono = a
            lista_cliente.append(ab)
            ab.plaza.estado = 'abono ocupada'
            lista_abonos.append(a)
            alta = True
        elif opcion_abono == 4:
            fecha_activacion = datetime.now()
            fecha_cancelacion = datetime.now() + timedelta(days=365)
            a = Abono(tipo=tipo_abono[3], factura=200, fecha_activacion=fecha_activacion,
                      fecha_cancelacion=fecha_cancelacion)
            ab.abono = a
            lista_cliente.append(ab)
            ab.plaza.estado = 'abono ocupada'
            lista_abonos.append(a)
            alta = True
        else:
            return alta
        return alta

    def modificar_tipo_abono(self, ab, opcion, lista_clientes):
        tipo_abono = ['Mensual', 'Trimestral', 'Semestral', 'Anual']
        registrado = False
        for c in lista_clientes:
            if isinstance(c, Abonado):
                if ab.dni.upper() == c.dni.upper() and ab.pin == c.pin:
                    ab = c
        if ab in lista_clientes:
            if opcion == 1:
                ab.abono.tipo = tipo_abono[0]
                ab.abono.factura += 25
                ab.abono.fecha_activacion = datetime.now()
                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=30)
                registrado = True
            elif opcion == 2:
                ab.abono.tipo = tipo_abono[1]
                ab.abono.factura += 70
                ab.abono.fecha_activacion = datetime.now()
                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=90)
                registrado = True
            elif opcion == 3:
                ab.abono.tipo = tipo_abono[2]
                ab.abono.factura += 130
                ab.abono.fecha_activacion = datetime.now()
                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=180)
                registrado = True
            elif opcion == 4:
                ab.abono.tipo = tipo_abono[3]
                ab.abono.factura += 200
                ab.abono.fecha_activacion = datetime.now()
                ab.abono.fecha_cancelacion = datetime.now() + timedelta(days=365)
                registrado = True
            else:
                registrado = False
            return registrado
        else:
            return registrado

    def modificar_datos_abonado(self, ab, datos, lista_clientes):
        hoy = datetime.now()
        registrado = False
        for c in lista_clientes:
            if isinstance(c, Abonado):
                if ab.dni.upper() == c.dni.upper() and ab.pin == c.pin:
                    ab = c
        if ab in lista_clientes and hoy < ab.abono.fecha_cancelacion:
            if datos == 1:
                ab.nombre = (input("Indica el nombre: "))
                registrado = True
            elif datos == 2:
                ab.apellidos = (input("Indica los apellidos: "))
                registrado = True
            elif datos == 3:
                ab.num_tarjeta = (input("Indica el n??mero de tarjeta: "))
                registrado = True
            elif datos == 4:
                ab.email = (input("Indica el email: "))
                registrado = True
            else:
                registrado = False
            return registrado
        else:
            return registrado

    def baja_abonado(self, parking, ab, lista_clientes, lista_plazas):
        hoy = datetime.now()
        it = 0
        salir = False
        registrado = False
        for c in lista_clientes:
            if isinstance(c, Abonado):
                if ab.dni.upper() == c.dni.upper() and ab.pin == c.pin:
                    ab = c
        if ab in lista_clientes and hoy < ab.abono.fecha_cancelacion:
            while not salir:
                if lista_plazas[it].id_plaza == ab.plaza.id_plaza:
                    lista_plazas[it].estado = 'libre'
                    ab.plaza.estado = 'libre'
                    salir = True
                it += 1
            if ab.vehiculo.tipo == 'Turismo':
                parking.plazas_disponibles['Turismo'] += 1
            elif ab.vehiculo.tipo == 'Motocicleta':
                parking.plazas_disponibles['Motocicleta'] += 1
            else:
                parking.plazas_disponibles['Movilidad reducida'] += 1
            lista_clientes.remove(ab)
            registrado = True
            return registrado
        else:
            return registrado

    def comprobar_abonos_mes(self, lista_clientes, mes):
        lista_caducidad = []
        caducado = False
        for a in lista_clientes:
            if isinstance(a, Abonado) and mes == a.abono.fecha_cancelacion.month:
                lista_caducidad.append(a)
        if len(lista_caducidad) == 0:
            return caducado
        else:
            caducado = True
            return caducado

    def comprobar_abonos_proximos(self, lista_clientes):
        lista_caducidad = []
        caducado = False
        hoy = datetime.now()
        ultimos_dias = datetime.now() + timedelta(days=10)
        for a in lista_clientes:
            if isinstance(a, Abonado) and hoy < a.abono.fecha_cancelacion < ultimos_dias:
                lista_caducidad.append(a)
        if len(lista_caducidad) == 0:
            return caducado
        else:
            caducado = True
            return caducado

    def mostrar_clientes_abonados(self, lista_clientes):
        imprimir_clientes(lista_clientes)


