'''
Clase:        Clase 08
Tema:         Fase de fortalecimiento logico
Ejercicio:    sumdor de valores posicionales
Descripción:  Pide un number al usuario y sum sus digits hasta que quede solo un digit.

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''
number = int(input("Ingresa un número: "))

while number >= 10:
    sum = 0
    for digit in str(number):
        sum += int(digit)
    print(f"{number} = {sum}")
    number = sum

print(f"\nEl resultado final es: {number}")
