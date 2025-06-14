#g07e10.py
#Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

def cargar_lluvias():
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    lluvias = []
    for dia in dias:
        mm = float(input(f"Ingrese la lluvia caída en mm para {dia}: "))
        lluvias.append(mm)
    return dias, lluvias

def total_lluvia(lluvias):
    return sum(lluvias)

def dia_mas_lluvia(dias, lluvias):
    indice = lluvias.index(max(lluvias))
    return dias[indice]

# Programa principal
dias, lluvias = cargar_lluvias()
print(f"Total de lluvia caída en la semana: {total_lluvia(lluvias)} mm")
print(f"El día que más llovió fue: {dia_mas_lluvia(dias, lluvias)}")



