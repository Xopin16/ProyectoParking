from datetime import datetime
from model.abonado import Abonado
from view.view import *


class ClienteService:

    def depositar_vehiculo(self, parking, cliente, lista_plazas):
        it = 0
        salir = False
        while not salir:
            if cliente.vehiculo.tipo == 'Turismo':
                if lista_plazas[it].estado == 'libre':
                    cliente.plaza = lista_plazas[it]
                    salir = True
            elif cliente.vehiculo.tipo == 'Motocicleta':
                if lista_plazas[it].estado == 'libre':
                    cliente.plaza = lista_plazas[it]
                    salir = True
            else:
                if lista_plazas[it].estado == 'libre':
                    cliente.plaza = lista_plazas[it]
                    salir = True
            it += 1
        cliente.plaza.estado = 'ocupada'
        cliente.plaza.fecha_deposito = datetime.now()
        ticket = parking.mostrar_ticket(cliente)
        parking.registro_facturas.append(ticket)

    def retirar_vehiculo(self, lista_clientes, lista_facturas, cliente, lista_plazas):
        retirado = False
        factura = dict()
        it = 0
        salir = False
        for c in lista_clientes:
            if cliente.pin == c.pin and cliente.plaza.id_plaza == c.plaza.id_plaza \
                    and cliente.vehiculo.matricula == c.vehiculo.matricula:
                cliente = c
        if cliente in lista_clientes:
            while not salir:
                if lista_plazas[it].id_plaza == cliente.plaza.id_plaza:
                    lista_plazas[it].estado = 'libre'
                    salir=True
                it += 1
            imprimir_tarifas()
            if cliente.vehiculo.tipo == 'Turismo':
                lista_clientes.remove(cliente)
            elif cliente.vehiculo.tipo == 'Motocicleta':
                lista_clientes.remove(cliente)
            else:
                lista_clientes.remove(cliente)
            factura[self.cobrar(cliente)] = datetime.now()
            imprimir_factura(factura)
            lista_facturas.append(factura)
            retirado = True
            return retirado
        else:
            return retirado

    def depositar_abonados(self, lista_clientes, abonado):
        # CAMBIAR ESTADO PLAZAS AQUI
        depositado = False
        for c in lista_clientes:
            if isinstance(c, Abonado):
                if abonado.vehiculo.matricula == c.vehiculo.matricula and abonado.dni == c.dni:
                    abonado = c
        if abonado in lista_clientes:
            if datetime.now() < abonado.abono.fecha_cancelacion:
                abonado.plaza.estado = "abono ocupada"
                depositado = True
                return depositado
            else:
                return depositado
        else:
            return depositado

    def retirar_abonados(self, lista_clientes, abonado):
        # CAMBIAR ESTADO PLAZAS AQUI
        retirado = False
        for c in lista_clientes:
            if abonado.vehiculo.matricula == c.vehiculo.matricula \
                    and abonado.plaza.id_plaza == c.plaza.id_plaza \
                    and abonado.pin == c.pin:
                abonado = c
        if abonado in lista_clientes:
            abonado.plaza.estado = 'abono libre'
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
