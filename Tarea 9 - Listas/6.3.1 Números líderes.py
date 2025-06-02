'''
Clase:        Clase 09
Tema:         Fase de fortalecimiento logico
Ejercicio:    Números líderes
Descripción:  Imprime los numeros mayores en una lista, 

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-06-1
Estado:       [ Terminado ]
'''
numbers = list(map(int, input("Lista de numeros: ").split()))
leaders=[]

max_right=-1
for number in reversed (numbers[:-1]):
    if number > max_right:
        leaders.append(number)
        max_right = number

leaders.reverse()
print("Líderes:",*leaders)

