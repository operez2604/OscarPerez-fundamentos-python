'''
Clase:        Clase 07
Tema:         Fase de fortalecimiento logico
Ejercicio:    Automatizando el cálculo de la propina
Descripción:  Calculo del total a pagar agregando propina

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

total=float(input("Ingresa el total de la cuenta: $"))
propinaper=float(input("Ingresa el porcentaje de propina (10 para 10%): "))

propina= total * (propinaper/100)
totalpayment= total + propina

print(f"Total de la cuenta: ${total}")
print(f"Propina del {propinaper}%: ${propina}")
print(f"Total a pagar: ${totalpayment}")