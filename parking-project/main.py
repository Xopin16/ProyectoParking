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

pk = Parking(plazas_totales=40,  registro_facturas=[])
lista_clientes = cargar_clientes()
lista_vehiculos = cargar_vehiculos()
lista_plazas = cargar_plazas()
lista_abonos = cargar_abonos()
lista_cobros_cliente = cargar_facturas()
pk.rellenar_plazas(lista_plazas)
# lista_plazas = []
# lista_vehiculos = []
# lista_abonos = []
# lista_clientes = []
# lista_cobros_cliente = []
# cargar_datos(lista_plazas, lista_vehiculos, lista_abonos, lista_clientes, lista_cobros_cliente, pk)
# guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk, lista_cobros_cliente)

menu = -1
menu1 = -1
menu2 = -1
menu3 = -1
menu4 = -1
opcion_abono = -1
opcion_modificar = -1
opcion_datos = -1
opcion_tipo = -1

while menu != 0:
    print("1. Cliente")
    print("2. Administrador")
    try:
        menu = int(input("Indica si eres cliente o administrador: "))
    except ValueError:
        print("Por favor, indica un número válido.")
    if menu == 1:
        menu1 = -1
        while menu1 != 0:
            pk.mostrar_clientes(lista_clientes)
            imprimir_menu_cliente()
            try:
                menu1 = int(input("Indica desea hacer: "))
            except ValueError:
                menu1 = -1
                print("Por favor, indica un número válido.")
            if menu1 == 1:
                pk.mostrar_plazas_tipo(lista_clientes)
                matricula = input("Introduzca matrícula: ")
                tipo = input("Introduzca tipo de vehículo: ")
                new_vehiculo = Vehiculo(matricula=matricula, tipo=tipo)
                lista_vehiculos.append(new_vehiculo)
                new_cliente = Cliente(vehiculo=new_vehiculo, plaza=None, pin=random.randint(100000, 999999))
                ClienteService.depositar_vehiculo(pk, new_cliente, lista_plazas)
                lista_clientes.append(new_cliente)
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu1 == 2:
                cliente = comprobar_cliente()
                if ClienteService.retirar_vehiculo(lista_clientes, lista_cobros_cliente, cliente, lista_plazas):
                    print("Se ha retirado su vehículo correctamente.")
                else:
                    print("Lo sentimos, no existe ese cliente.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu1 == 3:
                abonado = comprobar_abonados_deposito()
                if ClienteService.depositar_abonados(lista_clientes, abonado):
                    print("Se ha depositado su vehículo correctamente.")
                else:
                    print("Lo sentimos, el abonado no existe, compruebe si su abono ha caducado.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu1 == 4:
                abonado = comprobar_abonados_retiro()
                if ClienteService.retirar_abonados(lista_clientes, abonado):
                    print("Se he realizado el retiro correctamente.")
                else:
                    print("Lo sentimos, el abonado no existe, compruebe si su abono ha caducado.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            else:
                print("Saliendo...")
    elif menu == 2:
        menu2 = -1
        while menu2 != 0:
            imprimir_menu_admin()
            try:
                menu2 = int(input("Indica que desea hacer: "))
            except ValueError:
                menu2 = -1
                print("Por favor, indica un número válido.")
            if menu2 == 1:
                AdminService.controlar_estado_parking(pk, lista_plazas)
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu2 == 2:
                print("Indique la primera fecha:")
                fecha1 = generar_fecha()
                print("Indique la segunda fecha:")
                fecha2 = generar_fecha()
                if AdminService.comprobar_facturacion(lista_cobros_cliente, fecha1, fecha2):
                    imprimir_lista_facturas(lista_cobros_cliente, fecha1, fecha2)
                else:
                    print("No se han registrado facturas entre esas fechas.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu2 == 3:
                if AdminService.consultar_abonados(lista_clientes):
                    mostrar_abonados(lista_clientes)
                else:
                    print("En este momento no tenemos ningún abonado.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu2 == 4:
                menu4 = -1
                while menu4 != 0:
                    menu4 = imprimir_menu_abono()
                    if menu4 == 1:
                        abonado = crear_abonado_alta()
                        opcion_abono = imprimir_tipos_abono()
                        AdminService.alta_abonado(abonado, lista_clientes, lista_abonos, lista_plazas, opcion_abono)
                        print("Se ha registrado el abonado.")
                        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                      lista_cobros_cliente)
                    elif menu4 == 2:
                        abonado = comprobar_abonado_modificado()
                        opcion_modificar = -1
                        while opcion_modificar != 0:
                            opcion_modificar = imprimir_opcion_modificar()
                            if opcion_modificar == 1:
                                opcion_tipo = imprimir_tipos_abono()
                                if AdminService.modificar_tipo_abono(abonado, opcion_tipo, lista_clientes):
                                    print("Se ha modificado correctamente.")
                                else:
                                    print("Lo sentimos, el abonado no existe.")
                            elif opcion_modificar == 2:
                                opcion_datos = imprimir_datos_modificar()
                                if AdminService.modificar_datos_abonado(abonado, opcion_datos, lista_clientes):
                                    print("Se ha moficado correctamente.")
                                else:
                                    print("Lo sentimos, el abonado no existe, compruebe si su abono ha caducado.")
                                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                              lista_cobros_cliente)
                            else:
                                print("Saliendo...")
                    elif menu4 == 3:
                        abonado = comprobar_abonado_modificado()
                        if AdminService.baja_abonado(abonado, lista_clientes):
                            print("Se ha borrado con éxito.")
                        else:
                            print("Lo sentimos, el abonado no existe, compruebe si su abono ha caducado.")
                        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                      lista_cobros_cliente)
                    else:
                        print("Saliendo...")
            elif menu2 == 5:
                menu3 = -1
                while menu3 != 0:
                    menu3 = imprimir_menu_caducidad()
                    if menu3 == 1:
                        try:
                            mes = int(input("Indica el mes que desea consultar: "))
                            AdminService.comprobar_abonos_mes(lista_clientes, mes)
                            mostrar_abonados_mes(lista_clientes, mes)
                            guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                          lista_cobros_cliente)
                        except ValueError:
                            print("Por favor, indica un mes válido.")
                    elif menu3 == 2:
                        AdminService.comprobar_abonos_proximos(lista_clientes)
                        mostrar_abonos_proximos(lista_clientes)
                        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                      lista_cobros_cliente)
                    else:
                        print("Saliendo...")
            else:
                print("Saliendo...")
    else:
        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk, lista_cobros_cliente)
        print("Saliendo...")
