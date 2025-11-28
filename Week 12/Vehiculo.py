from abc import ABC, abstractmethod

class Vehiculo(ABC):

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, new_value):
        self.__marca = new_value

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, new_value):
        self.__modelo = new_value

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass