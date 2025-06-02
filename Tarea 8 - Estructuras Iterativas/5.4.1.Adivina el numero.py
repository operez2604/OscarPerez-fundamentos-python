'''
Clase:        Clase 08
Tema:         Fase de fortalecimiento logico
Ejercicio:    Adivina el numero
Descripción:  Genera un numero aleatorio entre 1 y 100

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''
import random

number = random.randint(1, 100)

while True:
    tries = int(input("Adivina el número: "))
    
    if tries < number:
        print("El número secreto es mayor.")
    elif tries > number:
        print("El número secreto es menor.")
    else:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
