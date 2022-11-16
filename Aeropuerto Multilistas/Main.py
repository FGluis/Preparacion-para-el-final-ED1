from Listas import Lista_Vuelos, Lista_Pasajeros

#Dejaremos estos datos como iniciales puedes cambiarlos si deseas 
Max_capacidad = 3   #Recuerda cambiar esto en la clase de listas.
#=======================================================================================
vuelos = [["1", "Barranquilla", "bogota" ],["2", "Medellin", "San Andres" ],
          ["3", "Cali", "Cartagena"],["4", "Santa Marta", "Bucaramenga"]]
pasajeros_vuelo1 = [["Luis", 100], ["Eliana", 110], ["Jesus", 120]]
pasajeros_vuelo2 = [["Naim", 620], ["Jose", 730]]
pasajeros_vuelo3 = [["Steven", 150]]
pasajeros_vuelo4 = [["Moises", 130], ["Racedo", 140], ["Bernardo", 950]]
espera_1 = [["Mathilda", 160], ["Pedro", 170], ["Ismael",180]]
espera_2 = []
espera_3 = []
espera_4 = [["Elder", 190],["Andres", 510]]
Vuelos = Lista_Vuelos()
Vuelos.add_multiple_nodes(vuelos)
Vuelos.head.Lista_Pasajeros.add_multiple_nodes(pasajeros_vuelo1)
Vuelos.head.Lista_espera.add_multiple_nodes(espera_1)
Vuelos.head.next.Lista_Pasajeros.add_multiple_nodes(pasajeros_vuelo2)
Vuelos.head.next.Lista_espera.add_multiple_nodes(espera_2)
Vuelos.head.next.next.Lista_Pasajeros.add_multiple_nodes(pasajeros_vuelo3)
Vuelos.head.next.next.Lista_espera.add_multiple_nodes(espera_3)
Vuelos.head.next.next.next.Lista_Pasajeros.add_multiple_nodes(pasajeros_vuelo4)
Vuelos.head.next.next.next.Lista_espera.add_multiple_nodes(espera_4)
#===========================================================================================

