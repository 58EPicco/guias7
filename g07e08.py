def cargar_nombres():
    nombres = []
    cantidad = int(input("¿Cuántos nombres desea ingresar? "))
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
    return nombres

# Programa principal
nombres = cargar_nombres()
buscar = input("Ingrese el nombre a buscar: ")

if buscar in nombres:
    posicion = nombres.index(buscar)
    print(f"El nombre '{buscar}' está en la posición {posicion}.")
else:
    print(f"El nombre '{buscar}' no se encuentra en la lista.")