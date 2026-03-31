# haga un pograma que pida el color de los semaforos y diga que tiene que hacer
# Si escribe rojo:
# 🔴 STOP! Debes detenerte

# # Si escribe amarillo:
# 🟡 PRECAUCIÓN! Prepárate para parar

# # Si escribe verde:
# 🟢 GO! Puedes avanzar

# # Si escribe cualquier otra cosa:
# ❌ Ese color no es válido en un semáforo

print("vamos a simular un semaforo(vas a elegir rojo/amarillo/verde)")
semaforo = input("Escriba: ").lower()


if semaforo == "rojo":
    print("STOP! Debes detenerte")
elif semaforo == "amarillo":
    print("PRECAUCIÓN! Prepárate para parar")
elif semaforo == "verde":
    print("GO! Puedes avanzar")
else:
    print("❌ Ese color no es válido en un semáforo")