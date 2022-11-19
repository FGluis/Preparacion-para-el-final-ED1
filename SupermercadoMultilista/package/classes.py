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
        elif client == self.tail:
            self.tail = prev 
            prev.link2 = None 
        else:
            prev.link2 = current.link2 
            current.link2 = None

    def attendClient(self, caja: Box, client: Client= None):
        current = self.head
        if caja.estado == False:
            caja.monto += current.monto_cliente
            self.deleteClient(client)
        else:
            for cliente in self:
                caja.monto += cliente.monto_cliente
            for cliente in self:
                self.deleteClient(cliente)

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


boxes = [Box(monto=10000, estado=True),
         Box(monto=5000, estado=False),
         Box(monto=2000, estado=True),
         Box(monto=1500, estado=False),
         Box(monto=0, estado=False)]

lista_cajas = ListaCajas()

for i in range(len(boxes)):
    lista_cajas.addBox(boxes[i])

lista_cajas.head.clientes.addClient(cliente1)
lista_cajas.head.link1.clientes.addClient(cliente2)
lista_cajas.head.link1.link1.clientes.addClient(cliente3)
lista_cajas.head.link1.link1.link1.clientes.addClient(cliente4)
lista_cajas.head.clientes.addClient(cliente5)
lista_cajas.head.link1.clientes.addClient(cliente6)
lista_cajas.head.link1.link1.clientes.addClient(cliente7)
lista_cajas.head.clientes.addClient(cliente8)
lista_cajas.head.link1.clientes.addClient(cliente9)


print(lista_cajas.head.clientes)
# lista_clientes.deleteClient(cliente1)
print('======================================')
print(lista_cajas.head.link1.clientes)
lista_cajas.head.link1.clientes.attendClient(lista_cajas.head.link1)
print('======================================')
print(lista_cajas.head.link1.clientes)

print('======================================')
print(lista_cajas)