import numpy as np
class Node:
    def __init__(self, value: list, next_node=None, prev_node=None):
        self.valor = value[0]
        self.i = value[1]
        self.j = value[2]
        self.n = value[3]
        self.m = value[4]
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return "║ X: "+ str(self.valor) +", (i,j): ("+ str(self.i) + ","+ str(self.j) +") ║"


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' --> '.join([str(node) for node in self])
    
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
        return [[node.valor,node.i,node.j ] for node in self]
    
    def add_node(self, value:list):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return self.tail
    
    def sorted_Insert(self, value:list): #Fuentes: https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
        new_node = Node(value)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
 
        elif int(self.head.i) >= int(new_node.i) and int(self.head.j) >= int(new_node.j):
            new_node.next = self.head
            new_node.prev_ = None
            self.head.prev = new_node
            self.head = new_node
 
        else :
            current = self.head
            while(current.next is not None and int(current.next.i) < int(new_node.i) and int(current.next.j) < int(new_node.j) ):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
    
    def Mat_to_list(self, Mat):
        value = []
        for i in range(Mat.shape[0]):
            for j in range(Mat.shape[1]):
                if(Mat[i][j] != 0):
                    value.append([Mat[i][j], i, j, Mat.shape[0],Mat.shape[1]]) 
        self.add_multiple_nodes(value)

    def List_to_Mat(self):
        New_Mat = np.zeros([self.head.n,self.head.m])
        for node in self:
            New_Mat[node.i][node.j] = node.valor
        return New_Mat


def additionLinkedList(Mat1: LinkedList(), Mat2: LinkedList()) -> LinkedList():
    result_matrix = LinkedList()
    for node1 in Mat1:
        sw = 0
        for node2 in Mat2:
            sw2 = 0
            if(node1.i == node2.i and node1.j == node2.j):
                sw = 1
                Value = [node1.valor + node2.valor,node1.i,node1.j, node1.n, node1.m]
                result_matrix.add_node(Value)
        if(sw != 1):
            Value = [node1.valor,node1.i,node1.j, node1.n, node1.m]
            result_matrix.add_node(Value)
    for node2 in Mat2:
        sw = 0
        for node1 in Mat1:
            if(node1.i == node2.i and node1.j == node2.j):
                sw = 1
        if(sw != 1):
            Value = [node2.valor,node2.i,node2.j, node1.n, node1.m]
            result_matrix.add_node(Value)
    return result_matrix

def subtractLinkedList(Mat1: LinkedList(), Mat2: LinkedList()) -> LinkedList():
    result_matrix = LinkedList()
    for node1 in Mat1:
        sw = 0
        for node2 in Mat2:
            sw2 = 0
            if(node1.i == node2.i and node1.j == node2.j):
                sw = 1
                Value = [node1.valor - node2.valor,node1.i,node1.j, node1.n, node1.m]
                result_matrix.add_node(Value)
        if(sw != 1):
            Value = [node1.valor,node1.i,node1.j, node1.n, node1.m]
            result_matrix.add_node(Value)
    for node2 in Mat2:
        sw = 0
        for node1 in Mat1:
            if(node1.i == node2.i and node1.j == node2.j):
                sw = 1
        if(sw != 1):
            Value = [node2.valor,node2.i,node2.j, node1.n, node1.m]
            result_matrix.add_node(Value)
    return result_matrix

def multiply(Mat1: LinkedList(), Mat2: LinkedList()) -> LinkedList():
    #falta
        

            

    
