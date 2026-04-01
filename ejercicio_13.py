# numeros primero son lols que se dividen entre ellos y 1
numero = int(input("ingrese el numero: "))

def primo(numero):
    if numero <= 1: return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
        
        
if primo(numero):
    print("es primo")
else:
    print("no es primo")