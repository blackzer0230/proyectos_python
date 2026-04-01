# Agendas de contactos donde se agrega, busca, elimina, ve y se sale del programa
import os
contactos = dict()
def menu():
    print("""
1. Agregar contacto
2. Buscar contacto
3. Eliminar contacto
4. Ver todos los contactos
5. Salir""")

while True:
    menu()
    opcion = input("-> ")
    
    if opcion == "1":
        os.system("clear")
        print("\t====== agregando =====")
        
        nombre = input("Ingrese el nombre del contacto: ").lower()
        numero = input("Ingrese el numero del contacto: ")
        contactos[nombre] = {}
        contactos[nombre]["telefono"] = numero
        os.system("clear")
        print(f"se agrego el usuario {nombre} con el numero {numero}")
        
    elif opcion == "2":
        os.system("clear")
        print("\t====== buscar =====")
        
        nombre = input("que contacto buscas: ").lower()
        if nombre in contactos:
            os.system("clear")
            print(f"{nombre} = {contactos[nombre]["telefono"]}")
        else:
            os.system("clear")
            print(f"{nombre} no esta en la lista de contactos")
    
    
    
    elif opcion == "3":
        os.system("clear")
        print("\t====== eliminar =====")  
        
        nombre = input("contacto que desees eliminar: ").lower()
        if nombre in contactos:
            os.system("clear")
            del contactos[nombre]
            print(f"se elimino a {nombre} de la lista")
            
        else:
            os.system("clear")
            print(f"{nombre} no esta en la lista")
          
          
          
    elif opcion == "4":
        os.system("clear")
        print("\t====== ver todos =====")
        for i, nombre in enumerate(contactos, 1):
            print(f"{i}. {nombre} = {contactos[nombre]['telefono']} ")
    
    elif opcion == "5":
        os.system("clear")
        print("saliendo de la agenda")
        break
    
    else:
        os.system("clear")
        print("opcion no valida")