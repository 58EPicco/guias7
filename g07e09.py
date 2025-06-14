def promedio(numeros):
    return sum(numeros) / len(numeros)

def mayor_que(numeros, valor):
    mayores = []
    for n in numeros:
        if n > valor:
            mayores.append(n)
    return mayores

# Programa principal
cantidad = int(input("¿Cuántos números desea ingresar? "))
numeros = []
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

prom = promedio(numeros)
print(f"El promedio es: {prom}")

mayores = mayor_que(numeros, prom)
print("Números mayores que el promedio:", mayores)

