def mas_repetido(lista):
    max_cantidad = 0
    mas_frecuente = None
    for num in lista:
        cantidad = lista.count(num)
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            mas_frecuente = num
    return mas_frecuente

# Ejemplo de uso
numeros = [2, 3, 5, 2, 8, 2, 3, 3, 3]
print("El número que más se repite es:", mas_repetido(numeros))
