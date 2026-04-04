# hacer un programa que pida un numero y si da un dato que no es entonces vuelva a pedir el numero 

while True:
    try:
        numero = int(input("Ingrese un numero: "))
        print(f"el numero que ingreso es {numero}")
        break
    except:
        print("no ingresaste un numero, por favor intento otro vez")
        