import unicodedata

#Funcion para normalizar el texto y quitar acentos.

def normalizar_texto(texto):
    texto = texto.lower()

    texto = unicodedata.normalize('NFD', texto)

    texto = ''.join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != 'Mn'
    )

    return texto