def main():
    opcion = 0    
    while opcion != 4:
        print("Escoja su opcion: ")
        print("1. opcion 1")
        print("2. opcion 2")
        print("3. opcion 3")
        print("4. salir")
        try:
            opcion = int(input()) 
            with open("archivo.txt") as file:
                print(file.readline())
        except ValueError as err:
            print("Opcion invalida, intente de nuevo.\n")
            print(err)
        except FileNotFoundError as err_file: 
            print("El archivo no existe\n")
            print(err_file)
        except: 
            print("error inesperado")
            print(generic_error)                

main()