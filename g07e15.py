#g07e15.py
def suma_digitos(numero):
    suma = 0
    for digito in str(abs(numero)):
        suma += int(digito)
    return suma
# Ejemplo de uso
num = int(input("Ingrese un número entero: "))  
print("La suma de los dígitos es:", suma_digitos(num))
