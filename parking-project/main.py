from datetime import datetime

from Abonado import Abonado
from Abono import Abono
from Cliente import Cliente
from Parking import Parking
from Plaza import Plaza
from Vehiculo import Vehiculo

coche1 = Vehiculo(matricula='1111A', tipo='Turismo')
coche2 = Vehiculo(matricula='1111B', tipo='Turismo')
moto1 = Vehiculo(matricula='1111C', tipo='Motocicleta')
moto2 = Vehiculo(matricula='1111D', tipo='Motocicleta')
mr1 = Vehiculo(matricula='1111E', tipo='Movilidad reducida')
mr2 = Vehiculo(matricula='1111F', tipo='Movilidad reducida')
c1 = Cliente(vehiculo=coche1,
             plaza=Plaza(id_plaza=1, pin=111111, fecha_deposito=datetime(2022, 12, 1, 10, 15, 00, 00000),
                         fecha_salida=datetime.now(), estado='ocupada'))
c2 = Cliente(vehiculo=coche2,
             plaza=Plaza(id_plaza=2, pin=111112, fecha_deposito=datetime(2022, 12, 2, 10, 15, 00, 00000),
                         fecha_salida=datetime.now(), estado='ocupada'))
c3 = Cliente(vehiculo=moto1,
             plaza=Plaza(id_plaza=3, pin=111113, fecha_deposito=datetime(2022, 12, 3, 10, 15, 00, 00000),
                         fecha_salida=datetime.now(), estado='ocupada'))
ab1 = Abonado(nombre='Pedro', apellidos='Benito', num_tarjeta=1111, email='pedro@gmail.com', dni='dni1',
              abono=Abono(tipo= 'Mensual', factura=75, fecha_activacion=datetime(2022, 12, 1, 10, 15, 00, 00000),
                          fecha_cancelacion=None), vehiculo=moto2,
              plaza=Plaza(id_plaza=4, pin=211111, fecha_deposito=datetime(2023, 12, 1, 10, 15, 00, 00000),
                          fecha_salida=datetime.now(), estado='abono ocupada'))
ab2 = Abonado(nombre='Paco', apellidos='Pérez', num_tarjeta=2222, email='paco@gmail.com', dni='dni2',
              abono=Abono(tipo= 'Anual', factura=200, fecha_activacion=datetime(2023, 1, 1, 10, 15, 00, 00000),
                          fecha_cancelacion=None),
              vehiculo=mr1, plaza=Plaza(id_plaza=5, pin=211112, fecha_deposito=datetime(2023, 1, 1, 10, 15, 00, 00000),
                                        fecha_salida=datetime.now(), estado='abono ocupada'))
pk = Parking(num_plazas=list(range(1, 41)), clientes=[c1, c2, c3, ab1, ab2], registro_facturas={})

menu = 1
while menu != 0:
    print("1. Cliente")
    print("2. Administrador")
    menu = int(input("Indica si eres administrador o cliente: "))
    if menu != 0:
        if menu == 1:
            pk.mostrar_clientes()
            print("1. Depositar vehiculo")
            print("2. Retirar vehiculo")
            print("3. Depositar abonados")
            print("4. Retirar abonados")
            print("0. Para salir")
            menu1 = int(input("Indica desea hacer: "))
            if menu1 == 1:
                pk.depositar_vehiculo()
            elif menu1 == 2:
                # if pk.retirar_vehiculo() is not None:
                print("Su vehículo ha sido retirado correctamente, se le cobrará ", pk.retirar_vehiculo(), '€')
                # else:
                #     print("No hay ningún cliente con esos datos.")
            elif menu1 == 3:
                pk.depositar_abonados()
            elif menu1 == 4:
                pk.retirar_abonados()
            else:
                print("Saliendo...")
        elif menu == 2:
            pk.mostrar_registro()
            print("1. Consultar estado parking")
            print("2. Mostrar registro de facturas")
            print("3. Consultar abonos")
            print("4. Gestionar abonos")
            print("5. Consultar caducidad de abonos")
            print("0. Para salir")
            menu2 = int(input("Indica que desea hacer: "))
            if menu2 == 1:
                pk.controlar_estado_parking()
            elif menu2 == 2:
                pk.mostrar_facturacion()
            elif menu2 == 3:
                pk.consular_abonados()
            elif menu2 == 4:
                pk.gestion_abonos()
            elif menu2 == 5:
                pk.caducidad_abonos()
            else:
                print("Saliendo...")
