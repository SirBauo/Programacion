
mi_variable = 2
print(mi_variable) #imprime 2
mi_variable = "Hola"
print(mi_variable) #imprime "Hola"

print("ahora hace esto primero")
print("hola mundo") 

x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 2
print(x)
print(y)
#la siguiente linea al intentar ejecutarse tira error. 
#print("La X vale " + x + ", y la y vale " + y) 
#aqui esta la linea corregida
print("La X vale " + str(x) + ", y la y vale " + str(y)) 
#la funcion str convierte lo que recibe en su representacion de hilera de caracteres


#funciones de transformacion
a = 3
b = 1.0
c = 10
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#aqui usamos las variables anteriores para la transformacion
x = str(a)
y = int(b)
z = float(c)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))