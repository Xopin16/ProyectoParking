from Abonado import Abonado
from Cliente import Cliente
from Parking import Parking
from Plaza import Plaza
from Vehiculo import Vehiculo
import math

coche1 = Vehiculo(matricula=None, tipo='Turismo')
coche2 = Vehiculo(matricula='1111B', tipo='Turismo')
moto1 = Vehiculo(matricula='1111C', tipo='Motocicleta')
moto2 = Vehiculo(matricula='1111D', tipo='Motocicleta')
mr1 = Vehiculo(matricula='1111E', tipo='Movilidad reducida')
mr2 = Vehiculo(matricula='1111F', tipo='Movilidad reducida')
c1 = Cliente(vehiculo=coche1, plaza=None)
c2 = Cliente(vehiculo=coche2, plaza=None)
c3 = Cliente(vehiculo=moto1, plaza=None)
ab1 = Abonado(nombre='Pedro', apellidos='Benito', num_tarjeta=1111, email='pedro@gmail.com', dni='dni1', abono=None,
              vehiculo=coche2, plaza=None)
ab2 = Abonado(nombre='Paco', apellidos='Pérez', num_tarjeta=2222, email='paco@gmail.com', dni='dni2', abono=None,
              vehiculo=moto1, plaza=None)
pk = Parking(abonados=[ab1, ab2], num_plazas=list(range(1, 100)), clientes=[c1, c2, c3],
             plazas={Plaza.estado: list(range(1, 100))}, registro_facturas=[])

menu = 1
while menu != 0:
    print("1. Cliente")
    print("2. Administrador")
    menu = int(input("Indica si eres administrador o cliente: "))
    if menu != 0:
        if menu == 1:
            print("1. Depositar vehiculo")
            print("2. Retirar vehiculo")
            print("3. Depositar abonados")
            print("4. Retirar abonados")
            print("0. Para salir")
            menu1 = int(input("Indica desea hacer: "))
            if menu1 == 1:
                pk.depositar_vehiculo(c1)
            elif menu1 == 2:
                pk.retirar_vehiculo()
            elif menu1 == 3:
                pk.depositar_abonados()
            elif menu1 == 4:
                pk.retirar_abonados()
            else:
                print("Saliendo...")
        elif menu == 2:
            print("1. Consultar estado parking")
            print("2. Consultar abonos")
            print("3. Gestionar abonos")
            print("4. Consultar caducidad de abonos")
            print("0. Para salir")
            menu2 = int(input("Indica que desea hacer: "))
            if menu2 == 1:
                pk.controlar_estado_parking()
            elif menu2 == 2:
                pass
            elif menu2 == 3:
                pk.gestion_abonos()
            elif menu2 == 4:
                pk.caducidad_abonos()
            else:
                print("Saliendo...")


