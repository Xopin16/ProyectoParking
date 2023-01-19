from service.cliente_service import *
from service.admin_service import *
from view.view import *
from model.abonado import Abonado
import pickle
from files.datos import *
from model.abono import Abono
from model.cliente import Cliente
from model.parking import Parking
from model.plaza import Plaza
from model.vehiculo import Vehiculo

ClienteService = ClienteService()
AdminService = AdminService()

pk = Parking(plazas_totales=40, clientes=None,  registro_facturas=[])
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
pk.rellenar_plazas(lista_plazas)

menu = -1
menu1 = -1
menu2 = -1
while menu != 0:
    print("1. Cliente")
    print("2. Administrador")
    menu = int(input("Indica si eres cliente o administrador: "))
    if menu == 1:
        menu1 = -1
        try:
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
        except ValueError:
            print("")
    elif menu == 2:
        menu2 = -1
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
        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk, lista_cobros_cliente)
        print("Saliendo...")
