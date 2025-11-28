from Animal import Animal
from Perro import Perro
from Automovil import Automovil

#un_animal = Animal()
#print(un_animal)

un_perro = Perro("capitan", "chihuahua", 8)
print(un_perro)
print(un_perro.hacer_sonido())

un_auto = Automovil("Toyota", "Tercel")
print(un_auto.arrancar())
print(un_auto.detener())
print(un_auto.marca)
print(un_auto.modelo)