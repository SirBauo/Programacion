def leer_lineas(ruta_archivo):
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        lineas = archivo.readlines()
    except:
        print("Error al abrir archivo.")
        return None
    else:
        return lineas
    finally:
        try:
            archivo.close()
        except:
            pass
        print("Fin de leer_lineas")


def leer_texto_completo(ruta_archivo):
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        contenido = archivo.read()
    except:
        print("Error al abrir archivo.")
        return None
    else:
        return contenido
    finally:
        try:
            archivo.close()
        except:
            pass
        print("Fin de leer_texto_completo")


def leer_primera_linea(ruta_archivo):
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        linea = archivo.readline()
    except:
        print("Error al abrir archivo.")
        return None
    else:
        return linea
    finally:
        try:
            archivo.close()
        except:
            pass
        print("Fin de leer_primera_linea")


def leer_palabras(ruta_archivo):
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        contenido = archivo.read()
    except:
        print("Error al abrir archivo.")
        return None
    else:
        return contenido.split()
    finally:
        try:
            archivo.close()
        except:
            pass
        print("Fin de leer_palabras")


def leer_n_lineas(ruta_archivo, n):
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        resultado = []
        contador = 0
        for linea in archivo:
            resultado.append(linea)
            contador += 1
            if contador == n:
                break
    except:
        print("Error al abrir archivo.")
        return None
    else:
        return resultado
    finally:
        try:
            archivo.close()
        except:
            pass
        print("Fin de leer_n_lineas")
