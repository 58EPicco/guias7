letras = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'x', 'y', 'z']
vocales = 'aeiou'
contador = 0

for letra in letras:
    if letra.lower() in vocales:
        contador += 1

        
print(f'Hay {contador} vocales en la lista de letras.')





