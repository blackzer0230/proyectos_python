# crear un program que imprima del 1 al 100 
# ero con estas reglas:
# Si el número es divisible entre 3 imprime Fizz
# Si el número es divisible entre 5 imprime Buzz
# Si es divisible entre 3 y 5 imprime FizzBuzz
# Si no es ninguno, imprime el número normal

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)