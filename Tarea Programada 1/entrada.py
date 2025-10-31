import csv
import sys
import os

def obtener_nombre_archivo():
    if len(sys.argv) < 2:
        print("Uso: python main.py <nombre_archivo.csv>")
        sys.exit(1)
    nombre_archivo = sys.argv[1]
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe")
        sys.exit(1)
    return nombre_archivo

def solicitar_formato_salida():
    formato = input("Ingrese el formato de salida entr trama, xml o json): ").strip().lower()
    if formato not in ("trama", "xml", "json"):
        print("Formato no valido.")
        sys.exit(1)
    return formato

def leer_csv(nombre_archivo):
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        filas = list(lector)
        columnas = lector.fieldnames
    return columnas, filas

def seleccionar_columnas(columnas):
    print("\nColumnas disponibles:")
    for i, col in enumerate(columnas, start=1):
        print(f"{i}- {col}")
    usar_todas = input("\n¿Desea usar todas las columnas? (s/n): ").strip().lower()
    if usar_todas == "s":
        return columnas
    seleccion = input("Ingrese los números de las columnas a usar separados por coma: ").strip()
    try:
        indices = [int(x.strip())-1 for x in seleccion.split(",")]
        seleccionadas = [columnas[i] for i in indices if 0 <= i < len(columnas)]
    except ValueError:
        print("Entrada inválida")
        sys.exit(1)
    if not seleccionadas:
        print("No se seleccionaron columnas válidas.")
        sys.exit(1)
    return seleccionadas
