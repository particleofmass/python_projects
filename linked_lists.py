class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def paint(self):
        paintlist = self.headval
        flag = 0
        while paintlist is not None:
            print(paintlist.dataval, ' ', end='')
            flag += 1
            paintlist = paintlist.nextval
        print('\n\nThe length of the linked list is: ', flag)


class DoublyLinkedList:
    def __init__(self):
        self.headval = None
        self.tailval = None

    def paint_reverse(self):
        paintlist = self.tailval
        flag = 0
        while paintlist is not None:
            print(paintlist.dataval, ' ', end='')
            flag += 1
            paintlist = paintlist.prevval
        print('\n\nThe length of the linked list is: ', flag)



