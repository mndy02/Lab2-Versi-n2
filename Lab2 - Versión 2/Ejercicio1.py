'''Crear un programa que, regriste que un policía de tránsito reporta a la central un promedio de 
N infracciones en el mes de las cuales el 20% se producen en las horas de la mañana, el 35% se 
producen en horas de la tarde y el 45% restante se producen en horas de la noche'''

print("BIENVENIDO AL PROGRAMA\n")

#Pedir al usuario que ingrese el n° total de infracciones en el mes y almacenarlos en una variable 
totalIn = int(input("Ingrese el número total de infracciones en el mes: "))

#Calcular el número de infracciones en diferentes momentos en el día (mañana, tarde y noche)
mañana = int(totalIn * 0.2)
tarde = int(totalIn * 0.35 )
noche = int(totalIn * 0.45 )

#Calcular el promedio diario (mañana, tarde y noche)
prom_mañana = mañana / 30 
prom_tarde = tarde / 30
prom_noche = noche / 30

#Imprimir los resultados de infracciones diarias 
print("\nPromedio diario de infracciones por la mañana: ", prom_mañana.__round__(2))
print("Promedio diario de infracciones por la tarde: ", prom_tarde.__round__(2))
print("Promedio diario  de infracciones por la noche: ", prom_noche.__round__(2))

print("\nFIN DEL PROGRAMA")