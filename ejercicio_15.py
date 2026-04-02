# hacer una calculadora pero usado el try/except

# funcion para pedir los valores de la operacion 
def pedir():
    try:
        datos = input("ingrese los 2 valores separsos: ").split(" ")
        num_one = float(datos[0])
        num_two = float(datos[1])
        return num_one, num_two
    except:
        print("no digitaste numeros!")
        return pedir()
    
# funciom de menu
def menu():
    print("""
+. Suma
-. Resta
*. Multiplicación
/. División""")
    operador = input("-> ")
    return operador

def generar(num_one, num_two, operador):
    if operador == "+":
        final = num_one + num_two
        final = round(final, 2)
    elif operador == "-":
        final = num_one - num_two
        final = round(final, 2)
    elif operador == "*":
        final = num_one * num_two
        final = round(final, 2)
    elif operador == "/":
        try:
            final = num_one / num_two
            final = round(final, 2)
        except ZeroDivisionError:
            return "no se puede dividir entre 0"
    return final
        

operador = menu()
num_one, num_two = pedir()
print(f"{generar(num_one, num_two, operador)}")

