# Hacer una calculadora simple que muestre un menu de opciones 
# y pensar si el usuario divide entre 0


def operacion(opcion, num_uno, num_two):
    # suma 
    if opcion == "1":
        resultado = num_uno + num_two
    # resta 
    elif opcion == "2":
        resultado = num_uno - num_two

    # multiplicacion
    elif opcion == "3":
        resultado = num_uno * num_two

    # division 
    elif opcion == "4":
        if num_two == 0:
            return "no se puede dividir entre cero(0)"
        else:
            resultado = num_uno / num_two
    return resultado

print("""
      elegir la opcion
1. Suma
2. Resta
3. Multiplicación
4. División
""")
opcion = input("->")

num_uno = float(input("ingrese el primer valor: "))
num_two = float(input("ingrese el segundo valor: "))

print(operacion(opcion, num_uno, num_two))

