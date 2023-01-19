import pickle
from datetime import datetime
from model.abonado import Abonado
from model.abono import Abono
from model.cliente import Cliente
from model.parking import Parking
from model.plaza import Plaza
from model.vehiculo import Vehiculo


def guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, parking, lista_cobros_cliente):
    clientes = open('files/clientes.pckl', 'wb')
    pickle.dump(lista_clientes, clientes)
    clientes.close()

    vehiculos = open('files/vehiculos.pckl', 'wb')
    pickle.dump(lista_vehiculos, vehiculos)
    vehiculos.close()

    plazas = open('files/plazas.pckl', 'wb')
    pickle.dump(lista_plazas, plazas)
    plazas.close()

    abonos = open('files/abonos.pckl', 'wb')
    pickle.dump(lista_abonos, abonos)
    abonos.close()

    tickets_cliente = open('files/facturas_cliente.pckl', 'wb')
    pickle.dump(parking.registro_facturas, tickets_cliente)
    tickets_cliente.close()

    cobros_cliente = open('files/facturas_cliente.pckl', 'wb')
    pickle.dump(lista_cobros_cliente, cobros_cliente)
    cobros_cliente.close()


def cargar_datos(lista_plazas, lista_vehiculos, lista_abonos, lista_clientes, lista_cobros_cliente, pk):
    plaza1 = Plaza(id_plaza=1, estado='ocupada', fecha_deposito=datetime(2023, 1, 1, 10, 15, 00, 00000))
    plaza2 = Plaza(id_plaza=2, estado='ocupada', fecha_deposito=datetime(2023, 1, 2, 10, 15, 00, 00000))
    plaza3 = Plaza(id_plaza=3, estado='ocupada', fecha_deposito=datetime(2023, 1, 3, 10, 15, 00, 00000))
    plaza4 = Plaza(id_plaza=4, estado='abono ocupada')
    plaza5 = Plaza(id_plaza=5, estado='abono ocupada')
    plazas = [plaza1, plaza2, plaza3, plaza4, plaza5]
    for i in plazas:
        lista_plazas.append(i)

    v1 = Vehiculo(matricula='1111A', tipo='Turismo')
    v2 = Vehiculo(matricula='1111B', tipo='Turismo')
    v3 = Vehiculo(matricula='1111C', tipo='Motocicleta')
    v4 = Vehiculo(matricula='1111D', tipo='Motocicleta')
    v5 = Vehiculo(matricula='1111F', tipo='Movilidad reducida')
    vehiculos = [v1, v2, v3, v4, v5]
    for i in vehiculos:
        lista_vehiculos.append(i)

    abono1 = Abono(tipo='Mensual', factura=25, fecha_activacion=datetime(2023, 1, 1, 10, 15, 00, 00000),
                   fecha_cancelacion=datetime(2023, 2, 1, 10, 15, 00, 00000))
    abono2 = Abono(tipo='Anual', factura=200, fecha_activacion=datetime(2023, 1, 1, 10, 15, 00, 00000),
                   fecha_cancelacion=datetime(2024, 1, 1, 10, 15, 00, 00000))
    abonos = [abono1, abono2]
    for i in abonos:
        lista_abonos.append(i)

    c1 = Cliente(vehiculo=v1, plaza=plaza1, pin=111111)
    c2 = Cliente(vehiculo=v2, plaza=plaza2, pin=111112)
    c3 = Cliente(vehiculo=v3, plaza=plaza3, pin=111113)

    ab1 = Abonado(nombre='Pedro', apellidos='Benito', num_tarjeta=1111, email='pedro@gmail.com', dni='dni1',
                  abono=abono1, vehiculo=v4, plaza=plaza4, pin=211111)
    ab2 = Abonado(nombre='Paco', apellidos='Pérez', num_tarjeta=2222, email='paco@gmail.com', dni='dni2',
                  abono=abono2, vehiculo=v5, plaza=plaza5, pin=211112)
    clientes = [c1, c2, c3, ab1, ab2]
    for i in clientes:
        lista_clientes.append(i)
    cobros = []
    for i in cobros:
        lista_cobros_cliente.append(i)
    pk = Parking(plazas_totales=40, clientes=[c1, c2, c3, ab1, ab2], registro_facturas=[])
    parking = pk


def cargar_datos_prueba(parking):
    clientes = open('files/clientes.pckl', 'rb')
    lista_clientes = pickle.load(clientes)
    clientes.close()

    vehiculos = open('files/vehiculos.pckl', 'rb')
    lista_vehiculos = pickle.load(vehiculos)
    vehiculos.close()

    plazas = open('files/plazas.pckl', 'rb')
    lista_plazas = pickle.load(plazas)
    plazas.close()

    abonos = open('files/abonos.pckl', 'rb')
    lista_abonos = pickle.load(abonos)
    abonos.close()

    tickets_cliente = open('files/facturas_cliente.pckl', 'rb')
    lista_tickets = pickle.load(tickets_cliente)
    tickets_cliente.close()

    cobros_cliente = open('files/facturas_cliente.pckl', 'rb')
    lista_cobros_cliente = pickle.load(cobros_cliente)
    cobros_cliente.close()
