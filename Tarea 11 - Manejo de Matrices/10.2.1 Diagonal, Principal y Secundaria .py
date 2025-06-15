'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    Diagonal, principal y secundaria
Descripción:  Crea la matriz, extrae cada diagonal y muestra el resultado

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
n = int(input())

matriz = [list(map(int, input().split(','))) for _ in range(n)]

principal = [matriz[i][i] for i in range(n)]

secundaria = [matriz[i][n-1-i] for i in range(n)]

print(principal)
print(secundaria)
