# vignere.py
# Implementación de la Cifra de Vigenère

def generar_clave(texto, clave):
    """Extiende la clave para que tenga el mismo largo que el texto."""
    clave = clave.lower()
    clave_repetida = ""
    i = 0
    for caracter in texto:
        if caracter.isalpha():
            clave_repetida += clave[i % len(clave)]
            i += 1
        else:
            clave_repetida += caracter
    return clave_repetida


def cifrar_vignere(texto, clave):
    """Cifrado de texto usando la cifra de Vigenère."""
    texto_cifrado = ""
    clave_extendida = generar_clave(texto, clave)
    for t, k in zip(texto, clave_extendida):
        if t.isalpha():
            base = 'A' if t.isupper() else 'a'
            offset = (ord(t.lower()) - ord('a') + ord(k) - ord('a')) % 26
            texto_cifrado += chr(offset + ord(base))
        else:
            texto_cifrado += t
    return texto_cifrado


def descifrar_vignere(texto, clave):
    """Descifrado de texto cifrado con la cifra de Vigenere."""
    texto_descifrado = ""
    clave_extendida = generar_clave(texto, clave)
    for t, k in zip(texto, clave_extendida):
        if t.isalpha():
            base = 'A' if t.isupper() else 'a'
            offset = (ord(t.lower()) - ord('a') - (ord(k) - ord('a'))) % 26
            texto_descifrado += chr(offset + ord(base))
        else:
            texto_descifrado += t
    return texto_descifrado
