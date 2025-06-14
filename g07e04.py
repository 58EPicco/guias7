#Contar la cantidad de palabras. 
def contar_palabras(cadena):
    palabras = cadena.split()
    contador = 0
    for palabra in palabras:
        if palabra.strip('.,;:!?'):
            contador += 1
    return contador


