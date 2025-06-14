def cargar_palabras(texto):
    for c in ',.;:!?':
        texto = texto.replace(c, '')
    return texto.split()

def longitud_palabra_mas_larga(lista_palabras):
    max_len = 0
    for palabra in lista_palabras:
        if len(palabra) > max_len:
            max_len = len(palabra)
    return max_len

texto = input("Ingrese una frase: ")
palabras = cargar_palabras(texto)
print("La palabra más larga tiene", longitud_palabra_mas_larga(palabras), "letras.")

