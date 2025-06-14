def contiene_todas_vocales(cadena):
    vocales = set('aeiou')
    cadena = cadena.lower()
    return vocales.issubset(set(cadena))

# Ejemplo de uso
texto = input("Ingrese una cadena: ")
if contiene_todas_vocales(texto):
    print("La cadena contiene todas las vocales.")
else:
    print("La cadena NO contiene todas las vocales.")