#Estructuras condicionales (if, elif y else)

condición1 = (5 == 5)
condición2 = (4 == 4)

if condición1:
    print("Como 5 es igual a 5, entraría en este if y no iríamos al elif")
elif condición2:
    print("Si el if de la condición 1 no se cumple, entramos aqui porque 4 es igual a 4")
else:
   print("Si las dos condiciones anterior fueran incorrectas, se entraría aquí por defecto")

#Bucles for y while
for i in range(5):
    print(i) #Para programacion, el primer número es el 0, no el 1

#Mientras sea True o Verdadero se ejecuta el código (cuando contador sea mayor o igual a 5, no entra en el while)
contador = 0
while contador < 5:
    print(contador)
    contador += 1 #Para concatenar, si la primera vez 1, la segunda sería (1+=1) = 2, y así sucesivamente

#Colecciones Básicas

lista = [1, 2, 3, 4, 5] #Secuencia ordenada y mutable
tupla = (1, 2, 3, 4, 5) #Secuencia ordenada e inmutable
conjunto = {1, 2, 3, 4, 5} #Colección no ordenada sin elementos duplicados.
diccionario = {'nombre': 'Ana', 'edad': 25} #Colección de pares clave-valor

#List Comprehensions
multiplicar_por_2 = [x*2 for x in range(10)] #Sintaxis para crear listas en base a una expresión (multiplicar números x 2)
print(multiplicar_por_2)

cuadrados = [x**2 for x in range(10)] #Sintaxis para crear listas en base a una expresión (elevar números al cuadrado)
print(cuadrados)
