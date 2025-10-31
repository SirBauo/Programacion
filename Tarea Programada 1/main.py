import os
from entrada import obtener_nombre_archivo, solicitar_formato_salida, leer_csv, seleccionar_columnas
from conversiones import convertir_a_xml, convertir_a_json, convertir_a_trama
from salida import guardar_archivo

def main():
    # Obtener el CSV
    nombre_archivo = obtener_nombre_archivo()
    
    # Preguntar formato
    formato = solicitar_formato_salida()
    
    # Leer CSV
    columnas, filas = leer_csv(nombre_archivo)
    
    # Preguntar columnas
    columnas_usadas = seleccionar_columnas(columnas)
    
    # Preparar nombre base del archivo
    nombre_base = os.path.splitext(nombre_archivo)[0]
    
    # Convertir
    if formato == "xml":
        contenido = convertir_a_xml(nombre_base, filas, columnas_usadas)
        extension = ".xml"
    elif formato == "json":
        contenido = convertir_a_json(filas, columnas_usadas)
        extension = ".json"
    else:
        contenido = convertir_a_trama(filas, columnas_usadas)
        extension = ".dat"
    
    # Guardar archivo
    guardar_archivo(nombre_base, extension, contenido)

if __name__ == "__main__":
    main()
