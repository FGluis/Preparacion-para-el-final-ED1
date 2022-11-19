from __future__ import annotations

class Empleado:
    def __init__(self, id: int, num_t: int) -> None:
        self.id = id
        self.num_t = num_t
        self.link1 = None
        self.link2 = ListaTareas()

    def __str__(self):
        return f'|| Id: {self.id} - Número de tareas: {self.num_t} ||'

class Tarea:
    def __init__(self, desc: str, dept: str) -> None:
        self.desc = desc
        self.dept = dept
        self.nextTsk = None

    def __str__(self) -> None:
        return f'|| Descripcion: {self.desc} - Departamento de solicitud: {self.dept} ||'

class ListaEmpleados:
    def __init__(self) -> None:
        self.head = None 
        self.tail = None 

    def __iter__(self):
        current = self.head 
        while current:
            yield current 
            current = current.link1
    
    def addEmployee(self, empleado: Empeado) -> None:
        p = empleado

        if self.head == None:
            self.head = p 
            self.tail = p
            self.tail.link1 = None 
            return 
        self.tail.link1 = p
        self.tail = self.tail.link1

    @property
    def id_empleados(self):
        return [empleado.id for empleado in self]

    def menor_num_t(self):
        current = self.head 
        menor = current.num_t
        while current:
            if current.num_t < menor:
                menor = current.num_t
            current = current.link1 

        current = self.head 
        while current:
            if current.num_t == menor:
                return current
            current = current.link1

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

class ListaTareas:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 

    def __iter__(self):
        current = self.head 
        while current:
            yield current 
            current = current.nextTsk

    def addTask(self, task: Tarea) -> None:
        tarea = task

        if self.head == None:
            self.head = tarea 
            self.tail = tarea 
            self.tail.nextTsk = None 
            return 
        self.tail.nextTsk = tarea 
        self.tail = self.tail.nextTsk

    def __str__(self):
        return ' -> '.join([str(tarea) for tarea in self])


empleado1 = Empleado(id=10, num_t=2)
empleado2 = Empleado(id=12, num_t=3)

lista_empleados = ListaEmpleados()

lista_empleados.addEmployee(empleado1)
lista_empleados.addEmployee(empleado2)

tareas_empleado1 = [Tarea(desc='Pajearse', dept='xvideos'), Tarea(desc='Volar', dept='Avianca')]

tareas_empleado2 = [Tarea(desc='Comer', dept='Cocina'), Tarea(desc='Insultar a racedo', dept='MoisesInc'), 
                    Tarea(desc='Llorar', dept='Mi casa')]

tareas_pendientes = [Tarea(desc='Pujo', dept='Comelona'), Tarea(desc='Putines', dept='El ano de Moises')]

for k in range(empleado1.num_t):
    lista_empleados.head.link2.addTask(tareas_empleado1[k])

for k in range(empleado2.num_t):
    lista_empleados.head.link1.link2.addTask(tareas_empleado2[k])

for k in range(len(tareas_pendientes)):
    empleado_menos_ocupado = lista_empleados.menor_num_t()
    empleado_menos_ocupado.link2.addTask(tareas_pendientes[k])

print(lista_empleados)
print('====================')
print(lista_empleados.head.link2)
print('====================')
print(lista_empleados.head.link1.link2)