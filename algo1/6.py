class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self.size += 1

    def delete_first(self):
        if self.empty():
            return None
        tmp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return tmp

    def delete_last(self):
        if self.empty():
            return None
        tmp = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return tmp

    def len(self):
        return self.size

    def empty(self):
        return self.len() == 0

    def add_in_head(self, newNode):
        if self.head is None:
            self.add_in_tail(newNode)
            return
        self.head.prev = newNode
        tmp = self.head 
        if newNode is not None:
            self.head = newNode
            newNode.next = tmp
            newNode.prev = None
        self.size += 1

    def show(self):
        curr = self.head
        while curr:
            print(curr.value, end=' ')
            curr = curr.next
        print(f'\nsize = {self.len()}\n')

class Deque:
    def __init__(self):
        self.lst = LinkedList2()

    def addFront(self, item):
        self.lst.add_in_head(Node(item))

    def addTail(self, item):
        self.lst.add_in_tail(Node(item))

    def removeFront(self):
        return self.lst.delete_first()

    def removeTail(self):
        return self.lst.delete_last()

    def size(self):
        return self.lst.len()

    def show(self):
        self.lst.show()
