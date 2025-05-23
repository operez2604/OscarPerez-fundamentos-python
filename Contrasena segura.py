'''
Clase:        Clase 08
Tema:         Fase de fortalecimiento logico
Ejercicio:    Contraseña segura
Descripción:  Verifica si una contraseña es segura o no

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

contraseña=input("Ingresa tu contraseña: ")

eightcaracter=len(contraseña) >= 8
mayuscula=any(c.isupper() for c in contraseña)
numeros=any(c.isdigit() for c in contraseña)

if eightcaracter and mayuscula and numeros:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")