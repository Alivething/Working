class Node:
    def __init__(self, val):
        self.val = val
        self.ptr = None

class LinkedList:
    def __init__(self):
        self.head = None

List1 = LinkedList()
List1.head = Node("Item1")
List1.head.ptr = Node("Item2")