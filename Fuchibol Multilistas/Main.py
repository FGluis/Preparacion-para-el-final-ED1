from Listas import Lista_Equipos, Lista_jugadores
#=======================================================================================
equipos = [["Junior", "1"],["Millonarios", "2" ],["Medellin", "3"],["Union Magdalena", "4"],["Santa Fe", "5"]]
Jugadores1 = [["Luis", "1"], ["Eliana", "2"], ["Jesus", "3"],["Yitzhack", "10"]]
Jugadores2 = [["Naim", "1"], ["Jose", "9"], ["Steven", "10"],["Mathilda", "13"], ["Moisex", "69"]]
Jugadores3 = [["Racedo", "1"], ["Bernardo", "11"]]
Jugadores4 = [["Pedro", "1"], ["Ismael", "7"], ["Elder", "9"]]
Jugadores5 = [["Vega", "1"], ["Anselmo", "2"], ["Jairo", "3"],["De oro", "10"]]

Equipos = Lista_Equipos()
Equipos.add_multiple_nodes(equipos)
Equipos.head.lista_jugadores.add_multiple_nodes(Jugadores1)
Equipos.head.next.lista_jugadores.add_multiple_nodes(Jugadores2)
Equipos.head.next.next.lista_jugadores.add_multiple_nodes(Jugadores3)
Equipos.head.next.next.next.lista_jugadores.add_multiple_nodes(Jugadores4)
Equipos.head.next.next.next.next.lista_jugadores.add_multiple_nodes(Jugadores5)
#===========================================================================================

