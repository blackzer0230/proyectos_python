# una calculadora como el ejercicio 3 pero cada operacion es una funcion por separado
print("calculadora")

def suma(num_one, num_two):
    resultado = num_one + num_two
    resultado = round(resultado, 2)
    return resultado

def resta(num_one, num_two):
    resultado = num_one - num_two
    resultado = round(resultado, 2)
    return resultado

def multiplicacion(num_one, num_two):
    resultado = num_one * num_two
    resultado = round(resultado, 2)
    return resultado

def division(num_one, num_two):
    if num_two == 0:
        return "Error. no se puede dividir entre 0"
    else:
        resultado = num_one / num_two
        resultado = round(resultado, 2)
    return resultado

def menu():
    print("""
+. Suma
-. Resta
*. Multiplicación
/. División""")
    return




menu()
operador = input("-> ")
num_one, num_two = map(float, input("ingrese los 2 valores: ").split(" "))

if operador == "+":
    print(suma(num_one, num_two))
elif operador == "-":
    print(resta(num_one, num_two))
elif operador == "*":
    print(multiplicacion(num_one, num_two))
elif operador == "/":
    print(division(num_one, num_two))
else:
    print("operador no valido")