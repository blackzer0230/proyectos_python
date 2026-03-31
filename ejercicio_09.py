# Hacer un progrma que de lista de tareas, poder agregar, eliminar, ver, y salir
tarea = []
print("Bienvenidos a mi lista de tareas pendientes!!")

while True:
    print("""
1. Agregar tarea
2. Eliminar tarea
3. Ver tareas
4. Salir""")
    opcion = input("-> ")
    
    if opcion == "1":
        agregar = input("que desea agregar a la lista: ")
        tarea.append(agregar)
        
    elif opcion == "2":
        eliminar = input("que quieres eliminar: ")
        if eliminar in tarea:
            tarea.remove(eliminar)
            print(f"se elimino {eliminar} de la lista")
        else:
            print(f"no existe{eliminar} en la lista")
                
    elif opcion == "3":
        for i, ii in enumerate(tarea, 1):
            print(f"{i} = {ii}")
            
    elif opcion == "4":
        print("saliendo de la lista de tareas")
        break
    
    else:
        print("dato invalido!! intente otra vez")