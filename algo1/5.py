class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.length = 0

    def enqueue(self, item):
        self.stack1.append(item)
        self.length += 1

    def dequeue(self):
        if self.empty():
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.length -= 1
        return self.stack2.pop()

    def empty(self):
        return self.size() == 0

    def size(self):
        return self.length
