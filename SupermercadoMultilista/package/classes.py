from __future__ import annotations

class Box:
    def __init__(self, monto: int, estado: bool) -> None:
        self.monto = monto 
        self.estado = estado 
        self.link1 = None 
        self.clientes = ListaClientes()

    def __str__(self) -> str:
        return f'|| Nro clientes: {self.clientes.n_cliente} - Monto: {self.monto} ||'

class Client:
    def __init__(self, id_cliente: int, monto_cliente: int) -> None:
        self.id_cliente = id_cliente
        self.monto_cliente = monto_cliente
        self.link2 = None 

    def __str__(self) -> str:
        return f'|| Id cliente: {self.id_cliente} - Monto: {self.monto_cliente} ||'

class ListaClientes:
    def __init__(self) -> None:
        self.head = None 
        self.tail = None
        self.n_cliente = 0

    def __iter__(self):
        current = self.head 
        while current:
            yield current 
            current = current.link2 

    def __len__(self):
        current = self.head
        tam = 0
        while current:
            tam += 1
            current = current.link2
        return tam
    
    def addClient(self, cliente: Client):
        p = cliente
        if self.head == None:
            self.head = p 
            self.tail = p
            self.tail.link2 = None
            self.n_cliente += 1
            return 
        self.tail.link2 = p
        self.tail = self.tail.link2
        self.n_cliente += 1

    def deleteClient(self, client: Client):
        p = client 
        current = self.head 
        prev = None 

        while current != None and current != client:
            prev = current 
            current = current.link2

        if client == self.head:
            self.head = current.link2
        if client == self.tail:
            self.tail = prev 
            prev.link2 = None 
        else:
            prev.link2 = current.link2 
            current.link2 = None

    def __str__(self) -> str:
        return ' -> '.join([str(cliente) for cliente in self])

class ListaCajas:
    def __init__(self) -> None:
        self.head = None 
        self.tail = None

    def __iter__(self):
        current = self.head 
        while current:
            yield current
            current = current.link1 
    
    def addBox(self, box: Box) -> None:
        p = box 
        if self.head == None:
            self.head = p 
            self.tail = p
            self.tail.link1 = None 
            return 
        self.tail.link1 = p
        self.tail = self.tail.link1

    def __str__(self) -> None:
        return ' -> '.join([str(box) for box in self])

cliente1 = Client(id_cliente=10, monto_cliente=2000)
cliente2 = Client(id_cliente=12, monto_cliente=3000)
cliente3 = Client(id_cliente=9, monto_cliente=2000)
cliente4 = Client(id_cliente=8, monto_cliente=3000)
cliente5 = Client(id_cliente=77, monto_cliente=2000)
cliente6 = Client(id_cliente=1, monto_cliente=2000)
cliente7 = Client(id_cliente=4, monto_cliente=3000)
cliente8 = Client(id_cliente=5, monto_cliente=2000)
cliente9 = Client(id_cliente=44, monto_cliente=3000)


boxes = [Box(monto=10000, estado=False),
         Box(monto=5000, estado=False),
         Box(monto=2000, estado=False),
         Box(monto=1500, estado=False),
         Box(monto=0, estado=False)]

lista_clientes = ListaClientes()
lista_cajas = ListaCajas()

lista_clientes.addClient(cliente3)
lista_clientes.addClient(cliente4)
lista_clientes.addClient(cliente1)
lista_clientes.addClient(cliente2)

for i in range(len(boxes)):
    lista_cajas.addBox(boxes[i])

lista_cajas.head.clientes.addClient(cliente1)
lista_cajas.head.clientes.addClient(cliente2)
lista_cajas.head.link1.clientes.addClient(cliente2)

print('Before deleting')
print(lista_clientes)
# lista_clientes.deleteClient(cliente1)
print('======================================')
print('After deleting')
print(lista_clientes)
print('======================================')
print(lista_cajas)