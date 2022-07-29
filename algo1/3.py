import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.MIN_CAPACITY = 16
        self.capacity = self.MIN_CAPACITY
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def _right_shift(self, i):
        for i in range(self.count, i, -1):
            self.array[i] = self.array[i - 1]

    def _left_shift(self, i):
        for i in range(i, self.count - 1):
            self.array[i] = self.array[i + 1]

    def insert(self, i, itm):
        if not(0 <= i <= self.count):
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self._right_shift(i)
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if not(0 <= i < self.count):
            raise IndexError('Index is out of bounds')
        self._left_shift(i)
        self.count -= 1
        if self.count * 2 < self.capacity:
            self.resize(max(self.MIN_CAPACITY, int(self.capacity / 1.5)))

    def show(self):
        for i in range(0, self.count):
            print(self.array[i], end=' ')
        print(f'\ncount {self.count}   cap {self.capacity}\n')
