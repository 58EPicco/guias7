def reemplazar_palabra(texto, palabra_buscar, palabra_reemplazo):
    palabras = texto.split()
    for i in range(len(palabras)):
        palabra_limpia = palabras[i].strip('.,;:!?')
        if palabra_limpia == palabra_buscar:

            palabras[i] = palabras[i].replace(palabra_buscar, palabra_reemplazo)
    return ' '.join(palabras)

texto = 'Quiero comer peras, solamente peras.'
nuevo_texto = reemplazar_palabra(texto, 'peras', 'manzanas')
print(nuevo_texto)