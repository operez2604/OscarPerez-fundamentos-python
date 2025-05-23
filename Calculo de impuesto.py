'''
Clase:        Clase 08
Tema:         Fase de fortalecimiento logico
Ejercicio:    Cálculo de impuesto
Descripción:  Calculo del impuesto asignado al producto por unidad

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''
unidades=int(input("Ingresar las unidades consumidas: "))

if unidades<=100:
    impuesto=0
elif unidades<=200:
    impuesto=unidades*0.5
else:
    impuesto = unidades*0.7
print(f"Impuesto aplicado: ${impuesto:}")