'''
Clase:        Clase 07
Tema:         Introducción al manejo de datos tabulares con NumPy
Ejercicio:    Adivina el numero
Descripción:  Cuestionario al final del código

Autor:        Oscar Enrique Pérez Osorio
Fecha:        2025-06-03
Estado:       [ Terminado ]
'''
import numpy as np

# 2. Caso de Estudio: Consumo Energético
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# Exploración inicial de los datos
print("Dimensiones:",consumo.ndim)                      # 2(filas y columnas)
print("Forma:",consumo.shape)                           # (10,7) -> 10 filas y 7 columnas
print("Tipo de dato:",consumo.dtype)                    # float64 (números decimales)
print("Consumo del primer hogar:",consumo[0])           # Todos los datos de la fila 0
print("Consumo el miércoles (Día 3):",consumo[:,2])     # Todos los datos de la columna 2

# Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo,axis=1)

# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo,axis=0)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print("Promedio de consumo por hogar:",promedio_por_hogar)
print("Promedio de consumo diario de todos los hogares:",promedio_por_dia)
print("Total de consumo en la semana de los 10 hogares:",total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis=1)

# Mínimo por día
minimos = np.min(consumo, axis=0)

# Desviación estándar global
desviacion = np.std(consumo)

print("Maximos: ",maximos)
print("Minimos: ",minimos)
print("Desviación", desviacion)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)

# Indice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)

# Indice del hogar con mejor consumo
hogar_mas_eficiente=np.argmin(consumo_total_hogar)

print("Consumo total hogar:",consumo_total_hogar)
print("Hogar consumo mayor",hogar_mayor_consumo)
print("Hogar más eficiente", hogar_mas_eficiente)

# Suma por hogar (semana)
consumo_total_hogar=np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana:{consumo_total_hogar}")

# Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar>100
# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"ID's de hogares con consumo mayor a 100:{consumo_mayor_100}")

# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado=(consumo-consumo.min())/(consumo.max()-consumo.min())

# Resultado
print(f"Consumo normalizado:{consumo_normalizado}")

# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumo_hogar5_fri = consumo[4, 4]
print("1. Consumo del hogar 5 el viernes:", consumo_hogar5_fri)

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
consumo_ultimos3_sun = consumo[-3:, 6]
print("2. Consumo de los últimos 3 hogares el domingo:", consumo_ultimos3_sun)
# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
weekends = consumo[:, 5:7]
weekendsprom = np.mean(weekends)
print("3. Promedio de consumo en fines de semana:", weekendsprom)
# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desviacion_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviacion_por_dia)
print("4. Día con mayor desviación estándar:", dia_mayor_desviacion)
print("   Esto indica que ese día los consumos entre hogares fueron más variables.")
# 5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print("5. Índices de los 3 hogares con menor consumo total:", indices_menor_consumo)
print("   Valores de consumo total de esos hogares:", valores_menor_consumo)
# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
consumo_hogar3 = consumo[2]
consumo_hogar3_incrementado = consumo_hogar3 * 1.10
nuevo_total_hogar3 = np.sum(consumo_hogar3_incrementado)
print("6. Nuevo consumo total del hogar 3 tras aumento del 10% diario:", nuevo_total_hogar3)