class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        curr = self.head
        result = []
        while curr:
            if curr.value == val:
                result.append(curr)
            curr = curr.next
        return result

    def _delete_one(self, val):
        if self.head is None:
            return
        node = self.head
        prev = None
        while node and node.value != val:
            prev = node
            node = node.next
        if node == self.tail:
            self.tail = prev
            if self.tail:
                self.tail.next = None
        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        if prev and node:
            prev.next = node.next
            if node.next:
                node.next.prev = prev

    def _find_first_not_eq(self, node, val):
        while node and node.value == val:
            node = node.next
        return node
    
    def _delete_all(self, val):
        self.head = self._find_first_not_eq(self.head, val)
        self.head.prev = None

        first = None
        second = self.head
        while second:
            tmp = self._find_first_not_eq(second.next, val)
            second.next = tmp
            second.prev = first
            
            first = second
            second = second.next
        self.tail = first    

    def delete(self, val, all=False):
        if not all:
            self._delete_one(val)
            return
        self._delete_all(val)

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        curr = self.head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
            return
        if afterNode == self.tail:
            self.tail = newNode
        tmp = afterNode.next
        if tmp is not None:
            tmp.prev = newNode
        afterNode.next = newNode
        newNode.prev = afterNode
        newNode.next = tmp
       

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
