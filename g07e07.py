def carga():
    nombres = []
    sexos = []
    for i in range(8):
        nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
        sexo = input(f"Ingrese el sexo de {nombre} (M/F): ").strip().upper()
        nombres.append(nombre)
        sexos.append(sexo)
    return nombres, sexos

def mostrar_mujeres(nombres, sexos):
    print("Nombres de las mujeres:")
    for i in range(len(nombres)):
        if sexos[i] == 'F':
            print(nombres[i])

nombres, sexos = carga()
mostrar_mujeres(nombres, sexos)