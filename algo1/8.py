class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash_sum = 0
        for ch in value:
            hash_sum += ord(ch)
        return hash_sum % self.size

    def seek_slot(self, value):
        idx = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[idx] is None:
                return idx
            idx = (idx + self.step) % self.size
        return None

    def put(self, value):
        insert_idx = self.seek_slot(value)
        if insert_idx is None:
            return None
        self.slots[insert_idx] = value
        return insert_idx

    def find(self, value):
        for i in range(len(self.slots)):
            el = self.slots[i]
            if el == value:
                return i
        return None

    def show(self):
        print(self.slots)
