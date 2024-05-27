# Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 


print("Ingrese 10 nombres, no repetidos")
nombre = str(input("Ingrese el primer nombre: "))
lista = []
while len(lista) < 10:
    print(lista)
    if nombre not in lista:
        lista.append(nombre)
        nombre = str(input("Ingrese otro nombre: "))

print(lista)