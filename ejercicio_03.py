# Un programa que diga si el numero es par o impar usando el operador % (modulo)

print("Vamos a ver si tu numero es impar o par")
valor = int(input("ingrese el valor: "))

if valor % 2 == 0:
    print(f"el numero {valor} es par")
else:
    print(f"el numero {valor} es impar")

