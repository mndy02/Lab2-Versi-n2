'''Desarrolle un programa que solicite tres números enteros desde teclado al uasuario, luego el programa deberá 
determinar e indicar a tráves de un mnesaje en pantalla, cuál de los tres es el más grande sin importar el orden
en el que se ingresen los números, así mismo el número más pequeño y el de en medio'''

print("BIENVENIDO AL PROGRAMA\n")

#Pedir al usuario que ingrese tres números enteros 
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

#Calcular cual es el número máximo, mediano y mínimo
numMax = max(num1, num2, num3)
numMin = min(num1, num2, num3)
numMed = (num1 + num2 + num3) - numMax - numMin

#Imprimir los resultados
print("\nEl número", numMax,"es el más grande de los tres")
print("El número", numMin, "es el más pequeño de los tres")
print("El número", numMed, "es el número mediano de los tres\n")

print("FIN DEL PROGRAMA")