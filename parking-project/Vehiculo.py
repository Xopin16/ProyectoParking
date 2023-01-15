class Vehiculo:

    def __init__(self, matricula, tipo):
        self.matricula = matricula
        self.tipo = tipo

    def __str__(self):
        return '{} {}'.format(self.matricula, self.tipo)
