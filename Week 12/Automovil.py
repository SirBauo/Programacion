from Vehiculo import Vehiculo

class Automovil(Vehiculo):

    def arrancar(self):
        return f"{self.marca}, {self.modelo} enciende el motor"

    def detener(self):
        return f"{self.marca}, {self.modelo} detiene el motor"