import pickle
from datetime import datetime
from model.abonado import Abonado
from model.abono import Abono
from model.cliente import Cliente
from model.parking import Parking
from model.plaza import Plaza
from model.vehiculo import Vehiculo
from view.view import *


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

    abono1 = Abono(tipo='Mensual', factura=25, fecha_activacion=datetime(2022, 12, 25, 10, 15, 00, 00000),
                   fecha_cancelacion=datetime(2023, 1, 25, 10, 15, 00, 00000))
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
    pk = Parking(plazas_totales=40, registro_facturas=[])
    parking = pk


def cargar_clientes():
    clientes = open('files/clientes.pckl', 'rb')
    lista_clientes = pickle.load(clientes)
    clientes.close()
    return lista_clientes


def cargar_vehiculos():
    vehiculos = open('files/vehiculos.pckl', 'rb')
    lista_vehiculos = pickle.load(vehiculos)
    vehiculos.close()
    return lista_vehiculos


def cargar_plazas():
    plazas = open('files/plazas.pckl', 'rb')
    lista_plazas = pickle.load(plazas)
    plazas.close()
    return lista_plazas


def cargar_abonos():
    abonos = open('files/abonos.pckl', 'rb')
    lista_abonos = pickle.load(abonos)
    abonos.close()
    return lista_abonos


def cargar_facturas():
    cobros_cliente = open('files/facturas_cliente.pckl', 'rb')
    lista_cobros_cliente = pickle.load(cobros_cliente)
    cobros_cliente.close()
    return lista_cobros_cliente


def comprobar_abonado_modificado():
    dni = input("Indique su dni: ")
    try:
        pin = int(input("Indique su pin: "))
        return Abonado(dni=dni, pin=pin)
    except ValueError:
        return Abonado(dni=dni, pin=0)


def comprobar_cliente(lista_clientes):
    matricula = input("Introduzca matricula: ")
    try:
        id_plaza = int(input("Introduzca id de la plaza: "))
        pin = int(input("Introduzca pin: "))
        return Cliente(vehiculo=Vehiculo(matricula=matricula),
                       plaza=Plaza(id_plaza=id_plaza), pin=pin)
    except ValueError:
        return Cliente(vehiculo=Vehiculo(matricula=matricula),
                       plaza=Plaza(id_plaza=0), pin=0)


def comprobar_abonados_retiro():
    matricula = input("Introduzca matricula: ")
    try:
        id_plaza = int(input("Introduzca id de la plaza: "))
        pin = int(input("Introduzca pin: "))
        return Abonado(vehiculo=Vehiculo(matricula=matricula),
                       plaza=Plaza(id_plaza=id_plaza), pin=pin)
    except ValueError:
        return Abonado(vehiculo=Vehiculo(matricula=matricula),
                       plaza=Plaza(id_plaza=0), pin=0)


def crear_abonado_alta(lista_clientes):
    nombre = input("Introduzca su nombre: ")
    apellidos = input("Introduzca su apellido: ")
    num_tarjeta = input("Introduzca su número de tarjeta: ")
    email = input("Introduzca su email: ")
    dni = input("Introduzca su dni: ")
    matricula = input("Indique la matricula: ")
    print("Seleccione su tipo de vehículo: ")
    tipo = asignar_tipo()
    if not comprobar_dni(dni, lista_clientes) and not comprobar_matricula(matricula, lista_clientes):
        v1 = Vehiculo(matricula=matricula, tipo=tipo)
        ab = Abonado(nombre=nombre, apellidos=apellidos, num_tarjeta=num_tarjeta, email=email,
                     dni=dni, vehiculo=v1, pin=random.randint(100000, 999999))
        return ab
    else:
        return None


def comprobar_abonados_deposito():
    matricula = input("Introduzca matricula: ")
    dni = input("Introduzca dni: ")
    return Abonado(vehiculo=Vehiculo(matricula=matricula),
                   dni=dni)
