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
Equipos.head.lista_jugadores.delete_node(Equipos.head.lista_jugadores.head_jugador)
print("w")