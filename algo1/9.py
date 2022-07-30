class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        hash_sum = 0
        for ch in key:
            hash_sum += ord(ch)
        return hash_sum % self.size

    def is_key(self, key):
        return self.get(key) is not None

    def put(self, key, value):
        insert_idx = self.hash_fun(key)
        if self.slots[insert_idx] is None:
            self.slots[insert_idx] = []
            self.values[insert_idx] = []
        for i in range(len(self.slots[insert_idx])):
            el = self.slots[insert_idx][i]
            if el == key:
                self.values[insert_idx][i] = value
                return
        self.slots[insert_idx].append(key)
        self.values[insert_idx].append(value)

    def get(self, key):
        for i in range(len(self.slots)):
            el = self.slots[i]
            if el is None:
                continue
            for j in range(len(el)):
                if el[j] == key:
                    return self.values[i][j]
        return None

    def show(self):
        for i in range(len(self.slots)):
            if self.slots[i] is None:
                continue
            for j in range(len(self.slots[i])):
                print(f'{self.slots[i][j]}: {self.values[i][j]}')
