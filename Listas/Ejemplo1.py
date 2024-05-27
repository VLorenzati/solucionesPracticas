"""
Crear una lista de 5 numeros al azar entre 0 y 9, que esten ordenados y no repertidos
"""
"""
i = 1
lista = []
print("Ingrese 5 numeros:")
while i != 6:
    lista += (input(f"Este es el {i} numero.... "))
    i += 1
lista.sort()
print(lista)
"""

import random

lista = []

numero = random.randint(0,9)

while len(lista) < 5:
    if numero not in lista:
        lista.append(numero)
    numero = random.randint(0,9)

lista.sort()
print(lista)