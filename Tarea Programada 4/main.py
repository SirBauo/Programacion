from Rey import Rey
from Reina import Reina
from Torre import Torre
from Arfil import Arfil
from Caballo import Caballo
from Peon import Peon


def crear_pieza(nombre, col, row):
    nombre = nombre.lower()
    mapping = {
        "rey": Rey,
        "reina": Reina,
        "dama": Reina,
        "torre": Torre,
        "arfil": Arfil,
        "caballo": Caballo,
        "peon": Peon,
        "peón": Peon
    }
    if nombre not in mapping:
        return None
    return mapping[nombre](col, row)


def main():
    while True:
        print("\n=== MENÚ ===")
        print("1. Ver movimientos posibles")
        print("2. Consultar si una casilla es válida")
        print("3. Salir")

        op = input("Opción: ")

        if op == "3":
            print("Adiós!")
            break

        pieza = input("Ingrese pieza: ")
        col = input("Columna (a-h): ").lower()
        row = int(input("Fila (1-8): "))

        obj = crear_pieza(pieza, col, row)
        if obj is None:
            print("Pieza no reconocida.")
            continue

        moves = obj.possible_moves()

        if op == "1":
            print(f"Movimientos de {obj}:")
            for c, r in moves:
                print(f"- {c}{r}")

        elif op == "2":
            c2 = input("Columna destino: ").lower()
            r2 = int(input("Fila destino: "))

            if (c2, r2) in moves:
                print("El movimiento es posible")
            else:
                print("El movimiento no es posible")

if __name__ == "__main__":
    main()
