from Animal import Animal

class Perro(Animal):

    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
    
    def __str__(self):
        return f"{self.__nombre}, edad: {self.__edad} de la raza {self.__raza}"

    def hacer_sonido(self):
        return "Guau"