class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        self.head = None


class stack:
    def __init__(self):
        self.List = LinkedList()

    def push(self, val):
        nod = Node(val)
        if self.list.head == None:
            self.list.head = nod
        else:
            current = nod
            current.next = self.list.head
            self.list.head = current

    def pop(self):
        self.list.head = self.list.head.next


a = 1 - 2 - 3 - 4 - 5

arr = [0, 0, 0, 1, 1, 0, 1]
n = arr.count(0)
