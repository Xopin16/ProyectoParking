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

pk = Parking(plazas_totales=40, registro_facturas=[])
lista_clientes = cargar_clientes()
lista_vehiculos = cargar_vehiculos()
lista_plazas = cargar_plazas()
lista_abonos = cargar_abonos()
lista_cobros_cliente = cargar_facturas()
pk.rellenar_plazas(lista_plazas)
pk.plazas_disponibles = pk.rellenar_plazas_tipo(lista_clientes)


menu_principal = -1
menu_cliente = -1
menu_admin = -1
menu3 = -1
menu_abono = -1
opcion_abono = -1
opcion_modificar = -1
opcion_datos = -1
opcion_tipo = -1


while menu_principal != 0:
    print("1. Cliente")
    print("2. Administrador")
    print("0. Guardar y salir.")
    try:
        menu_principal = int(input("Indica si eres cliente o administrador: "))
        print("\n")
    except ValueError:
        print("Por favor, indica un número válido.")
    if menu_principal == 1:
        menu_cliente = -1
        while menu_cliente != 0:
            pk.mostrar_plazas_tipo()
            print("\n")
            imprimir_tarifas()
            print("\n")
            imprimir_menu_cliente()
            try:
                menu_cliente = int(input("Indica desea hacer: "))
                print("\n")
            except ValueError:
                menu_cliente = -1
                print("Por favor, indica un número válido.")
            if menu_cliente == 1:
                matricula = input("Introduzca matrícula: ")
                comprobar_matricula(matricula, lista_clientes)
                tipo = asignar_tipo()
                if not comprobar_matricula(matricula, lista_clientes):
                    if tipo != 'No encontrado':
                        if pk.plazas_disponibles[tipo] > 0:
                            new_vehiculo = Vehiculo(matricula=matricula, tipo=tipo)
                            lista_vehiculos.append(new_vehiculo)
                            new_cliente = Cliente(vehiculo=new_vehiculo, pin=random.randint(100000, 999999))
                            ClienteService.depositar_vehiculo(pk, new_cliente, lista_plazas)
                            lista_clientes.append(new_cliente)
                        else:
                            print("No tenemos más plazas disponibles para su vehículo.")
                    else:
                        print("Introduzca un vehículo valido.")
                else:
                    print("Lo sentimos, ya se ha registrado esa matricula.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu_cliente == 2:
                cliente = comprobar_cliente(lista_clientes)
                if ClienteService.retirar_vehiculo(pk, lista_clientes, lista_cobros_cliente, cliente, lista_plazas):
                    print("Se ha retirado su vehículo correctamente.")
                else:
                    print("Lo sentimos, no existe ese cliente.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu_cliente == 3:
                abonado = comprobar_abonados_deposito()
                if ClienteService.depositar_abonados(lista_clientes, abonado, lista_plazas):
                    print("Se ha depositado su vehículo correctamente.")
                else:
                    print("No se ha podido depositar el vehiculo,  compruebe si su abono ha caducado o si ya "
                          "ha depositado su vehiculo.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu_cliente == 4:
                abonado = comprobar_abonados_retiro()
                if ClienteService.retirar_abonados(lista_clientes, abonado, lista_plazas):
                    print("Se he realizado el retiro correctamente.")
                else:
                    print("No se ha podido retirar el vehiculo,  compruebe si su abono ha caducado o si ya "
                          "ha retirado su vehiculo.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            else:
                print("Saliendo...")
    elif menu_principal == 2:
        menu_admin = -1
        while menu_admin != 0:
            imprimir_menu_admin()
            try:
                menu_admin = int(input("Indica que desea hacer: "))
                print("\n")
            except ValueError:
                menu_admin = -1
                print("Por favor, indica un número válido.")
            if menu_admin == 1:
                AdminService.controlar_estado_parking(pk, lista_plazas)
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu_admin == 2:
                print("Indique la primera fecha:")
                fecha1 = generar_fecha()
                print("Indique la segunda fecha:")
                fecha2 = generar_fecha()
                if fecha1 is not None and fecha2 is not None:
                    if AdminService.comprobar_facturacion(lista_cobros_cliente, fecha1, fecha2):
                        imprimir_lista_facturas(lista_cobros_cliente, fecha1, fecha2)
                    else:
                        print("No se han registrado facturas entre esas fechas.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu_admin == 3:
                if AdminService.consultar_abonados(lista_clientes):
                    mostrar_abonados(lista_clientes)
                else:
                    print("En este momento no tenemos ningún abonado.")
                guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                              lista_cobros_cliente)
            elif menu_admin == 4:
                menu_abono = -1
                while menu_abono != 0:
                    menu_abono = imprimir_menu_abono()
                    if menu_abono == 1:
                        abonado = crear_abonado_alta(lista_clientes)
                        if abonado is not None:
                            if abonado.vehiculo.tipo != 'No encontrado':
                                if pk.plazas_disponibles[abonado.vehiculo.tipo] > 0:
                                    opcion_abono = imprimir_tipos_abono()
                                    if AdminService.alta_abonado(pk, abonado, lista_clientes, lista_abonos,
                                                                 lista_plazas,
                                                                 opcion_abono):
                                        pk.plazas_disponibles[abonado.vehiculo.tipo] -= 1
                                        print("Se ha registrado el abonado.")
                                    else:
                                        print("Introduzca un tipo de abono correcto.")
                                else:
                                    print("No tenemos más plazas disponibles para su vehículo.")
                            else:
                                print("Tipo de vehículo incorrecto, seleccione una opción válida.")
                        else:
                            print("Datos incorrectos, ya hemos registrado un abono con un dni o matricula idénticos.")
                        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                      lista_cobros_cliente)
                    elif menu_abono == 2:
                        abonado = comprobar_abonado_modificado()
                        opcion_modificar = -1
                        while opcion_modificar != 0:
                            opcion_modificar = imprimir_opcion_modificar()
                            if opcion_modificar == 1:
                                opcion_tipo = imprimir_tipos_abono()
                                if AdminService.modificar_tipo_abono(abonado, opcion_tipo, lista_clientes):
                                    print("Se ha modificado correctamente.")
                                else:
                                    print("Lo sentimos, no se ha podido modificar el abono, "
                                          "compruebe que los datos son correctos.")
                            elif opcion_modificar == 2:
                                opcion_datos = imprimir_datos_modificar()
                                if AdminService.modificar_datos_abonado(abonado, opcion_datos, lista_clientes):
                                    print("Se ha moficado correctamente.")
                                else:
                                    print("Lo sentimos, no se ha podido modificar el abono, "
                                          "compruebe que los datos son correctos.")
                            else:
                                print("Saliendo...")
                        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                      lista_cobros_cliente)
                    elif menu_abono == 3:
                        abonado = comprobar_abonado_modificado()
                        if AdminService.baja_abonado(pk, abonado, lista_clientes, lista_plazas):
                            print("Se ha borrado con éxito.")
                        else:
                            print("Lo sentimos, el abonado no existe, compruebe si su abono ha caducado.")
                        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                      lista_cobros_cliente)
                    else:
                        print("Saliendo...")
            elif menu_admin == 5:
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
                        if AdminService.comprobar_abonos_proximos(lista_clientes):
                            mostrar_abonos_proximos(lista_clientes)
                        else:
                            print("No caducan abonos en los proximos 10 días.")
                        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk,
                                      lista_cobros_cliente)
                    else:
                        print("Saliendo...")
            elif menu_admin == 6:
                AdminService.mostrar_clientes_abonados(lista_clientes)
            else:
                print("Saliendo...")
    else:
        guardar_datos(lista_clientes, lista_vehiculos, lista_plazas, lista_abonos, pk, lista_cobros_cliente)
        print("Saliendo...")
