"""
1. Escriba un programa que lea números del teclado, si el numero leído es par
entonces va acumulando la suma de todos los pares introducidos. Termina si lee
del teclado un –1 e imprime el total sumado
"""

suma_pares = 0

while True:
    numero = int(input("Digite un número (-1 para terminar): "))

    if numero == -1:
        break

    if numero % 2 == 0:
        suma_pares += numero

print("La suma total de los pares es:", suma_pares)

"""
2. Escriba un programa que lee números del teclado. Guarda en una lista los pares
positivos y en otra los impares positivos. Termina si meten cualquier numero
negativo. Al terminar imprime cuantos numeros pares e impares positivos se
introdujeron
"""

pares = []
impares = []

while True:
    numero2 = int(input("Digite un número (negativo para terminar): "))

    if numero2 < 0:
        break

    if numero2 > 0:
        if numero2 % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
            
print("La cantidad de números pares positivos introducidos es de:", len(pares))
print("La cantidad de números impares positivos introducidos es de:", len(impares))

"""
3. Haga un programa que lee un numero, y luego tantas palabras como ese numero.
Luego mete todas las palabras en un set, e imprime el set.
"""


n = int(input("¿Cuántas palabras desea ingresar?: "))

palabras = set()

for i in range(n):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.add(palabra) 

print("El conjunto de palabras es:", palabras)

"""
4. Haga un programa que lee un numero, y luego tantas palabras como ese numero.
Luego mete todas las palabras en una tupla y pregunta por un numero e imprime la
palabra en esa posicion de la tupla.
"""

m = int(input("¿Cuántas palabras desea ingresar?: "))

palabras2 = [] 

for i in range(m):
    palabra2 = input(f"Ingrese la palabra {i+1}: ")
    palabras2.append(palabra2)

# Tupla a lista
tupla_palabras = tuple(palabras2)

print("La tupla de palabras es:", tupla_palabras)

posición = int(input("Ingrese un número de posición: "))

if 1 <= posición <= len(tupla_palabras):
    print("La palabra en esa posición es:", tupla_palabras[posición - 1])
else:
    print("Posición inválida")

"""
5. Haga un programa que lea 5 numeros, los mete en una lista y luego escoge el mas
grande y el mas pequeño y los imprime.
"""

numeros5 = []

for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros5.append(num)

print("Lista:", numeros5)

mayor = max(numeros5)
menor = min(numeros5)

print("El número mayor es:", mayor)
print("El número menor es:", menor)

"""
6. Haga un programa que pida un numero y lea tantas palabras como la cantidad del
numero. Al final el programa imprime la mas larga. 
"""

k = int(input("¿Cuántas palabras desea ingresar?: "))

palabras6 = []

for i in range(k):
    palabra6 = input(f"Ingrese la palabra {i+1}: ")
    palabras6.append(palabra6)

mas_larga = max(palabras6, key=len)

print("La palabra más larga es:", mas_larga)