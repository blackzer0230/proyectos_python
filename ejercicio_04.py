# Haga un ejercicio que pida si es menor de edad(y diga cuanto falta para ser mayor de edad)
# si es mayor de edad(y diga cuando anios tiene siendo mayor de edad) y si acaba de cumplir los 18

print("por favor digite tu edad!!!")
edad = int(input("-> "))


if edad < 18:
    print(f"eres menor de edad y te faltan {18 - edad} para ser mayor de edad")
elif edad > 18:
    print(f"eres mayor de edad y llevas {edad - 18} siendolo")
else:
    print(f"acabas de cumplir los 18!! felicidades!!! ")