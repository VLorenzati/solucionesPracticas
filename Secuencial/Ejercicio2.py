"""Un pintor de casas debe hacer un presupuesto para un cliente. Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
cliente le indica que necesita conocer el costo de mano de obra para pintar una pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para pintar la pared.
"""
pintor_monto = int(input("Ingrese el monto que cobra el pintor por cada metro cuadrado: "))
metros_cuadrados = int(input("Ingrese la cantidad de metros cuadrados a calcular: "))

print(f"El costo de mano de obra para pintar {metros_cuadrados} metros cuadrados es: ", metros_cuadrados * pintor_monto)

