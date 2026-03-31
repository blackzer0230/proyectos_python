# hacer un programa que convierta Celsius en Fahrenheit
# (claude tambien hare que lo haga en viseversa)

def temperatura(opcion, grado):
    # Celsius en Fahrenheit
    if opcion == "1":
        resultado = (grado * 1.8) + 32
    # Fahrenheit en Celsius
    elif opcion == "2":
        resultado = (grado - 32) / 1.8

    return resultado


print("""
Convertir:
1.   °C -> °F
    
2.   °F -> °C""")
opcion = input("-> ")


grado = float(input("ingrese el grado: "))

print(f"{temperatura(opcion, grado):.2f}")
