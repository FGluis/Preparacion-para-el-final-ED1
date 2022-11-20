from Node import Node
from DoublyCircularLinkedList import DoublyCircularLinkedList

def compareSubList(l: DoublyCircularLinkedList, n1: Node, n2: Node) -> tuple:
    head2 = n2
    node1 = n1
    node2 = n2
    
    if node2.next == head2:
        if node1.value != node2.value:
            return (False, None)
        else:
            return (True, [node1])

    sublist = []

    while True:
        sublist.append(node1)
        if node1.value != node2.value:
            return (False, None)

        if node2 == l.tail:
            break
        node1 = node1.next
        node2 = node2.next

    return (True, sublist)

class Filter:
    def __init__(self) -> None:
        pass

    def find(self, l1: DoublyCircularLinkedList, l2: DoublyCircularLinkedList):
        ptr1 = l1.head
        ptr2 = l2.head
        if ptr1 == None:
            return (False, [])
        if ptr2 == None:
            return (False, [])
        
        node = ptr1
        while node != None:
            if node.value == ptr2.value:
                exists, subList = compareSubList(l2, node, ptr2)
                if exists:
                    return (True, subList)
            if node == l1.tail:
                break
            node = node.next
        
        return (False, [])

    def findAndRemove(self, l1: DoublyCircularLinkedList, l2: DoublyCircularLinkedList):
        ptr1 = l1.head
        ptr2 = l2.head
        if ptr1 == None:
            return
        if ptr2 == None:
            return
        
        node = ptr1
        
        while node != None:
            if node.value == ptr2.value:
                exists, subList = compareSubList(l2, node, ptr2)
                if exists:
                    for node in subList:
                        l1.removeNode(node)
                        print(node)
            if node == l1.tail:
                print(f'I\'m in the final {node}')
                break
            
            node = node.next