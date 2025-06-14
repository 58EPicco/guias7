#Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes). El resultado es el total general.

def contar_letras(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isalpha():
            contador += 1
    return contador

# Ejemplo de uso:
texto = input("Ingrese un texto: ")
total = contar_letras(texto)
print(f"Cantidad total de letras: {total}")