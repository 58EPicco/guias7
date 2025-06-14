#g07e12.py
#Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).

def invertir_nombre(nombre_completo):
    partes = nombre_completo.split()
    if len(partes) < 2:
        return "El nombre completo debe contener al menos un nombre y un apellido."
    
    apellido = partes[-1]
    nombre = ' '.join(partes[:-1])
    
    return f"{apellido}, {nombre}"
# Programa principal
nombre_completo = input("Ingrese su nombre completo (ej. Juan Pérez): ")
nombre_invertido = invertir_nombre(nombre_completo)
print(f"Nombre invertido: {nombre_invertido}")