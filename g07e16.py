def es_entero(cadena):
    return cadena.isdigit()

# Ejemplo de uso
texto = input("Ingrese una cadena: ")
if es_entero(texto):
    print("La cadena contiene solo caracteres numéricos.")
else:
    print("La cadena NO contiene solo caracteres numéricos.")
