class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0

    def pop(self):
        tmp = self.peek()
        if tmp is not None:
            self.stack.pop()
        return tmp

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.empty():
            return None
        return self.stack[-1]
