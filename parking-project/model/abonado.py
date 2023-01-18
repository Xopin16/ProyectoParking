from model.cliente import Cliente


class Abonado(Cliente):

    def __init__(self, nombre, apellidos, num_tarjeta, email, dni, abono, vehiculo, plaza):
        super().__init__(vehiculo, plaza)
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__num_tarjeta = num_tarjeta
        self.__email = email
        self.__dni = dni
        self.__abono = abono

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.nombre, self.apellidos, self.num_tarjeta, self.email, self.dni,
                                             self.abono, self.vehiculo, self.plaza.__str__())

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self.__apellidos = valor

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, valor):
        self.__num_tarjeta = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        self.__dni = valor

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, valor):
        self.__abono = valor

