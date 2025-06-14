def recu(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + recu(cadena[:-1])

# Ejemplo de uso
print(recu('pablokan'))           # naklobap
print(recu('Hola, cómo estás?'))  # ?sátse omóc ,aloH