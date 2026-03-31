# adivinar el numero pero vamos hace rque python eliga el numero del 1 al 100
import random

numero = random.randint(1, 100)
contador = 0

while True:
    adivina = int(input("adivina el numero: "))

    if adivina < numero:
        print("muy bajo")
        contador += 1

    elif adivina > numero:
        print("muy alto")
        contador += 1

    else:
        contador += 1
        print(f"felicidades adivinaste el numero en {contador} intentos")
        break

