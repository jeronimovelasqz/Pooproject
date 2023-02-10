

#1Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla.
"""nombre = input("Por favor ingrese su nombre: ")
edad = input("Por favor ingrese su edad: ")

print("Su nombre es: " + nombre)
print("Su edad es: " + edad)"""



#2Escribir una función que calcule el área de un círculo dado su radio.
"""import math

def area_circulo(radio):
    area = math.pi * radio**2
    return area"""



#3Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
"""import random

def generar_numero_aleatorio(numeros_aleatorios, cantidad_restante):
    if cantidad_restante == 0:
        return numeros_aleatorios
    else:
        numero = random.randint(1, 100)
        numeros_aleatorios.append(numero)
        return generar_numero_aleatorio(numeros_aleatorios, cantidad_restante - 1)

numeros_aleatorios = []
resultado = generar_numero_aleatorio(numeros_aleatorios, 10)
print(resultado)
"""


#4Escribir un programa que determine si un número dado es par o impar.
"""def es_par(numero):
    if numero == 0:
        return True
    elif numero == 1:
        return False
    else:
        return es_par(numero - 2)

numero = int(input("Por favor ingrese un número: "))

if es_par(numero):
    print(str(numero) + " es un número par")
else:
    print(str(numero) + " es un número impar")"""


#5f a celsius
"""def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Por favor ingrese la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print("La temperatura en grados Celsius es: " + str(celsius))"""



#6Crear un programa que calcule la suma de los números en una lista dada usando recursion
"""def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(numeros)
print("La suma de los números en la lista es: " + str(resultado))"""


#7Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada. usando recursion
"""def min_max(lista):
    if len(lista) == 1:
        return (lista[0], lista[0])
    else:
        num1, num2 = min_max(lista[1:])
        return (min(lista[0], num1), max(lista[0], num2))

numeros = [5, 4, 1, 8, 7, 2, 6, 3]
resultado = min_max(numeros)
print("El número más pequeño es: " + str(resultado[0]))
print("El número más grande es: " + str(resultado[1]))"""



#8Crear una función que invierta el orden de los elementos en una lista dada. usando recursion
"""def inverso(lista):
    if len(lista) == 0:
        return []
    else:
        return inverso(lista[1:]) + [lista[0]]

numeros = [1, 2, 3, 4, 5]
resultado = inverso(numeros)
print("La lista invertida es: " + str(resultado))"""


#9Crear un programa que genere una matriz de números y la imprima en pantalla. usando recursion
"""def generar_matriz(filas, columnas):
    if filas == 0:
        return []
    else:
        fila = [0] * columnas
        return [fila] + generar_matriz(filas - 1, columnas)

def imprimir_matriz(matriz):
    if matriz == []:
        return
    else:
        print(matriz[0])
        imprimir_matriz(matriz[1:])

filas = 3
columnas = 4
matriz = generar_matriz(filas, columnas)
imprimir_matriz(matriz)"""

#10factorial
"""def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)"""

#11 Crear un programa que genere una lista de números pares entre 1 y 100
"""def generate_even_numbers(n):
    even_numbers = []
    for i in range(2, n+1, 2):
        even_numbers.append(i)
    return even_numbers

print(generate_even_numbers(100))"""


#12 Crear un programa que imprima los números del 1 al 10 utilizando un ciclo for
"""for i in range(1, 11):
    print(i)"""



#.13 Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división
"""num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)"""


#14 Escribir una función que calcule la media aritmética de una lista de números

"""def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(average(numbers))"""


#15 palindrome
"""def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

text = input("Ingrese una cadena de texto: ")

if is_palindrome(text):
    print("La cadena de texto es un palíndromo.")
else:
    print("La cadena de texto no es un palíndromo.")"""