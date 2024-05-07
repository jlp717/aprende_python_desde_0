#Ejercicio 1: Crear un programa que pida al usuario su nombre y edad, y lo salude.
nombre = input("Introduce su nombre: ")
edad = int(input("Introduce tu edad: "))
print(f"Hola, eres {nombre} y tienes {edad} años")

#Ejercicio 2: Escribir un programa que calcule el área de un triángulo dado su base y altura.
base = float(input("Introduce la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))
calcular_area = ((base * altura) / 2)
print(f"Tu triángulo tiene una base de {base}, una altura de {altura}, y su área es: {calcular_area}")

#Ejercicio 3: Realizar un programa que determine si un número ingresado es par o impar.
numero = int(input("Ingresa tu número para ver si es par o inpar: "))

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
