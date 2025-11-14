import io_utils
import product_manager

def process(option):
    if option == 1:
        data = read_product_data()
        product_manager.store(data)

    elif option == 2:
        print_products(product_manager.get_all())

    elif option == 3:
        sub = io_utils.read_str("Buscar por (a) nombre o (b) rango de precio? ")

        if sub.lower() == "a":
            name = io_utils.read_str("Nombre o fragmento: ")
            print_products(product_manager.find_by_name(name))

        elif sub.lower() == "b":
            minimo = io_utils.read_int("Precio mínimo: ")
            maximo = io_utils.read_int("Precio máximo: ")
            print_products(product_manager.find_by_price(minimo, maximo))

    elif option == 4:
        id_prod = io_utils.read_int("ID del producto a modificar: ")
        nuevo_precio = float(io_utils.read_str("Nuevo precio: "))
        nuevo_proveedor = io_utils.read_str("Nuevo proveedor: ")
        product_manager.update_product(id_prod, nuevo_precio, nuevo_proveedor)

    elif option == 5:
        id_prod = io_utils.read_int("ID del producto a borrar: ")
        product_manager.delete_product(id_prod)

    elif option == 6:
        print("Saliendo...")

    else:
        print("opción inválida.")

def read_product_data():
    data = []
    print("\n--- Ingreso de producto ---")
    data.append(io_utils.read_str("Nombre: "))
    data.append(io_utils.read_str("Categoría: "))
    data.append(float(io_utils.read_str("Precio: ")))
    data.append(io_utils.read_str("Proveedor: "))
    return data

def print_products(lista):
    for p in lista:
        print(p)
