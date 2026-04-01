# adivinar cuantas x letras hay en una palabra
palabra = input("ingrese la palabra: ")
letra = input("ingrese la letra a contar: ")
buscar = letra
contador = 0
for letra in palabra:
    if letra == buscar:
        contador += 1
print(f"hay {contador} {buscar}")