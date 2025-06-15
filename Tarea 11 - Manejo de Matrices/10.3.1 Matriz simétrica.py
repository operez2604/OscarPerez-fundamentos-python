'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    Diagonal, principal y secundaria
Descripción:  Compara los elementos por encima y debajo de la diagonal

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
n = int(input())

matriz = [list(map(int, input().split(','))) for _ in range(n)]

simetric = True
for i in range(n):
    for j in range(i+1, n):
        if matriz[i][j] != matriz[j][i]:
            simetric = False
            break

if simetric:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
