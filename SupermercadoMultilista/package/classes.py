from __future__ import annotations

class Box:
    def __init__(self, monto: int, estado: bool) -> None:
        self.monto = monto 
        self.estado = estado 
        self.link1 = None 
        self.clientes = ListaClientes()
        self.n_cliente = self.clientes.n_cliente
        
    def __str__(self) -> str:
        return f'|| Nro clientes: {self.n_cliente} - Monto: {self.monto} ||'

class Cliente:
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
    
    def addCliente(self, cliente: Cliente):
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

cliente1 = Cliente(id_cliente=10, monto_cliente=2000)
cliente2 = Cliente(id_cliente=12, monto_cliente=3000)

boxes = [Box(monto=10000, estado=False),
         Box(monto=5000, estado=False),
         Box(monto=2000, estado=False),
         Box(monto=1500, estado=False),
         Box(monto=0, estado=False)]

lista_clientes = ListaClientes()
lista_cajas = ListaCajas()

lista_clientes.addCliente(cliente1)
lista_clientes.addCliente(cliente2)

for i in range(len(boxes)):
    lista_cajas.addBox(boxes[i])

lista_cajas.head.clientes.addCliente(cliente1)


print(lista_clientes)
print('======================================')
print(lista_cajas)