Opcion = 0
while(Opcion != 7):
    print("╔═══════════════════════════════╗")
    print("║            DIMAYOR            ║")
    print("╚═══════════════════════════════╝")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║ Ingrese el numero correspondinte a la acción que deseas hacer: ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("╔═════════════════════════╗")
    print("║ (1) Buscar un Equipo    ║")
    print("║ (2) Eliminar un Equipo  ║")
    print("║ (3) Agregar un equipo   ║")
    print("║ (4) Buscar un Jugador   ║")
    print("║ (5) Eliminar un jugador ║")
    print("║ (6) Agregar un jugador  ║")
    print("║ (7) Salir               ║")
    print("╚═════════════════════════╝")
    Opcion = int(input())
    while(Opcion < 1 or Opcion > 7 ):
        print("╔═══════╗")
        print("║ ERROR ║")
        print("╚═══════╝")
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║                   Ese numero es invalido!!!                    ║")
        print("║ Ingrese el numero correspondinte a la acción que deseas hacer: ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print("╔═════════════════════════╗")
        print("║ (1) Buscar un Equipo    ║")
        print("║ (2) Eliminar un Equipo  ║")
        print("║ (3) Agregar un equipo   ║")
        print("║ (4) Buscar un Jugador   ║")
        print("║ (5) Eliminar un jugador ║")
        print("║ (6) Agregar un jugador  ║")
        print("║ (7) Salir               ║")
        print("╚═════════════════════════╝")
        Opcion = int(input())
    
    #══════════════════════════════════════════════════════════════════════════════
    if(Opcion == 1):
        print("╔══════════════════════════════════════════════════╗")
        print("║ Ingresa el codigo del equipo que estas buscando: ║")
        print("╚══════════════════════════════════════════════════╝")
        codigo = str(input())
        sw = 0
        while(int(codigo) < 0 or int(codigo) > 999):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔══════════════════════════════════════════════════╗")
            print("║        Ese numero de codigo es invalido!!!       ║")
            print("║ Ingresa el codigo del equipo que estas buscando: ║")
            print("╚══════════════════════════════════════════════════╝")
            codigo = str(input())
        for node in Equipos:
            if(node.codigo == codigo):
                print("╔═════════╗")
                print("║ EQUIPO: ║")
                print("╚═════════╝")
                print(node)
                print("╔════════════╗")
                print("║ JUGADORES: ║")
                print("╚════════════╝")
                if(len(node.lista_jugadores) != 0):
                    print(node.lista_jugadores)
                sw = 1
        if(sw == 0):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔═════════════════════════════════════════╗")
            print("║ Ese numero de codigo No esta registrado ║")
            print("╚═════════════════════════════════════════╝")
    #══════════════════════════════════════════════════════════════════════════════
    elif(Opcion == 2):
        print("╔════════════════════════════════════════════════════╗")
        print("║ Ingresa el codigo del equipo que quieres eliminar: ║")
        print("╚════════════════════════════════════════════════════╝")
        codigo = str(input())
        sw = 0
        while(int(codigo) < 0 or int(codigo) > 999):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔════════════════════════════════════════════════════╗")
            print("║         Ese numero de codigo es invalido!!!        ║")
            print("║ Ingresa el codigo del equipo que quieres eliminar: ║")
            print("╚════════════════════════════════════════════════════╝")
            codigo = str(input())
        for node in Equipos:
            if(node.codigo == codigo):
                print("╔═══════════════════╗")
                print("║ EQUIPO ELIMINADO: ║")
                print("╚═══════════════════╝")
                print(node)
                print("╔═══════════════════════╗")
                print("║ JUGADORES ELIMINADOS: ║")
                print("╚═══════════════════════╝")
                if(len(node.lista_jugadores) != 0):
                    print(node.lista_jugadores)
                    for node1 in node.lista_jugadores:
                        node.lista_jugadores.delete_node(node1)
                    Equipos.delete_node(node)
                sw = 1
        if(sw == 0):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔═════════════════════════════════════════╗")
            print("║ Ese numero de codigo No esta registrado ║")
            print("╚═════════════════════════════════════════╝")        
    #══════════════════════════════════════════════════════════════════════════════
    elif(Opcion == 3):
        print("╔═════════════════════════════════════════════════════════╗")
        print("║ Ingresa el codigo del nuevo equipo que quieres agregar: ║")
        print("╚═════════════════════════════════════════════════════════╝")
        codigo = str(input())
        sw = 0
        sw2 = False
        for node in Equipos:
            if(node.codigo == codigo):
                sw2 = True
        while(int(codigo) < 0 or int(codigo) > 999 or sw2):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔══════════════════════════════════════════════════╗")
            print("║        Ese numero de codigo es invalido!!!       ║")
            print("║ Ingresa el codigo del equipo que estas buscando: ║")
            print("╚══════════════════════════════════════════════════╝")
            codigo = str(input()) 
            sw2 = False
            for node in Equipos:
                if(node.codigo == codigo):
                    sw2 = True
        
        print("╔════════════════════╗")
        print("║ NOMBRE DEL EQUIPO: ║")
        print("╚════════════════════╝")
        nombre = str(input())
        Equipos.sorted_Insert([nombre, codigo])
        print("╔══════════════════════════════════╗")
        print("║ EQUIPO CREADO SATISFACTORIAMENTE ║")
        print("╚══════════════════════════════════╝")
    #══════════════════════════════════════════════════════════════════════════════
    elif(Opcion == 4):
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║ Ingresa el codigo del equipo del jugador que estas buscando: ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        codigo = str(input())
        sw = 0
        while(int(codigo) < 0 or int(codigo) > 999):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔══════════════════════════════════════════════════════════════╗")
            print("║              Ese numero de codigo es invalido!!!             ║")
            print("║ Ingresa el codigo del equipo del jugador que estas buscando: ║")
            print("╚══════════════════════════════════════════════════════════════╝")
            codigo = str(input())
        for node in Equipos:
            if(node.codigo == codigo):
                print("╔═══════════════════════════════════════════════════╗")
                print("║ Ingresa el número del jugador que estas buscando: ║")
                print("╚═══════════════════════════════════════════════════╝")
                numero = str(input())
                sw2 = 0
                while(int(numero) < 0 or int(numero) > 999):
                    print("╔═══════╗")
                    print("║ ERROR ║")
                    print("╚═══════╝")
                    print("╔═══════════════════════════════════════════════════╗")
                    print("║             Ese número es invalido!!!             ║")
                    print("║ Ingresa el número del jugador que estas buscando: ║")
                    print("╚═══════════════════════════════════════════════════╝")
                    numero = str(input())
                for node1 in node.lista_jugadores:
                    if(node1.numero_jugador == numero):
                        print("╔═════════╗")
                        print("║ EQUIPO: ║")
                        print("╚═════════╝")
                        print(node)
                        print("╔══════════╗")
                        print("║ JUGADOR: ║")
                        print("╚══════════╝")
                        print(node1)
                        sw2 = 1
                if(sw2 == 0):
                    print("╔═══════╗")
                    print("║ ERROR ║")
                    print("╚═══════╝")
                    print("╔══════════════════════════════════════════╗")
                    print("║ Ese numero de jugador No esta registrado ║")
                    print("╚══════════════════════════════════════════╝")
                sw = 1
        if(sw == 0):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔═════════════════════════════════════════╗")
            print("║ Ese numero de codigo No esta registrado ║")
            print("╚═════════════════════════════════════════╝")
    #══════════════════════════════════════════════════════════════════════════════
    elif(Opcion == 5):
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║ Ingresa el codigo del equipo del jugador que desea eliminar: ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        codigo = str(input())
        sw = 0
        while(int(codigo) < 0 or int(codigo) > 999):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔══════════════════════════════════════════════════════════════╗")
            print("║              Ese numero de codigo es invalido!!!             ║")
            print("║ Ingresa el codigo del equipo del jugador que desea eliminar: ║")
            print("╚══════════════════════════════════════════════════════════════╝")
            codigo = str(input())
        for node in Equipos:
            if(node.codigo == codigo):
                print("╔═══════════════════════════════════════════════════╗")
                print("║ Ingresa el número del jugador que desea eliminar: ║")
                print("╚═══════════════════════════════════════════════════╝")
                numero = str(input())
                sw2 = 0
                while(int(numero) < 0 or int(numero) > 999):
                    print("╔═══════╗")
                    print("║ ERROR ║")
                    print("╚═══════╝")
                    print("╔═══════════════════════════════════════════════════╗")
                    print("║             Ese número es invalido!!!             ║")
                    print("║ Ingresa el número del jugador que desea eliminar: ║")
                    print("╚═══════════════════════════════════════════════════╝")
                    numero = str(input())
                for node1 in node.lista_jugadores:
                    if(node1.numero_jugador == numero):
                        print("╔════════════════════╗")
                        print("║ JUGADOR ELIMINADO: ║")
                        print("╚════════════════════╝")
                        print(node1)
                        sw2 = 1
                        node.lista_jugadores.delete_node(node1)
                if(sw2 == 0):
                    print("╔═══════╗")
                    print("║ ERROR ║")
                    print("╚═══════╝")
                    print("╔══════════════════════════════════════════╗")
                    print("║ Ese numero de jugador No esta registrado ║")
                    print("╚══════════════════════════════════════════╝")
                sw = 1
        if(sw == 0):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔═════════════════════════════════════════╗")
            print("║ Ese numero de codigo No esta registrado ║")
            print("╚═════════════════════════════════════════╝")
    #══════════════════════════════════════════════════════════════════════════════
    elif(Opcion == 6):
        print("╔═════════════════════════════════════════════════╗")
        print("║ Ingresa el codigo del equipo del nuevo jugador: ║")
        print("╚═════════════════════════════════════════════════╝")
        codigo = str(input())
        sw = 0
        while(int(codigo) < 0 or int(codigo) > 999):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔═════════════════════════════════════════════════╗")
            print("║       Ese numero de codigo es invalido!!!       ║")
            print("║ Ingresa el codigo del equipo del nuevo jugador: ║")
            print("╚═════════════════════════════════════════════════╝")
            codigo = str(input())
        for node in Equipos:
            if(node.codigo == codigo):
                print("╔══════════════════════════════════════╗")
                print("║ Ingresa el número del nuevo jugador: ║")
                print("╚══════════════════════════════════════╝")
                numero = str(input())
                sw2 = 0
                while(int(numero) < 0 or int(numero) > 999):
                    print("╔═══════╗")
                    print("║ ERROR ║")
                    print("╚═══════╝")
                    print("╔══════════════════════════════════════╗")
                    print("║      Ese número es invalido!!!       ║")
                    print("║ Ingresa el número del nuevo jugador: ║")
                    print("╚══════════════════════════════════════╝")
                    numero = str(input())
                if(len(node.lista_jugadores) != 0):
                    for node1 in node.lista_jugadores:
                        if(node1.numero_jugador == numero):
                            print("╔═══════╗")
                            print("║ ERROR ║")
                            print("╚═══════╝")
                            print("╔══════════════════════════════════════════╗")
                            print("║ Ese numero de jugador ya esta registrado ║")
                            print("╚══════════════════════════════════════════╝")
                            sw2 = 1
                if(sw2 == 0):
                    print("╔═════════════════════╗")
                    print("║ NOMBRE DEL JUGADOR: ║")
                    print("╚═════════════════════╝")
                    nombre = str(input())
                    node.lista_jugadores.sorted_Insert([nombre, numero])
                    print("╔════════════════════════════════════╗")
                    print("║ JUGADOR AÑADIDO SATISFACTORIAMENTE ║")
                    print("╚════════════════════════════════════╝")
                sw = 1
        if(sw == 0):
            print("╔═══════╗")
            print("║ ERROR ║")
            print("╚═══════╝")
            print("╔═════════════════════════════════════════╗")
            print("║ Ese numero de codigo No esta registrado ║")
            print("╚═════════════════════════════════════════╝")
    #══════════════════════════════════════════════════════════════════════════════

    print("╔════════════════════════════════════════════════════════════════╗")
    print("║ Ingrese el numero correspondinte a la acción que deseas hacer: ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("╔════════════╗")
    print("║ (1) Seguir ║")
    print("║ (2) Salir  ║")
    print("╚════════════╝")
    aux = int(input())
    if(aux == 1):
        Opcion = 0
    else:
        Opcion = 7
