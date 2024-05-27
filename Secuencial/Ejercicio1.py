## UN ESTUDIANTE ESTA CURSANDO 5 materias, QUIERE SABER EL PROMEDIO
nota1 = float(input("Ingrese la nota de la primera materia: "))
nota2 = float(input("Ingrese la nota de la segunda materia: "))
nota3 = float(input("Ingrese la nota de la tercera materia: "))
nota4 = float(input("Ingrese la nota de la cuarta materia: "))
nota5 = float(input("Ingrese la nota de la quinta materia: "))

cantidadNotas = 5

sumatotal = nota1 + nota2 + nota3 + nota4 + nota5

prom = sumatotal / cantidadNotas
print(f"El promedio de las notas es: {prom}")