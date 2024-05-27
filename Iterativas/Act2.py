## MISMO ALGORITMO QUE EL N°1 PERO SOLO MOSTRANDO LOS PARES:
nums = int(input("Ingresa un numero: "))
i = 0
for i in range(nums):
    if i % 2 == 0:
        print(i)
if nums % 2 == 0:
    print(nums)
    
print("Fin del programa")

