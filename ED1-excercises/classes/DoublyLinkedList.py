from Node import Node

class LinkedList:
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
        return [node.value for node in self]
    
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
            
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head


class DoublyLinkedList(LinkedList):
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self
    
    def removeNode(self, value):
        if self.head == None:
            return

        for node in self:
            if node.value is value:
                if node == self.head:
                    self.head = node.next
                    self.head.prev = None
                    node.next = None
                if node == self.tail:
                    self.tail = node.prev
                    self.tail.next = None
                    node = None
                else:
                    temp = node.prev
                    temp.next = node.next
                    temp2 = node.next
                    temp2.prev = temp

    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head