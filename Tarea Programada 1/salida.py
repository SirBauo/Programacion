def guardar_archivo(nombre_base, extension, contenido):
    nombre_salida = f"{nombre_base}{extension}"
    with open(nombre_salida, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"\nArchivo generado exitosamente: {nombre_salida}")
