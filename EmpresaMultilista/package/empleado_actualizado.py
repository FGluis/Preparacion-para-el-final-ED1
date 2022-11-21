from __future__ import annotations

class Empleado:
    def __init__(self, id: int) -> None:
       self.id = id  
       self.nextEmp = None 
       self.link2 = ListaTareas()
       
    def __str__(self):
        return f'|| Id: {self.id} - Nro tareas: {len(self.link2)} ||'

class Tarea:
    def __init__(self, desc: str, dept: int) -> None:
        self.desc = desc 
        self.dept = dept
        self.nextTsk = None

    def __str__(self):
        return f'|| Desc: {self.desc} - Dept: {self.dept} ||'

class ListaTareas:
    def __init__(self) -> None:
        self.head = None 
        self.tail = None 

    def __iter__(self):
        current = self.head
        while current:
            yield current 
            current = current.nextTsk

    def __len__(self):
        tam = 0
        current = self.head 
        while current:
            tam += 1 
            current = current.nextTsk
        return tam

    def addTask(self, tarea: Tarea):
        node = tarea 
        if self.head == None:
            self.head = self.tail= node
            return 
        self.tail.nextTsk = node 
        self.tail = self.tail.nextTsk
    
    def eliminarTarea(self, tarea: Tarea):
        p = tarea 
        current = self.head 
        prev = None 

        while current != None and current != tarea:
            prev = current 
            current = current.nextTsk

        if tarea == self.head:
            self.head = current.nextTsk
        elif tarea == self.tail:
            self.tail = prev 
            prev.nextTsk = None 
        else:
            prev.nextTsk = current.nextTsk 
            current.nextTsk = None

    def __str__(self):
        return ' -> '.join([str(tarea) for tarea in self])

class ListaEmpleados:
    def __init__(self) -> None:
        self.HEAD
        self.headE = None 
        self.tailE = None 
    
    def __iter__(self):
        current = self.headE
        while current:
            yield current 
            current = current.nextEmp
    
    def addE(self,id: int, num_t: int):
        """
        Añade un empleado 
        """
        if self.headE == None:
            self.headE = self.tailE = Empleado(id)
        else:
            self.tailE.nextEmp = Empleado(id)
            self.tailE = self.tailE.nextEmp
        
    

        self.head = None 
        self.tail = None 
    
    def __iter__(self):
        current = self.head 
        while current:
            yield current 
            current = current.nextEmp

    def agregarEmpleado(self, empleado: Empleado):
        p = empleado 
        if self.head is None:
            p.nextEmp = self.head
            self.head = self.tail = p
            self.tail.nextEmp = None
            return 

        elif self.head.id >= p.id:
            p.nextEmp = self.head
            self.head = p
 
        else :
            current = self.head
            while(current.nextEmp is not None and
                 current.nextEmp.id < p.id):
                current = current.nextEmp
             
            p.nextEmp = current.nextEmp
            current.nextEmp = p

    def asignarTarea(self, empleado_buscado: Empleado, tarea: Tarea):
        for empleado in self:
            if empleado == empleado_buscado:
                empleado.link2.addTask(tarea)
    
    def sortEmpleados(self):
        current = self.head
        index = None
          
        if(self.head == None):
            return
        else:  
            while(current != None):  
                index = current.nextEmp  
                  
                while(index != None):  
                    if(current.id > index.id):
                        temp = current.id 
                        current.id= index.id 
                        index.id = temp
                    index = index.nextEmp  
                current = current.nextEmp

    def menor_num_t(self):
        current = self.head 
        menor = len(current.link2)

        while current:
            if len(current.link2) < menor:
                menor = len(current.link2)
            current = current.nextEmp 

        current = self.head 
        while current:
            if len(current.link2) == menor:
                return current
            current = current.nextEmp

    def __str__(self):
        return ' -> '.join([str(empleado) for empleado in self])


lista_tareas = ListaTareas()
lista_empleados = ListaEmpleados()

tarea_pendiente1 = Tarea(desc='Barrer', dept=13)
tarea_pendiente2 = Tarea(desc='Bañarse', dept=14)

tareas_pendientes = [tarea_pendiente1, tarea_pendiente2]

empleado1 = Empleado(73)
empleado2 = Empleado(37)
empleado3 = Empleado(12)

empleados = [empleado1, empleado2, empleado3]

for tarea in tareas_pendientes:
    lista_tareas.addTask(tarea)

for empleado in empleados:
    lista_empleados.agregarEmpleado(empleado)


# lista_empleados.sortEmpleados()
lista_empleados.asignarTarea(empleado1, Tarea(desc='Estudiar', dept=10))
lista_empleados.asignarTarea(empleado1, Tarea(desc='Comer', dept=11))
lista_empleados.asignarTarea(empleado2, Tarea(desc='Trapear', dept=15))
lista_empleados.asignarTarea(empleado2, Tarea(desc='Lavar', dept=20))
lista_empleados.asignarTarea(empleado3, Tarea(desc='Programar', dept=21))

print('\n[+] Lista empleados [+]')
print(lista_empleados)

print('\n[+] Lista de tareas pendientes[+]')
print(lista_tareas)
empleado_menos_ocupado = lista_empleados.menor_num_t()
lista_empleados.asignarTarea(empleado_menos_ocupado, Tarea(desc='Barrer', dept=13))
lista_tareas.eliminarTarea(lista_tareas.head)
print('\n[+] Lista de tareas pendientes despues de asignar al empleado con menos tareas [+]')
print(lista_tareas)

print('\n[+] Lista empleados [+]')
print(lista_empleados)
