def contar_letra(letra, cadena):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador
#ejemplo.
letra_buscada = 'a'
cadena = 'manzana'
print(f"La letra '{letra_buscada}' se repite {contar_letra(letra_buscada, cadena)} veces en '{cadena}'.")