from Node import Node

class DoublyCircularLinkedList:
    def __init__(self):    
        self.head = None    
        self.tail = None
        
    def addNode(self, value):      
        newNode = Node(value)

        if(self.head == None):    
            self.head = self.tail = newNode    
            self.head.prev = self.tail
            self.tail.next = self.head    
        else:    
            temp = self.tail
            self.tail.next = newNode
            # newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = self.head
            self.tail.prev = temp
            self.head.prev = self.tail

    def __iter__(self):
        current = self.head
        yield current
        current = current.next
        while current != self.tail.next:
            yield current
            current = current.next

    def all_nodes(self):
      return [node.value for node in self]

    def add_multiple_nodes(self, values):
      for value in values:
        self.addNode(value)
      
    @property
    def values(self):
        return [node.value for node in self]
    
    def deletebeg(self):
      if self.head==None:
          print("List is empty....")
      elif self.head.next==self.head:
        # print("deleted item ",self.head.value)
        self.head=None
      else: 
        position=self.head
        while position.next!=self.head:
          position=position.next
        print("deleted item ",self.head.value)
        self.head=self.head.next
        position.next=self.head
        self.head.prev=position

    def removeNode(self, node: Node):
      prev = node.prev
      next = node.next
      prev.next = next
      next.prev = prev

      if self.tail == node:
        self.tail = prev
      elif self.head == node:
        self.head = next
        

      # node.prev = None
      # node.next = None
    # def removeNode(self, dele):
         
    #     # Base Case
    #     if self.head is None or dele is None:
    #         return
         
    #     # If node to be deleted is head node
    #     if self.head == dele:
    #         self.head = dele.next
 
    #     # Change next only if node to be deleted is NOT
    #     # the last node
    #     if dele.next is not None:
    #         dele.next.prev = dele.prev
     
    #     # Change prev only if node to be deleted is NOT
    #     # the first node
    #     if dele.prev is not None:
    #         dele.prev.next = dele.next
    #     # Finally, free the memory occupied by dele
    #     # Call python garbage collector
    #     gc.collect()

    def removeNodeByValue(self, value):
      if self.head == None:
        return
      
      for node in self:
        if node.value is value:
          if node == self.head:
            self.head = node.next
            self.head.prev = self.tail
          if node == self.tail:
            self.tail = node.prev
            self.tail.next = self.head
          else:
            temp = node.prev
            temp.next = node.next
            temp2 = node.next
            temp2.prev = temp
                
    def display(self):    
        current = self.head
        if(self.head == None):    
            print("List is empty")
            return
        print("Nodes of doubly linked list: ")
        print(end=f'(TAIL) <-> ')
        while(current != self.tail):     
            print(current.value, end=' <-> ')    
            current = current.next
        
        print(self.tail.value, end=f' <-> (ROOT)')

    def __len__(self):
      temp = 1
      p = self.head

      if p == None:
        return 0
      
      p = p.next

      while p != self.head:
        temp += 1
        p = p.next
      return temp


    def buscarPorExtremos(self, value):
      current = self.head
      lastOne = self.tail

      if self.__len__() % 2 != 0:
        while lastOne != current:
          if current.value == value or lastOne.value == value:
            return 'He encontrado tu nodo !'
          current = current.next
          lastOne = lastOne.prev
        if current.value == value or lastOne.value == value:
          return 'Encontre tu nodo'
      else:
        while lastOne.prev != current:
          if current.value == value or lastOne.value == value:
            return 'He contrado tu nodo !'
          current = current.next
          lastOne = lastOne.prev
        if current.value == value or lastOne.value == value:
          return 'Encontre tu nodo'