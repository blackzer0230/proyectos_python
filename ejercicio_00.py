# ejercicio #1 hacer un programa que pida tu nombre, edad e imprima por consola tu nombre + en 10 anios 


def completo(nombre, edad):
    print(f"usted se llama {nombre} y en 17 anios vas a tener {edad + 17}")

print("escriba su nombre")
nombre = input("--> ")

print("digite su edad")
edad = int(input("--> "))

completo(nombre, edad)