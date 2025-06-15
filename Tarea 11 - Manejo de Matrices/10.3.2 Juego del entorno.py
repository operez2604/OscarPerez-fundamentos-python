'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    Diagonal, principal y secundaria
Descripción:  Recorre cada celda y verifica sus 8 vecinas posibles, sumando las que tienen un 1

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''


N = int(input())
M = int(input())

matriz = [list(map(int, input().split(','))) for _ in range(N)]

neighbors = [(-1,-1), (-1,0), (-1,1),
        (0,-1),         (0,1),
        (1,-1), (1,0),  (1,1)]

for i in range(N):
    fila = []
    for j in range(M):
        suma = 0
        for dx, dy in neighbors:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < M:
                suma += matriz[ni][nj]
        fila.append(suma)
    print(fila)
