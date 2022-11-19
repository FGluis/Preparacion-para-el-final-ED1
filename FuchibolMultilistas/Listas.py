class Equipos:
    def __init__(self, Nombre: str = "Sin establecer", Codigo: str = "NA", next_node=None, prev_node=None):
        self.codigo = Codigo
        self.nombre = Nombre
        self.next = next_node
        self.prev = prev_node
        self.lista_jugadores = Lista_jugadores()
    def __str__(self):
        return "║ Nombre: "+ self.nombre +", Codigo: "+ self.codigo + " ║"

class Lista_Equipos:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return ' <--> '.join([str(node) for node in self])
    
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
        return [[node.nombre, node.codigo] for node in self]
    
    def add_node(self, nombre, codigo):
        if self.head is None:
            self.tail = self.head = Equipos(nombre, codigo)
        else:
            self.tail.next = Equipos(nombre, codigo)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value[0],value[1])
            
    def delete_node(self, nodes:Equipos):
        for node in self:
            if nodes == node:
                if(len(self) == 1):
                    self.head = None
                    self.tail = None
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

    def sorted_Insert(self, value): #Fuentes: https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
        new_node = Equipos(value[0],value[1])
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
 
        elif int(self.head.codigo) >= int(new_node.codigo):
            new_node.next = self.head
            new_node.prev_ = None
            self.head.prev = new_node
            self.head = new_node
 
        else :
            current = self.head
            while(current.next is not None and int(current.next.codigo) < int(new_node.codigo)):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            
class Jugador:
    def __init__(self, nombre_jugador: str = "NA", numero_jugador: str = "NA", next_jugador=None, prev_jugador=None):
        self.nombre_jugador = nombre_jugador
        self.numero_jugador = numero_jugador
        self.next_jugador = next_jugador
        self.prev_jugador = prev_jugador
    def __str__(self):
        return "║ Nombre: "+ self.nombre_jugador +", Numero: "+ self.numero_jugador + " ║"
    
class Lista_jugadores:
    def __init__(self, values=None):
        self.head_jugador = None
        self.tail_jugador = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' --> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head_jugador
        while node:
            count += 1
            node = node.next_jugador
        return count
    
    def __iter__(self):
        current = self.head_jugador
        yield current
        current = current.next_jugador
        while current:
            yield current
            current = current.next_jugador
            
    @property
    def values(self):
        return [[node.nombre_jugador, node.numero_jugador] for node in self]

    def add_node(self, value: list):
        if self.head_jugador is None:
            self.tail_jugador = self.head_jugador = Jugador(
                nombre_jugador=value[0], numero_jugador=value[1])
        else:
            self.tail_jugador.next_jugador = Jugador(
                nombre_jugador=value[0], numero_jugador=value[1])
            self.tail_jugador.next_jugador.prev_jugador = self.tail_jugador
            self.tail_jugador = self.tail_jugador.next_jugador
        return self.tail_jugador


    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

    def delete_node(self, nodes:Jugador):
        for node in self:
            if nodes == node:
                if(len(self) == 0):
                    print("")
                elif(len(self) == 1):
                    self.head_jugador = None
                    self.tail_jugador = None
                elif (node == self.head_jugador): 
                    node.next_jugador.prev_jugador = None
                    self.head_jugador = node.next_jugador
                    node.next_jugador = None
                elif (node == self.tail_jugador):
                    node.prev_jugador.next_jugador = None
                    self.tail_jugador = node.prev_jugador
                    node.prev_jugador = None
                else:
                    node.prev_jugador.next_jugador = node.next_jugador
                    node.next_jugador.prev_jugador = node.prev_jugador
                    node.next_jugador = None
                    node.prev_jugador = None

    
    def sorted_Insert(self, value): #Fuentes: https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
        new_node = Jugador(value[0],value[1])
        if self.head_jugador is None:
            new_node.next_jugador = self.head_jugador
            self.head_jugador = new_node
            self.tail_jugador = new_node
 
        elif int(self.head_jugador.numero_jugador) >= int(new_node.numero_jugador):
            new_node.next_jugador = self.head_jugador
            new_node.prev_jugador = None
            self.head_jugador.prev_jugador = new_node
            self.head_jugador = new_node
 
        else :
            current = self.head_jugador
            while(current.next_jugador is not None and int(current.next_jugador.numero_jugador) < int(new_node.numero_jugador)):
                current = current.next_jugador
            new_node.next_jugador = current.next_jugador
            new_node.prev_jugador = current
            current.next_jugador = new_node