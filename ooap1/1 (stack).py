class ATDBoundedStack:

    PUSH_NIL = 0 # push() не вызывался
    PUSH_OK = 1  # последний push() успешно выполнился
    PUSH_ERR = 2 # переполнение стека

    POP_NIL = 0 # pop() не вызывался
    POP_OK = 1  # последний pop() успешно выполнился
    POP_ERR = 2 # стек пуст

    PEEK_NIL = 0 # peek() не вызывался
    PEEK_OK = 1  # последний peek() успешно выполнился
    PEEK_ERR = 2 # стек пуст


    # конструктор
    def __init__(self, capacity=32):
        # предусловие: capacity > 0
        pass

    # команды
    def push(self, value):
        # предусловие: размер стека меньше ограничения
        # постусловие: в стек добавлен элемент
        pass

    def pop(self):
        # предусловие: стек не пуст
        # постусловие: из стека удалён верхний элемент
        pass

    def clear(self):
        # постусловие: из стека удаляются все элементы
        pass

    # запросы
    def peek(self):
        # предусловие: стек не пуст
        pass

    def size(self):
        pass

    def max_size(self):
        pass

    # дополнительные запросы
    def get_push_status(self):
        pass

    def get_pop_status(self):
        pass

    def get_peek_status(self):
        pass


class BoundedStack:

    # statuses
    PUSH_NIL = 0
    PUSH_OK = 1
    PUSH_ERR = 2

    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2

    PEEK_NIL = 0
    PEEK_OK = 1
    PEEK_ERR = 2

    # ctor
    def __init__(self, capacity=32):
        assert(capacity > 0)
        self._capacity = capacity # private
        self.clear()

    # command
    def push(self, value):
        if self.size() < self._capacity:
            self._stack.append(value)
            self._push_status = BoundedStack.PUSH_OK
        else:
            self._push_status = BoundedStack.PUSH_ERR

    def pop(self):
        if self.size() > 0:
            self._stack.pop()
            self._pop_status = BoundedStack.POP_OK
        else:
            self._pop_status = BoundedStack.POP_ERR

    def clear(self):
        self._stack = [] # private
        self._push_status = BoundedStack.PUSH_NIL # private
        self._pop_status = BoundedStack.POP_NIL   # private
        self._peek_status = BoundedStack.PEEK_NIL # private

    # query
    def peek(self):
        result = 0
        self._peek_status = BoundedStack.POP_ERR
        if self.size() > 0:
            self._peek_status = BoundedStack.POP_OK
            result = self._stack[-1]
        return result

    def size(self):
        return len(self._stack)

    def max_size(self):
        return self._capacity

    # query statuses
    def get_push_status(self):
        return self._push_status

    def get_pop_status(self):
        return self._pop_status

    def get_peek_status(self):
        return self._peek_status
