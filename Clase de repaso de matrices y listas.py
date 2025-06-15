lista = [ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# Accediendo a la fila uno
lista[0]

# Accediendo a la celeda 3,2
lista[2][1]

cubo = []

# para recorrer una matriz es siempre con un for anidado

# for fila in lista:
#     for celda in fila:
#         print (f"{celda},",end="")
#     print()

# Segunda forma
for i in range(len(lista)):
    for j in range(len(lista[i])): # len cuenta -1
        print (f"{lista[i][j]},",end="")
    print()