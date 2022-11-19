class Vuelo:
    #Por simplicidad la capacidad maxima de pasajeros sera 3, puedes cambiarla si deseas 
    Max_capacidad = 3   #Recuerda cambiar esto en la clase Main.
    def __init__(self, Nro: str = "Sin establecer", Salida: str = "NA", LLegada: str = "NA", capacidad:int = Max_capacidad, next_node=None, prev_node=None):
        self.Nro = Nro
        self.Salida = Salida
        self.LLegada = LLegada
        self.capacidad_vuelo = capacidad
        self.next = next_node
        self.prev = prev_node
        self.Lista_Pasajeros = Lista_Pasajeros()
        self.Lista_espera = Lista_Pasajeros()
    def __str__(self):
        return "|| Nro vuelo: "+ self.Nro +", Desde: "+ self.Salida + " a " + self.LLegada + " ||"

class Lista_Vuelos:
    
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            
    @property
    def values(self):
        return [[node.Nro, node.Salida, node.LLegada] for node in self]
    
    def add_node(self, Nro, Salida, LLegada):
        if self.head is None:
            self.tail = self.head = Vuelo(Nro, Salida, LLegada)
        else:
            self.tail.next = Vuelo(Nro, Salida, LLegada)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value[0],value[1],value[2] )
            
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Vuelo(value)
        else:
            self.head = Vuelo(value, self.head)
        return self.head

    def delete_node(self, nodes:Vuelo):
        for node in self:
            if nodes == node:
                if(len(self) == 1):
                    self.head_pasajero = None
                    self.tail_pasajero = None
                elif (node == self.tail):
                    node.prev.next = None
                    self.tail = node.prev
                    node.prev = None
                elif (node == self.head): 
                    node.next.prev = None
                    self.head = node.next
                    node.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node.next = None
                    node.prev = None


class Pasajero:
    def __init__(self, nombre_pasajero: str = "NA", id: str = "NA", next_pasajero=None, prev_pasajero=None):

        self.nombre_pasajero = nombre_pasajero
        self.id = id
        self.next_pasajero = next_pasajero
        self.prev_pasajero = prev_pasajero

    def __str__(self):
        return "|| nombre: "+ self.nombre_pasajero + " Id: " + str(self.id) + " ||"
    
class Lista_Pasajeros:
    def __init__(self, values=None):
        self.head_pasajero = None
        self.tail_pasajero = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head_pasajero
        while node:
            count += 1
            node = node.next_pasajero
        return count
    
    def __iter__(self):
        current = self.head_pasajero
        while current:
            yield current
            current = current.next_pasajero
            
    @property
    def values(self):
        return [node.nombre_pasajero for node in self]

    def add_node(self, value: list):
        if self.head_pasajero is None:
            self.tail_pasajero = self.head_pasajero = Pasajero(
                nombre_pasajero=value[0], id=value[1])
        else:
            self.tail_pasajero.next_pasajero = Pasajero(
                nombre_pasajero=value[0], id=value[1])
            self.tail_pasajero.next_pasajero.prev_pasajero = self.tail_pasajero
            self.tail_pasajero = self.tail_pasajero.next_pasajero
        return self.tail_pasajero

    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

    def delete_node(self, nodes:Pasajero):
        for node in self:
            if nodes == node:
                if(len(self) == 0):
                    print("")
                elif(len(self) == 1):
                    self.head_pasajero = None
                    self.tail_pasajero = None
                elif (node == self.head_pasajero): 
                    node.next_pasajero.prev_pasajero = None
                    self.head_pasajero = node.next_pasajero
                    node.next_pasajero = None
                elif (node == self.tail_pasajero):
                    node.prev_pasajero.next_pasajero = None
                    self.tail_pasajero = node.prev_pasajero
                    node.prev_pasajero = None
                else:
                    node.prev_pasajero.next_pasajero = node.next_pasajero
                    node.next_pasajero.prev_pasajero = node.prev_pasajero
                    node.next_pasajero = None
                    node.prev_pasajero = None
    
    def sorted_Insert(self, value): #Fuentes: https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
        new_node = Pasajero(value[0],value[1])
        if self.head_pasajero is None:
            new_node.next_pasajero = self.head_pasajero
            self.head_pasajero = new_node
            self.tail = new_node
 
        elif int(self.head_pasajero.id) >= int(new_node.id):
            new_node.next_pasajero = self.head_pasajero
            new_node.prev_pasajero = None
            self.head_pasajero = new_node
 
        else :
            current = self.head_pasajero
            while(current.next_pasajero is not None and int(current.next_pasajero.id) < int(new_node.id)):
                current = current.next_pasajero
            new_node.next_pasajero = current.next_pasajero
            new_node.prev_pasajero = current
            current.next_pasajero = new_node



