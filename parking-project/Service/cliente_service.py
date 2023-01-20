from datetime import datetime
from model.abonado import Abonado
from view.view import *


class ClienteService:

    def depositar_vehiculo(self, parking, cliente, lista_plazas):
        it = 0
        salir = False
        while not salir:
            if cliente.vehiculo.tipo == 'Turismo':
                if lista_plazas[it].estado == 'libre' \
                        and parking.plazas_disponibles['Turismo'] > 0:
                    cliente.plaza = lista_plazas[it]
                    parking.plazas_disponibles['Turismo'] -= 1
                    salir = True
            elif cliente.vehiculo.tipo == 'Motocicleta'\
                    and parking.plazas_disponibles['Motocicleta'] > 0:
                if lista_plazas[it].estado == 'libre':
                    cliente.plaza = lista_plazas[it]
                    parking.plazas_disponibles['Motocicleta'] -= 1
                    salir = True
            else:
                if lista_plazas[it].estado == 'libre'\
                        and parking.plazas_disponibles['Movilidad reducida'] > 0:
                    cliente.plaza = lista_plazas[it]
                    parking.plazas_disponibles['Movilidad reducida'] -= 1
                    salir = True
            lista_plazas[it].fecha_deposito = datetime.now()
            it += 1
        cliente.plaza.estado = 'ocupada'
        cliente.plaza.fecha_deposito = datetime.now()
        ticket = parking.mostrar_ticket(cliente)
        parking.registro_facturas.append(ticket)

    def retirar_vehiculo(self, parking, lista_clientes, lista_facturas, cliente, lista_plazas):
        retirado = False
        factura = dict()
        it = 0
        salir = False
        for c in lista_clientes:
            if not isinstance(c, Abonado):
                if cliente.pin == c.pin and cliente.plaza.id_plaza == c.plaza.id_plaza \
                        and cliente.vehiculo.matricula.upper() == c.vehiculo.matricula.upper():
                    cliente = c
        if cliente in lista_clientes:
            while not salir:
                if lista_plazas[it].id_plaza == cliente.plaza.id_plaza:
                    lista_plazas[it].estado = 'libre'
                    salir = True
                it += 1
            if cliente.vehiculo.tipo == 'Turismo':
                parking.plazas_disponibles['Turismo'] += 1
            elif cliente.vehiculo.tipo == 'Motocicleta':
                parking.plazas_disponibles['Motocicleta'] += 1
            else:
                parking.plazas_disponibles['Movilidad reducida'] += 1
            lista_clientes.remove(cliente)
            factura[self.cobrar(cliente)] = datetime.now()
            imprimir_factura(factura)
            lista_facturas.append(factura)
            retirado = True
            return retirado
        else:
            return retirado

    def depositar_abonados(self, lista_clientes, abonado, lista_plazas):
        it = 0
        salir = False
        depositado = False
        for c in lista_clientes:
            if isinstance(c, Abonado):
                if abonado.vehiculo.matricula.upper() == c.vehiculo.matricula.upper() \
                        and abonado.dni.upper() == c.dni.upper():
                    abonado = c
        if abonado in lista_clientes and abonado.plaza.estado == 'abono libre':
            if datetime.now() < abonado.abono.fecha_cancelacion:
                while not salir:
                    if lista_plazas[it].id_plaza == abonado.plaza.id_plaza:
                        lista_plazas[it].estado = 'abono ocupada'
                        abonado.plaza.estado = "abono ocupada"
                        salir = True
                    it += 1
                depositado = True
                return depositado
            else:
                return depositado
        else:
            return depositado

    def retirar_abonados(self, lista_clientes, abonado, lista_plazas):
        it = 0
        salir = False
        retirado = False
        for c in lista_clientes:
            if abonado.vehiculo.matricula.upper() == c.vehiculo.matricula.upper() \
                    and abonado.plaza.id_plaza == c.plaza.id_plaza \
                    and abonado.pin == c.pin:
                abonado = c
        if abonado in lista_clientes and abonado.plaza.estado == 'abono ocupada':
            while not salir:
                if lista_plazas[it].id_plaza == abonado.plaza.id_plaza:
                    lista_plazas[it].estado = 'abono libre'
                    abonado.plaza.estado = "abono libre"
                    salir = True
                it += 1
            retirado = True
            return retirado
        else:
            return retirado

    def cobrar(self, cliente):
        fecha_salida = datetime.now()
        if cliente.vehiculo.tipo == 'Turismo':
            diferencia = fecha_salida - cliente.plaza.fecha_deposito
            minutos_diferencia = diferencia.total_seconds() / 60
            factura = minutos_diferencia * 0.12
        elif cliente.vehiculo.tipo == 'Motocicleta':
            diferencia = fecha_salida - cliente.plaza.fecha_deposito
            minutos_diferencia = diferencia.total_seconds() / 60
            factura = minutos_diferencia * 0.08
        else:
            diferencia = fecha_salida - cliente.plaza.fecha_deposito
            minutos_diferencia = diferencia.total_seconds() / 60
            factura = minutos_diferencia * 0.12
        return round(factura, 2)
