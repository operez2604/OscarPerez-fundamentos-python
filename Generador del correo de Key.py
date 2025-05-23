'''
Clase:        Clase 07
Tema:         Fase de fortalecimiento logico
Ejercicio:    Generador del correo de Key
Descripción:  Genera correos para Key

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''
primer_nombre = input("Ingresa tu primer nombre: ")
segundo_nombre = input("Ingresa tu segundo nombre: ")
primer_apellido = input("Ingresa tu primer apellido: ")
segundo_apellido = input("Ingresa tu segundo apellido: ")

correo = primer_nombre.lower() + "." + primer_apellido.lower() + "@keyinstitute.edu.sv"

print("El correo que se debe asignar al usuario ingresado es:", correo)
