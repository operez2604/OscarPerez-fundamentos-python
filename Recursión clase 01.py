# Función que muestra una cuenta regresiva
# 5...4...3..2...1

import time

# def cuenta_regresiva_iterativa(n):
#     for i in range(n,0,-1):
#         print(i, end="...")
#         time.sleep(0.5)
#     print("¡Despegue!")

# def cuenta_regresiva_recursiva(n):
#         if n<=0:
#             print("¡Despegue!")
#         else:
#             print(n,end="...")
#             time.sleep(0.5)
#             cuenta_regresiva_recursiva(n-1)
# cuenta_regresiva_recursiva(10)
#cuenta_regresiva_iterativa(10)


# Crear dos funcione (iterativa y recursiva) que genere y devuelva el abecedario


def generar_alfabeto_iterativo():
    alfabeto=''
    letra = 'a'
    for i in range(ord('a'),ord('z')+1,1): #ord a numero ascii
        alfabeto += chr(i) + ', '
    alfabeto=alfabeto.rstrip(', ') #rstrip elimina la ultima coma
        #print(chr(i)) #chr un numero a letra 
    return alfabeto
#lista=generar_alfabeto_iterativo()
print(generar_alfabeto_iterativo())


def generar_alfabeto_recursivo(letra):
    if letra == 'z':
        return'z'
    return letra + ", " + generar_alfabeto_recursivo(chr(ord(letra)+1))
print(generar_alfabeto_recursivo('a'))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print (factorial(5))

# Crear una función que cuente recursivamente los vecinos en una matriz binaria
# Condición: contar vecinos que se encuentren horizontal y verticalmenete (NO en las esquinas)

