from datetime import datetime
from model.abonado import Abonado


class ClienteService:

    def depositar_vehiculo(self, parking, cliente, lista_plazas):
        if cliente.vehiculo.tipo == 'Turismo':
            for p in lista_plazas:
                if p.estado == 'libre':
                    cliente.plaza = p
            cliente.plaza.estado = 'ocupada'
        elif cliente.vehiculo.tipo == 'Motocicleta':
            for p in lista_plazas:
                if p.estado == 'libre':
                    cliente.plaza = p
            cliente.plaza.estado = 'ocupada'
        else:
            for p in lista_plazas:
                if p.estado == 'libre':
                    cliente.plaza.estado = p
            cliente.plaza = 'ocupada'
        cliente.plaza.fecha_deposito = datetime.now()
        ticket = parking.mostrar_ticket(cliente)
        parking.registro_facturas.append(ticket)

    def retirar_vehiculo(self, lista_clientes, lista_facturas):
        cliente = 0
        factura = dict()
        matricula = input("Introduzca matricula: ")
        id_plaza = int(input("Introduzca id de la plaza: "))
        pin = int(input("Introduzca pin: "))
        for c in lista_clientes:
            if pin == c.pin and id_plaza == c.plaza.id_plaza \
                    and matricula == c.vehiculo.matricula:
                cliente = c
        if cliente in lista_clientes:
            print("La tarifas son las siguientes:\nTurismos 0,12€ por minuto.\nMotocicletas 0,10€ por minuto."
                  "\nMovilidad reducida 0,08€ por minuto.")
            if cliente.vehiculo.tipo == 'Turismo':
                cliente.plaza.estado = 'libre'
                lista_clientes.remove(cliente)
            elif cliente.vehiculo.tipo == 'Motocicleta':
                cliente.plaza.estado = 'libre'
                lista_clientes.remove(cliente)
            else:
                cliente.plaza.estado = 'libre'
                lista_clientes.remove(cliente)
            factura[self.cobrar(cliente)] = datetime.now()
            for k, v in factura.items():
                print("Total pagado: ", k, "€ , Fecha de salida: ", v)
            lista_facturas.append(factura)
        else:
            print("No existe ese cliente.")

    def depositar_abonados(self, lista):
        abonado = 0
        matricula = input("Introduzca matricula: ")
        dni = input("Introduzca dni: ")
        for c in lista:
            if isinstance(c, Abonado):
                if matricula == c.vehiculo.matricula and dni == c.dni:
                    abonado = c
        if abonado in lista:
            abonado.plaza.estado = "abono ocupada"
        else:
            print("No existe tal abonado.")

    def retirar_abonados(self, lista):
        abonado = 0
        matricula = input("Introduzca matricula: ")
        id_plaza = int(input("Introduce el id_plaza: "))
        pin = int(input("Introduce el pin: "))
        for c in lista:
            if matricula == c.vehiculo.matricula and id_plaza == c.plaza.id_plaza and pin == c.pin:
                abonado = c
        if abonado in lista:
            abonado.plaza.estado = 'abono libre'
        else:
            print("No existe tal abonado.")

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
