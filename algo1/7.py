class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.clean(asc) 

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        return 1

    def ascenging(self):
        return self.__ascending

    def insert_after(self, after_node, new_node):
        if self.empty():
            self.head = new_node
            self.tail = new_node
        elif after_node is None:
            tmp = self.head
            self.head = new_node
            self.head.next = tmp
            self.head.prev = None
            tmp.prev = self.head
        elif after_node.next is None:
            tmp = self.tail
            self.tail = new_node
            self.tail.next = None
            self.tail.prev = tmp
            tmp.next = self.tail
        else:
            tmp = after_node.next
            after_node.next = new_node
            new_node.prev = after_node
            new_node.next = tmp
            tmp.prev = new_node
        self.size += 1
            

    def add(self, value):
        new_node = Node(value)
        asc = self.ascenging()
        node = self.head
        # 1 2 3
        while node:
            cmp1 = self.compare(node.value, new_node.value)
            cmp2 = 0
            if node.next is not None:
                cmp2 = self.compare(new_node.value, node.next.value)
            cond1 = asc and cmp1 <= 0 and cmp2 <= 0
            cond2 = not asc and cmp1 >= 0 and cmp2 >= 0
            if cond1 or cond2:
                self.insert_after(node, new_node)
                return
            node = node.next
        self.insert_after(None, new_node)

    def find(self, val):
        node = self.head
        asc = self.ascenging()
        while asc and node and self.compare(node.value, val) < 0:
            node = node.next
        while not asc and node and self.compare(node.value, val) > 0:
            node = node.next
        if node and self.compare(node.value, val) == 0:
            return node
        return None

    def delete(self, val):
        node = self.find(val)
        if node is None:
            return
        deleted = False
        if node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            deleted = True
        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            deleted = True
        if not deleted:
            tmp1 = self.node.prev
            tmp2 = self.node.next
            tmp1.next = tmp2
            tmp2.prev = tmp1
        self.size -= 1

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.size = 0

    def len(self):
        return self.size

    def empty(self):
        return self.len() == 0

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def show(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.next
        print(f'\nsize {self.len()}\n')

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        return super(OrderedStringList, self).compare(v1.strip(), v2.strip())