Opcion = 0
print("|=============================================|")
print("|             Vuelos inteligentes             |")
print("|=============================================|")
print("                                               ")
while(Opcion != 10):
    print(" Ingrese el numero correspondinte a la acción\n que deseas hacer:")
    print(" (1) Buscar Vuelo \n (2) Borrar un vuelo \n (3) Buscar pasajero \n (4) Eliminar pasajero \n (5) Crear vuelo \n (6) Agregar pasajero \n (7) Agregar pasajero a cola \n (8) Buscar Pasajero en cola \n (9) Eliminar pasajero en cola \n (10) Salir")
    print("Ingrese su opción: ")
    Opcion = int(input())
    while(Opcion < 1 or Opcion > 10 ):
        print("============ Esta no es una opción ============")
        print("Ingrese su opción: ")
        Opcion = int(input())

    #==============================================================================================

    if(Opcion == 1):
        print("Ingresa el numero del vuelo que estas buscando: ")
        Nro = int(input())
        sw = 1
        while(Nro < 0 or Nro > 999):
            print("Creeme no tenemos tantos vuelos, ni tan pocos...")
            print("Ingresa el numero del vuelo que estas buscando: ")
            Nro = int(input())
        for node in Vuelos:
            if (str(Nro) == node.Nro):
                print("Información general:", node)
                print("Pasjaeros:", node.Lista_Pasajeros)
                print("Lista de espera:", node.Lista_espera)
                sw = 0
        if(sw == 1):
            print("                                                   ")
            print("======== Lo siento, ese vuelo no existe :c =========")
            print("                                                   ")

    #============================================================================================== 

    elif (Opcion == 2):
        print("Ingresa el numero del vuelo que deseas eliminar: ")
        Nro = int(input())
        sw = 1
        while(Nro < 0 or Nro > 999):
            print("Creeme no tenemos tantos vuelos, ni tan pocos...")
            print("Ingresa el numero del vuelo que deseas eliminar: ")
            Nro = int(input())
        for node in Vuelos:
            if (str(Nro) == node.Nro):
                print("======= Pasajeros eliminados =========")
                print(node.Lista_Pasajeros)
                for node1 in node.Lista_Pasajeros:
                    node.Lista_Pasajeros.delete_node(node1)
                print("======= Pasajeros en espera eliminados =========")
                print(node.Lista_espera)
                for node2 in node.Lista_espera:
                    node.Lista_espera.delete_node(node2)
                print("======= Vuelo eliminado ==========")
                print(node)
                Vuelos.delete_node(node)
                sw = 0
        if(sw == 1):
            print("                                                   ")
            print("======== Lo siento, ese vuelo no existe :c =========")
            print("                                                   ")

    #==============================================================================================

    elif (Opcion == 3):
        print("Ingresa el id del pasajero que estas buscando: ")
        Id = int(input())
        sw = 1
        while(Id < 0 or Id > 999):
            print("Los id son positivos y de maximo 3 digitos !!!")
            print("Ingresa el id del pasajero que estas buscando: ")
            Id = int(input())
        for node in Vuelos:
            for node1 in node.Lista_Pasajeros:
                if (Id == node1.id):
                    print("=============================")
                    print("Nombre:", node1.nombre_pasajero)
                    print("Id:", node1.id)
                    print("======= Vuelo del que tiene ticket ==========")
                    print(node)
                    sw = 0
            for node2 in node.Lista_espera:
                if (Id == node2.id):
                    sw = 2
        if(sw == 1):
            print("                                                                     ")
            print("======== Lo siento, esta persona no esta en registrada  :c =========")
            print("                                                                     ")
        if(sw == 2):
            print("                                                                     ")
            print("======== Lo siento, esta persona no posee ticket  :c =========")
            print("======== Puedes intentar buscarlo por el metodo (8)  =========")
            print("                                                                     ")

    #==============================================================================================

    elif (Opcion == 4):
        print("Ingresa el id del pasajero que deseas eliminar: ")
        Id = int(input())
        sw = 1
        while(Id < 0 or Id > 999):
            print("Los id son positivos y de maximo 3 dígitos !!!")
            print("Ingresa el id del pasajero que deseas eliminar: ")
            Id = int(input())
        for node in Vuelos:
            for node1 in node.Lista_Pasajeros:
                if (Id == node1.id):
                    print("======= Usuario eliminado ==========")
                    print("Nombre:", node1.nombre_pasajero)
                    print("Id:", node1.id)
                    print("=============================")
                    node.Lista_Pasajeros.delete_node(node1)
                    node.Lista_Pasajeros.sorted_Insert([node.Lista_espera.head_pasajero.nombre_pasajero, node.Lista_espera.head_pasajero.id])
                    node.Lista_espera.delete_node(node.Lista_espera.head_pasajero)
                    sw = 0
            for node2 in node.Lista_espera:
                if (Id == node2.id):
                    sw = 2
        if(sw == 1):
            print("                                                                     ")
            print("======== Lo siento, esta persona no esta en registrada :c =========")
            print("                                                                     ")
        if(sw == 2):
            print("                                                                     ")
            print("======== Lo siento, esta persona no posee ticket  :c =========")
            print("======== Puedes intentar eliminarlo por el metodo (9)  =========")
            print("                                                                     ")

    #==============================================================================================

    elif (Opcion == 5):
        print("Ingresa el número del nuevo vuelo: ")
        Nro = int(input())
        sw = 1
        while(Nro < int(Vuelos.tail.Nro) or Nro > 999):
            if(Nro < int(Vuelos.tail.Nro)):
                print("El numero del vuelo debe ser mayor al ultimo agendado")
            else:
                print("Creeme no tenemos tantos vuelos, ni tan pocos...")
            print("Ingresa el número del nuevo vuelo: ")
            Nro = int(input())
        print("Ingrese desde donde sale: ")
        Salida = str(input())
        print("Ingrese a donde llega: ")
        LLegada = str(input())
        Vuelos.add_node(str(Nro), Salida, LLegada)
    
    #==============================================================================================

    elif (Opcion == 6):
        print("Ingresa el número del vuelo que deseas ingresar: ")
        Nro = int(input())
        sw = 1
        while(Nro < 0 or Nro > 999):
            print("Creeme no tenemos tantos vuelos, ni tan pocos...")
            print("Ingresa el numero del vuelo que deseas ingresar: ")
            Nro = int(input())
        for node in Vuelos:
            if (str(Nro) == node.Nro and len(node.Lista_Pasajeros) >= Max_capacidad):
                sw = 2
            elif(str(Nro) == node.Nro and len(node.Lista_Pasajeros) < Max_capacidad):
                print("Ingresa el nombre del nuevo pasajero: ")
                nombre = str(input())
                print("Ingresa el Id del nuevo pasajero: ")
                Id = str(input())
                node.Lista_Pasajeros.sorted_Insert([nombre,Id])
                sw = 0
                print("=== Informacion actualizada ===")
                print("Información general:", node)
                print("Pasjaeros:", node.Lista_Pasajeros)
                print("Lista de espera:", node.Lista_espera)
                    
        if(sw == 2):
            print("                                                                     ")
            print("======== Lo siento, este vuelo esta lleno  :c =========")
            print("======== Usa el método (7) en este caso :D  =========")
            print("                                                                     ")
        if(sw == 1):
            print("                                                                     ")
            print("======== Lo siento, este vuelo no esta registrado :c =========")
            print("                                                                     ")
    
    #==============================================================================================
    
    elif (Opcion == 7):
        print("Ingresa el número del vuelo que deseas estar en espera: ")
        Nro = int(input())
        sw = 1
        while(Nro < 0 or Nro > 999):
            print("Creeme no tenemos tantos vuelos, ni tan pocos...")
            print("Ingresa el numero del vuelo que deseas ingresar: ")
            Nro = int(input())
        for node in Vuelos:
            if(str(Nro) == node.Nro and len(node.Lista_Pasajeros) < Max_capacidad):
                sw = 2
            elif(str(Nro) == node.Nro):
                print("Ingresa el nombre del nuevo pasajero: ")
                nombre = str(input())
                print("Ingresa el Id del nuevo pasajero: ")
                Id = str(input())
                node.Lista_espera.sorted_Insert([nombre,Id])
                sw = 0
                print("=== Información actualizada ===")
                print("Información general:", node)
                print("Pasajeros:", node.Lista_Pasajeros)
                print("Lista de espera:", node.Lista_espera)
           
        if(sw == 2):
            print("                                                                     ")
            print("======== Felicidades, aún hay cupo en el vuelo =========")
            print("======== Usa el método (6) en este caso :D  =========")
            print("                                                                     ")
        if(sw == 1):
            print("                                                                     ")
            print("======== Lo siento, este vuelo no esta registrado :c =========")
            print("                                                                     ")

    #==============================================================================================

    elif (Opcion == 8):
        print("Ingresa el id del pasajero que estas buscando: ")
        Id = int(input())
        sw = 1
        while(Id < 0 or Id > 999):
            print("Los id son positivos y de maximo 3 dígitos !!!")
            print("Ingresa el id del pasajero que estas buscando: ")
            Id = int(input())
        for node in Vuelos:
            for node1 in node.Lista_espera:
                if (Id == node1.id):
                    print("=============================")
                    print("Nombre:", node1.nombre_pasajero)
                    print("Id:", node1.id)
                    print("======= Vuelo al que esta esperando ==========")
                    print(node)
                    sw = 0
            for node2 in node.Lista_Pasajeros:
                if (Id == node2.id):
                    sw = 2
        if(sw == 1):
            print("                                                                     ")
            print("======== Lo siento, esta persona no esta en registrada  :c =========")
            print("                                                                     ")
        if(sw == 2):
            print("                                                                     ")
            print("======== Lo siento, ya compro el ticket  :c =========")
            print("======== Puedes intentar buscarlo por el metodo (3)  =========")
            print("                                                                     ")

    #==============================================================================================
            
    elif (Opcion == 9):
        print("Ingresa el id del pasajero que deseas eliminar: ")
        Id = int(input())
        sw = 1
        while(Id < 0 or Id > 999):
            print("Los id son positivos y de maximo 3 dígitos !!!")
            print("Ingresa el id del pasajero que deseas eliminar: ")
            Id = int(input())
        for node in Vuelos:
            for node1 in node.Lista_espera:
                if (Id == node1.id):
                    print("======= Usuario eliminado ==========")
                    print("Nombre:", node1.nombre_pasajero)
                    print("Id:", node1.id)
                    print("=============================")
                    node.Lista_Pasajeros.delete_node(node1)
                    sw = 0
            for node2 in node.Lista_Pasajeros:
                if (Id == node2.id):
                    sw = 2
        if(sw == 1):
            print("                                                                     ")
            print("======== Lo siento, esta persona no posee ticket  :c =========")
            print("                                                                     ")
        if(sw == 2):
            print("                                                                     ")
            print("======== Lo siento, esta persona no posee ticket  :c =========")
            print("======== Puedes intentar eliminarlo por el método (4)  =========")
            print("                                                                     ")

    #==============================================================================================

    print("                                               ")
    print("|=============================================|")
    print("|             Vuelos inteligentes             |")
    print("|=============================================|")
    print("                                               ")





