def mostrar_menu(opciones):
    print("\n=== MENÚ ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")


def leer_string(prompt):
    try:
        valor = input(prompt)
        if valor == "":
            raise ValueError("No puede estar vacío")
    except:
        print("Error inesperado al leer string")
        return None
    else:
        return valor
    finally:
        print("Fin de leer_string")


def leer_entero(prompt):
    try:
        valor = int(input(prompt))
    except:
        print("Error: debe ingresar un número entero.")
        return None
    else:
        return valor
    finally:
        print("Fin de leer_entero")


def leer_flotante(prompt):
    try:
        valor = float(input(prompt))
    except:
        print("Error: debe ingresar un número flotante.")
        return None
    else:
        return valor
    finally:
        print("Fin de leer_flotante")


def leer_imaginario(prompt):
    try:
        valor = complex(input(prompt))
    except:
        print("Error: número complejo inválido.")
        return None
    else:
        return valor
    finally:
        print("Fin de leer_imaginario")
