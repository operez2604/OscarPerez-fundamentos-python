'''
Clase:        Clase 09
Tema:         Fase de fortalecimiento logico
Ejercicio:    Eliminando valores repetidos
Descripción:  Genera correos para Key

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

# Ingresar los numeros con espacio entre ellos (1 2 3 4 5)
numbers= input()
checknumber= numbers.split()
checkednumbers=[]

for num in checknumber:
    if num not in checkednumbers:
        checkednumbers.append(num)

for result in checkednumbers:
    print(result, end="")
