from linked_lists import Node, DoublyLinkedList

dlist = DoublyLinkedList()
dlist.tailval = Node(8)
n_2 = Node(5)
n_3 = Node(3)
n_4 = Node(2)
n_5 = Node(1)
n_6 = Node(1)

dlist.tailval.prevval = n_2
n_2.prevval = n_3
n_3.prevval = n_4
n_4.prevval = n_5
n_5.prevval = n_6

dlist.paint_reverse()