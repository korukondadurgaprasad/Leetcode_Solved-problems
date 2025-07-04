class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        if index < 0 or index >= self.length:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def addAtHead(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self.length += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            if self.length == 1:
                self.tail = None
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            to_delete = temp.next
            temp.next = to_delete.next
            if index == self.length - 1:
                self.tail = temp
            to_delete.next = None
        self.length -= 1
