def main():
    opcion = 0    
    while opcion != 4:
        print("Escoja su opcion: ")
        print("1. opcion 1")
        print("2. opcion 2")
        print("3. opcion 3")
        print("4. salir")
        try:
            opcion = int(input()) #dentro del try
            # va el codigo que puede generar error
        except: #aqui va el codigo para manejar el error
            print("Opcion invalida, intente de nuevo.\n")

main()
