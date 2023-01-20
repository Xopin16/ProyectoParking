from datetime import datetime, timedelta
import random

from model.abonado import Abonado
from model.cliente import Cliente
from model.plaza import Plaza
from model.vehiculo import Vehiculo


def imprimir_menu_cliente():
    print("1. Depositar vehiculo")
    print("2. Retirar vehiculo")
    print("3. Depositar abonados")
    print("4. Retirar abonados")
    print("0. Para salir")


def imprimir_menu_admin():
    print("1. Consultar estado parking")
    print("2. Mostrar registro de facturas entre dos fechas")
    print("3. Consultar abonos")
    print("4. Gestionar abonos")
    print("5. Consultar caducidad de abonos")
    print("0. Para salir")


def imprimir_datos_modificar():
    try:
        print("1.Nombre.")
        print("2.Apellidos.")
        print("3.Numero de tarjeta.")
        print("4.Email.")
        datos = int(input("Que desea modificar: "))
        return datos
    except ValueError:
        print("Por favor, introduzca un número valido.")


def imprimir_tarifas():
    print("Las tarifas son las siguientes:")
    print("Turismos 0,12€ por minuto.")
    print("Motocicletas 0,10€ por minuto.")
    print("Movilidad reducida 0,08€ por minuto.")


# def comprobar_cliente():
#     matricula = input("Introduzca matricula: ")
#     try:
#         id_plaza = int(input("Introduzca id de la plaza: "))
#         pin = int(input("Introduzca pin: "))
#         return Cliente(vehiculo=Vehiculo(matricula=matricula),
#                        plaza=Plaza(id_plaza=id_plaza), pin=pin)
#     except ValueError:
#         return Cliente(vehiculo=Vehiculo(matricula=matricula),
#                        plaza=Plaza(id_plaza=0), pin=0)


# def comprobar_abonados_deposito():
#     matricula = input("Introduzca matricula: ")
#     dni = input("Introduzca dni: ")
#     return Abonado(vehiculo=Vehiculo(matricula=matricula),
#                    dni=dni)


# def comprobar_abonados_retiro():
#     matricula = input("Introduzca matricula: ")
#     try:
#         id_plaza = int(input("Introduzca id de la plaza: "))
#         pin = int(input("Introduzca pin: "))
#         return Abonado(vehiculo=Vehiculo(matricula=matricula),
#                        plaza=Plaza(id_plaza=id_plaza), pin=pin)
#     except ValueError:
#         return Abonado(vehiculo=Vehiculo(matricula=matricula),
#                        plaza=Plaza(id_plaza=0), pin=0)


def imprimir_factura(factura):
    # for i in lista_facturas:
    for k, v in factura.items():
        print("***************************************")
        print("Total pagado: ", k, "€ , Fecha de salida: ", v)
        print("***************************************")


def imprimir_lista_facturas(lista_facturas, fecha1, fecha2):
    for i in lista_facturas:
        for k, v in i.items():
            if fecha1 < v < fecha2:
                print("***************************************")
                print("Total pagado: ", k, "€ , Fecha de salida: ", v)
                print("***************************************")


def generar_fecha():
    try:
        fecha = datetime(int(input("Año: ")), int(input("Mes: ")), int(input("Dia: ")), int(input("Hora: ")))
        return fecha
    except ValueError:
        print("Por favor, introduzca un fecha valida con números enteros.")


def mostrar_abonados(lista_clientes):
    for a in lista_clientes:
        if isinstance(a, Abonado):
            a.mostrar_clientes()


def imprimir_menu_caducidad():
    try:
        print("1. Consultar caducidad de un mes.")
        print("2. Consultar caducidad de abonos de los últimos 10 días.")
        print("0. Salir")
        opcion = int(input("¿Qué desea hacer?: "))
        return opcion
    except ValueError:
        print("Por favor, introduzca un número valido")


def mostrar_abonados_mes(lista_clientes, mes):
    lista_caducidad = []
    for a in lista_clientes:
        if isinstance(a, Abonado) and mes == a.abono.fecha_cancelacion.month:
            lista_caducidad.append(a)
    mostrar_abonados(lista_caducidad)


def mostrar_abonos_proximos(lista_clientes):
    lista_caducidad = []
    hoy = datetime.now()
    ultimos_dias = datetime.now() + timedelta(days=10)
    for a in lista_clientes:
        if isinstance(a, Abonado) and hoy < a.abono.fecha_cancelacion < ultimos_dias:
            lista_caducidad.append(a)
    mostrar_abonados(lista_caducidad)


def imprimir_menu_abono():
    try:
        print("1. Alta de abono")
        print("2. Modificar abono")
        print("3. Baja de abono")
        print("Pulsa cualquier 0 para salir")
        menu_abono = int(input("¿Qué desea hacer?: "))
        return menu_abono
    except ValueError:
        print("Por favor, introduzca un número valido.")


def imprimir_tipos_abono():
    try:
        print("1. Mensual(20€)")
        print("2. Trimestral(70€)")
        print("3. Semestral(130€)")
        print("4. Anual(200€)")
        print("0. Para salir")
        opcion_abono = int(input("Elija el tipo de abono: "))
        return opcion_abono
    except ValueError:
        print("Por favor, introduzca un número valido.")


# def crear_abonado_alta(lista_clientes):
#     nombre = input("Introduzca su nombre: ")
#     apellidos = input("Introduzca su apellido: ")
#     num_tarjeta = input("Introduzca su número de tarjeta: ")
#     email = input("Introduzca su email: ")
#     dni = input("Introduzca su dni: ")
#     matricula = input("Indique la matricula: ")
#     print("Seleccione su tipo de vehículo: ")
#     tipo = asignar_tipo()
#     if tipo == 'No encontrado':
#         return None
#     else:
#         if comprobar_dni(dni, lista_clientes) and comprobar_matricula(matricula, lista_clientes):
#             v1 = Vehiculo(matricula=matricula, tipo=tipo)
#             ab = Abonado(nombre=nombre, apellidos=apellidos, num_tarjeta=num_tarjeta, email=email,
#                          dni=dni, vehiculo=v1, pin=random.randint(100000, 999999))
#             return ab
#         else:
#             return None


def asignar_tipo():
    tipo_vehiculo = ['Turismo', 'Motocicleta', 'Movilidad reducida', 'No encontrado']
    try:
        print("1. Turismo")
        print("2. Motocicleta")
        print("3. Movilidad reducida")
        tipo = int(input("Indique el tipo de vehículo: "))
        if tipo == 1:
            return tipo_vehiculo[0]
        elif tipo == 2:
            return tipo_vehiculo[1]
        else:
            return tipo_vehiculo[2]
    except ValueError:
        return tipo_vehiculo[3]


def comprobar_dni(dni, lista_clientes):
    existe = True
    for i in lista_clientes:
        if isinstance(i, Abonado):
            if dni == i.dni:
                existe = False

    return existe


def comprobar_matricula(matricula, lista_clientes):
    existe = True
    for i in lista_clientes:
        if matricula == i.vehiculo.matricula:
            existe = False
    return existe


def imprimir_opcion_modificar():
    try:
        print("1.Modificar tipo de abono.")
        print("2.Modificar datos personales.")
        cambio = int(input("¿Que desea modificar?: "))
        return cambio
    except ValueError:
        print("Por favor, introduzca un número valido.")


# def comprobar_abonado_modificado():
#     dni = input("Indique su dni: ")
#     try:
#         pin = int(input("Indique su pin: "))
#         return Abonado(dni=dni, pin=pin)
#     except ValueError:
#         return Abonado(dni=dni, pin=0)
