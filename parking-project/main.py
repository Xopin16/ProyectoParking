from service.cliente_service import *
from service.admin_service import *
from view.view import *
from model.abonado import Abonado
import pickle
from model.abono import Abono
from model.cliente import Cliente
from model.parking import Parking
from model.plaza import Plaza
from model.vehiculo import Vehiculo

ClienteService = ClienteService()
AdminService = AdminService()

plaza1 = Plaza(id_plaza=1, estado='ocupada', fecha_deposito=datetime(2023, 1, 1, 10, 15, 00, 00000))
plaza2 = Plaza(id_plaza=2, estado='ocupada', fecha_deposito=datetime(2023, 1, 2, 10, 15, 00, 00000))
plaza3 = Plaza(id_plaza=3, estado='ocupada', fecha_deposito=datetime(2023, 1, 3, 10, 15, 00, 00000))
plaza4 = Plaza(id_plaza=4, estado='abono ocupada')
plaza5 = Plaza(id_plaza=5, estado='abono ocupada')
lista_plazas = [plaza1, plaza2, plaza3, plaza4, plaza5]

v1 = Vehiculo(matricula='1111A', tipo='Turismo')
v2 = Vehiculo(matricula='1111B', tipo='Turismo')
v3 = Vehiculo(matricula='1111C', tipo='Motocicleta')
v4 = Vehiculo(matricula='1111D', tipo='Motocicleta')
v5 = Vehiculo(matricula='1111F', tipo='Movilidad reducida')
lista_vehiculos = [v1, v2, v3, v4, v5]

abono1 = Abono(tipo='Mensual', factura=25, fecha_activacion=datetime(2023, 1, 1, 10, 15, 00, 00000),
               fecha_cancelacion=datetime(2023, 2, 1, 10, 15, 00, 00000))
abono2 = Abono(tipo='Anual', factura=200, fecha_activacion=datetime(2023, 1, 1, 10, 15, 00, 00000),
               fecha_cancelacion=datetime(2024, 1, 1, 10, 15, 00, 00000))
lista_abonos = [abono1, abono2]

c1 = Cliente(vehiculo=v1, plaza=plaza1, pin=111111)
c2 = Cliente(vehiculo=v2, plaza=plaza2, pin=111112)
c3 = Cliente(vehiculo=v3, plaza=plaza3, pin=111113)

ab1 = Abonado(nombre='Pedro', apellidos='Benito', num_tarjeta=1111, email='pedro@gmail.com', dni='dni1',
              abono=abono1, vehiculo=v4, plaza=plaza4, pin=211111)
ab2 = Abonado(nombre='Paco', apellidos='Pérez', num_tarjeta=2222, email='paco@gmail.com', dni='dni2',
              abono=abono2, vehiculo=v5, plaza=plaza5, pin=211112)
lista_clientes = [c1, c2, c3, ab1, ab2]
lista_cobros_cliente = []
pk = Parking(plazas_totales=40, clientes=[c1, c2, c3, ab1, ab2], registro_facturas=[])
pk.rellenar_plazas(lista_plazas)

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

tickets_cliente = open('files/facturas_cliente.pckl', 'wb')
pickle.dump(pk.registro_facturas, tickets_cliente)
tickets_cliente.close()

cobros_cliente = open('files/facturas_cliente.pckl', 'wb')
pickle.dump(lista_cobros_cliente, cobros_cliente)
cobros_cliente.close()

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

tickets_cliente = open('files/facturas_cliente.pckl', 'rb')
ticekts_cliente_list = pickle.load(tickets_cliente)
tickets_cliente.close()

cobros_cliente = open('files/facturas_cliente.pckl', 'rb')
cobros_cliente_list = pickle.load(cobros_cliente)
cobros_cliente.close()

menu = 1
menu1 = 1
menu2 = 1
while menu != 0:
    print("1. Cliente")
    print("2. Administrador")
    menu = int(input("Indica si eres cliente o administrador: "))
    if menu != 0:
        if menu == 1:
            while menu1 != 0:
                pk.mostrar_clientes(lista_clientes)
                imprimir_menu_cliente()
                menu1 = int(input("Indica desea hacer: "))
                if menu1 == 1:
                    pk.mostrar_plazas_tipo(lista_clientes)
                    matricula = input("Introduzca matrícula: ")
                    tipo = input("Introduzca tipo de vehículo: ")
                    new_vehiculo = Vehiculo(matricula=matricula, tipo=tipo)
                    lista_vehiculos.append(new_vehiculo)
                    new_cliente = Cliente(vehiculo=new_vehiculo, plaza=None, pin=random.randint(100000, 999999))
                    lista_clientes.append(new_cliente)
                    ClienteService.depositar_vehiculo(pk, new_cliente, lista_plazas)
                elif menu1 == 2:
                    ClienteService.retirar_vehiculo(lista_clientes, lista_cobros_cliente)
                elif menu1 == 3:
                    ClienteService.depositar_abonados(lista_clientes)
                elif menu1 == 4:
                    ClienteService.retirar_abonados(lista_clientes)
                else:
                    print("Saliendo...")
        elif menu == 2:
            while menu2 != 0:
                imprimir_menu_admin()
                menu2 = int(input("Indica que desea hacer: "))
                if menu2 == 1:
                    AdminService.controlar_estado_parking(pk, lista_plazas)
                elif menu2 == 2:
                    AdminService.mostrar_facturacion(lista_cobros_cliente)
                elif menu2 == 3:
                    AdminService.consular_abonados(lista_clientes)
                elif menu2 == 4:
                    AdminService.gestion_abonos(lista_clientes, lista_plazas, lista_abonos)
                elif menu2 == 5:
                    AdminService.caducidad_abonos(lista_clientes)
                else:
                    print("Saliendo...")
        else:
            print("Saliendo...")
