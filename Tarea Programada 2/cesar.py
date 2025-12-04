# Implementación del Cifrado Cesar

def cifrar_cesar(texto, desplazamiento):
    """Cifra un texto usando la cifra de César con un desplazamiento dado."""
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = 'A' if caracter.isupper() else 'a'
            nueva_letra = chr((ord(caracter) - ord(base) + desplazamiento) % 26 + ord(base))
            resultado += nueva_letra
        else:
            resultado += caracter
    return resultado


def descifrar_cesar(texto, desplazamiento):
    """Descifra un texto cifrado con César."""
    return cifrar_cesar(texto, -desplazamiento)
