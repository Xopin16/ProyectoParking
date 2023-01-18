from model import cliente
from service.parking_service import *
from view.view import *
from model.abonado import Abonado
import pickle
from model.abono import Abono
from model.cliente import Cliente
from model.parking import Parking
from model.plaza import Plaza
from model.vehiculo import Vehiculo

ParkingService = ParkingService()

plaza1 = Plaza(id_plaza=1, pin=111111, fecha_deposito=datetime(2022, 12, 1, 10, 15, 00, 00000),
               fecha_salida=datetime.now(), estado='ocupada')
plaza2 = Plaza(id_plaza=2, pin=111112, fecha_deposito=datetime(2022, 12, 2, 10, 15, 00, 00000),
               fecha_salida=datetime.now(), estado='ocupada')
plaza3 = Plaza(id_plaza=3, pin=111113, fecha_deposito=datetime(2022, 12, 3, 10, 15, 00, 00000),
               fecha_salida=datetime.now(), estado='ocupada')
plaza4 = Plaza(id_plaza=4, pin=211111, fecha_deposito=None,
               fecha_salida=None, estado='abono ocupada')
plaza5 = Plaza(id_plaza=5, pin=211112, fecha_deposito=None, fecha_salida=None, estado='abono ocupada')
lista_plazas = [plaza1, plaza2, plaza3, plaza4, plaza5]

v1 = Vehiculo(matricula='1111A', tipo='Turismo')
v2 = Vehiculo(matricula='1111B', tipo='Turismo')
v3 = Vehiculo(matricula='1111C', tipo='Motocicleta')
v4 = Vehiculo(matricula='1111D', tipo='Motocicleta')
v5 = Vehiculo(matricula='1111F', tipo='Movilidad reducida')
lista_vehiculos = [v1, v2, v3, v4, v5]

abono1 = Abono(tipo='Mensual', factura=75, fecha_activacion=datetime(2022, 12, 1, 10, 15, 00, 00000),
               fecha_cancelacion=datetime(2023, 1, 1, 10, 15, 00, 00000))
abono2 = Abono(tipo='Anual', factura=200, fecha_activacion=datetime(2022, 1, 1, 10, 15, 00, 00000),
               fecha_cancelacion=datetime(2023, 1, 1, 10, 15, 00, 00000))
lista_abonos = [abono1, abono2]

c1 = Cliente(vehiculo=v1, plaza=plaza1)
c2 = Cliente(vehiculo=v2, plaza=plaza2)
c3 = Cliente(vehiculo=v3, plaza=plaza3)

ab1 = Abonado(nombre='Pedro', apellidos='Benito', num_tarjeta=1111, email='pedro@gmail.com', dni='dni1',
              abono=abono1, vehiculo=v4, plaza=plaza4)
ab2 = Abonado(nombre='Paco', apellidos='Pérez', num_tarjeta=2222, email='paco@gmail.com', dni='dni2',
              abono=Abono, vehiculo=v5, plaza=plaza5)
lista_clientes = [c1, c2, c3, abono1, abono2]

pk = Parking(num_plazas=list(range(1, 41)), clientes=[c1, c2, c3, ab1, ab2], registro_facturas={})

# ESCRIBIMOS LISTAS
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

facturas_cliente = open('files/facturas_cliente.pckl', 'wb')
pickle.dump(pk.registro_facturas, facturas_cliente)
facturas_cliente.close()

# LEEMOS LISTAS
clientes = open('files/clientes.pckl', 'rb')
clientes_list = pickle.load(clientes)
clientes.close()

vehiculos = open('files/vehiculos.pckl', 'rb')
vehiculos_list = pickle.load(vehiculos)
vehiculos.close()

plazas = open('files/plazas.pckl', 'rb')
plazas_list = pickle.load(plazas)
plazas.close()

abonos = open('files/abonos.pckl', 'rb')
abonos_list = pickle.load(abonos)
abonos.close()

facturas_cliente = open('files/facturas_cliente.pckl', 'rb')
facturas_cliente_list = pickle.load(facturas_cliente)
facturas_cliente.close()

menu = 1
while menu != 0:
    print("1. Cliente")
    print("2. Administrador")
    menu = int(input("Indica si eres cliente o administrador: "))
    if menu != 0:
        if menu == 1:
            pk.mostrar_clientes()
            imprimir_menu_cliente()
            menu1 = int(input("Indica desea hacer: "))
            if menu1 == 1:
                ##CREAR MATRICULA Y TIPO FUERA DEL MÉTODO PARA CREAR AQUI UN NUEVO CLIENTE
                matricula = input("Introduzca matrícula: ")
                tipo = input("Introduzca tipo de vehículo: ")
                new_vehiculo = Vehiculo(matricula=matricula, tipo=tipo)
                new_vehiculo.guardar_vehiculo(vehiculos)
                new_vehiculo.cargar_vehiculos()
                new_plaza = Plaza(id_plaza=pk.num_plazas[0], pin=111111,
                                  fecha_deposito=datetime(2022, 12, 1, 10, 15, 00, 00000),
                                  fecha_salida=None, estado='ocupada')
                new_plaza.guardar_plaza(plazas)
                new_plaza.cargar_plazas()
                new_cliente = Cliente(vehiculo=new_plaza, plaza=new_plaza)
                new_cliente.guardar_cliente(clientes)
                new_cliente.cargar_clientes()
                ParkingService.depositar_vehiculo(pk, lista_vehiculos, new_cliente)

            elif menu1 == 2:
                print("Su vehículo ha sido retirado correctamente, se le cobrará ",
                      ParkingService.retirar_vehiculo(pk), '€')
            elif menu1 == 3:
                ParkingService.depositar_abonados(pk)
            elif menu1 == 4:
                ParkingService.retirar_abonados(pk)
            else:
                print("Saliendo...")
        elif menu == 2:
            pk.mostrar_registro()
            imprimir_menu_admin()
            menu2 = int(input("Indica que desea hacer: "))
            if menu2 == 1:
                ParkingService.controlar_estado_parking(pk)
            elif menu2 == 2:
                ParkingService.mostrar_facturacion(pk)
            elif menu2 == 3:
                ParkingService.consular_abonados(pk)
            elif menu2 == 4:
                ParkingService.gestion_abonos(pk)
            elif menu2 == 5:
                ParkingService.caducidad_abonos(pk)
            else:
                print("Saliendo...")
