from classes.DoublyLinkedList import DoublyLinkedList
from classes.DoublyCircularLinkedList import DoublyCircularLinkedList
from classes.Filter import Filter
#from Classess import LinkedList

def test_len_list():
    lista = DoublyLinkedList([1,2,3,4])
    assert len(lista) == 4

def test_add_node():
    lista = DoublyLinkedList()
    lista.add_node(1)
    assert lista.values == [1]

def test_add_multiple_nodes():
    lista = DoublyLinkedList()
    lista.add_multiple_nodes([1,2,3,4])
    assert lista.values == [1,2,3,4]

def test_remove_node():
    lista = DoublyLinkedList()
    lista.add_multiple_nodes([1,2,3,4])
    lista.removeNode(3)
    assert lista.values == [1, 2, 4]

# Right here, we going to test DoublyCircularLinkedList

def test_remove_node_circular():
    lista = DoublyCircularLinkedList()
    lista.add_multiple_nodes([1, 2, 3, 4])
    lista.removeNodeByValue(3)

    assert lista.values == [1, 2, 4]

def test_remove_sequence_circular():
    lista1 = DoublyCircularLinkedList()
    lista2 = DoublyCircularLinkedList()
    lista1.add_multiple_nodes([37, 37, 73, 73])
    lista2.add_multiple_nodes([73, 37])
    f = Filter()
    while f.find(l1=lista1, l2=lista2)[0]:
        f.findAndRemove(l1=lista1, l2=lista2)
    assert lista1.values == []