#g07e11.py
#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad. Funciones de carga y cálculo de edad.

def cargar_personas():
    nombres = []
    fechas_nacimiento = []
    cantidad = int(input("¿Cuántas personas desea ingresar? "))
    
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
        fecha_nacimiento = input(f"Ingrese la fecha de nacimiento de {nombre} (DD/MM/AAAA): ")
        nombres.append(nombre)
        fechas_nacimiento.append(fecha_nacimiento)
    
    return nombres, fechas_nacimiento
def calcular_edad(fecha_nacimiento):
    from datetime import datetime
    
    dia, mes, anio = map(int, fecha_nacimiento.split('/'))
    fecha_nac = datetime(anio, mes, dia)
    fecha_actual = datetime.now()
    
    edad = fecha_actual.year - fecha_nac.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day))
    
    return edad
def mostrar_mayores_de_edad(nombres, fechas_nacimiento):
    print("Nombres de las personas mayores de edad:")
    for i in range(len(nombres)):
        edad = calcular_edad(fechas_nacimiento[i])
        if edad >= 18:
            print(nombres[i])       


nombres, fechas_nacimiento = cargar_personas()
mostrar_mayores_de_edad(nombres, fechas_nacimiento)
