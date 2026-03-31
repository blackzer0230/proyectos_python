# hacer un programa que hago la plata de multiplicar con el numero que digite el usuario
print("vamos hacer una tabla de multiplicar por el numero que digites")
tabla = int(input("-> "))

for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")