import module_io as io
import module_file as mf

def main():
    opcion = 0
    while opcion != 4:

        print("\nEscoja su opción:")
        print("1. Probar lectura de entero")
        print("2. Probar lectura de archivo")
        print("3. Probar lectura de flotante")
        print("4. Salir")

        try:
            opcion = int(input("Ingrese opción: "))

            if opcion == 1:
                res = io.leer_entero("Ingrese un entero: ")
                print("Resultado:", res)

            elif opcion == 2:
                texto = mf.leer_texto_completo("archivo_inexistente.txt")
                print("Contenido:", texto)

            elif opcion == 3:
                res = io.leer_flotante("Ingrese un flotante: ")
                print("Resultado:", res)

        except:
            print("Error inesperado en el menú.")

    print("Programa finalizado.")

main()