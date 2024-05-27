"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). Desarrolle una solución algorítmica para
saber cuento debe pagar el cliente.
"""
# V es las unidades que compra el cliente
# leche = 1000
# si 12u =< V and V <=24u tiene un descuento del 10%
# si V >24u tiene 15% de descuento
# si el cliente es jubilado se le suma un 10% de descuento adicional


#ENTRADA
unidadesL = int(input("Ingrese la cantidad de unidades de leche que va comprar:"))
jub = str(input("Es una persona jubilada? ------ Ingrese Si/No: "))
while jub.lower() != "si" and jub.lower() != "no":
    print("Error, ingrese, si es una persona jubilada o no (Si/No)")
    jub = input("Es una persona jubilada?: ")

#DESCUENTO / PROCESO
des = 0
if 12 <= unidadesL and unidadesL <= 24:
    des = 10
if unidadesL > 24:
    des = 15
if jub.lower() == "si":
    des += 10
print(des)
#SALIDA
precioSinDes = unidadesL * 1000
pago = print(f"El costo total es de:{precioSinDes - precioSinDes * (des * 0.01)} pesos")

