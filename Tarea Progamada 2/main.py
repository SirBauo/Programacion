# main.py
# Programa principal: el usuario elige algoritmo y acción

import cesar
import vignere

def menu():
    print("ENCRIPTADOR")
    texto = input("Ingrese el texto: ").strip()
    print("\nElija el tipo de cifrado:")
    print("1. Cifra de César")
    print("2. Cifra de Vigenère")

    opcion = input("Opción: ").strip()
    if opcion == "1":
        manejar_cesar(texto)
    elif opcion == "2":
        manejar_vignere(texto)
    else:
        print("Opción invalida.")


def manejar_cesar(texto):
    desplazamiento = int(input("Ingrese el desplazamiento (número entero): "))
    accion = input("¿Desea (E)ncriptar o (D)esencriptar?: ").strip().lower()
    if accion == "e":
        resultado = cesar.cifrar_cesar(texto, desplazamiento)
        print("\nTexto encriptado:", resultado)
    elif accion == "d":
        resultado = cesar.descifrar_cesar(texto, desplazamiento)
        print("\nTexto desencriptado:", resultado)
    else:
        print("Opción invalida.")


def manejar_vignere(texto):
    clave = input("Ingrese la clave: ").strip().lower()
    accion = input("¿Desea (E)ncriptar o (D)esencriptar?: ").strip().lower()
    if accion == "e":
        resultado = vignere.cifrar_vignere(texto, clave)
        print("\nTexto encriptado:", resultado)
    elif accion == "d":
        resultado = vignere.descifrar_vignere(texto, clave)
        print("\nTexto desencriptado:", resultado)
    else:
        print("Opción invalida.")


if __name__ == "__main__":
    menu()
