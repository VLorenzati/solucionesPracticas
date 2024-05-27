# Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”
persona = input(f"Ingresa un nombre de persona, cuando quieras terminar tipea el valor: fin     ")
while persona != "fin":
    print(persona)
    persona = input("Ingresa otro nombre: ")
    