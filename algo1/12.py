class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.cnt = 0
        self.step = 1

    def hash_fun(self, key):
        hash_sum = 0
        for ch in key:
            hash_sum += ord(ch)
        return hash_sum % self.size

    def seek_slot(self, key):
        idx = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[idx] is None:
                return idx
            idx = (idx + self.step) % self.size
        return None

    def get_low_hit_element_idx(self, key):
        min_value = float('inf')
        min_idx = -1
        idx = self.hash_fun(key)
        for _ in range(self.size):
            if min_idx == -1 or min_value > self.hits[idx]:
                min_value = self.hits[idx]
                min_idx = idx
            idx = (idx + self.step) % self.size
        assert(min_idx >= 0)
        return min_idx

    def delete_slot(self, idx):
        assert(0 <= idx < self.cnt)
        self.slots[idx] = None
        self.values[idx] = None
        self.hits[idx] = 0

    def put(self, key, value):
        insert_idx = self._find_idx(key)
        if insert_idx is not None:
            self.values[insert_idx] = value
            self.hits[insert_idx] += 1
            return
        insert_idx = self.seek_slot(key)
        if insert_idx is None:
            delete_idx = self.get_low_hit_element_idx(key)
            self.delete_slot(delete_idx)
            self.cnt -= 1
            insert_idx = delete_idx
        self.cnt += 1
        self.slots[insert_idx] = key
        self.values[insert_idx] = value
        self.hits[insert_idx] = 1

    def _find_idx(self, key):
        for i in range(len(self.slots)):
            el = self.slots[i]
            if el == key:
                return i
        return None

    def find(self, key):
        idx = self._find_idx(key)
        if idx is not None:
            self.hits[idx] += 1
        return idx

    def show(self):
        for i in range(3):
            print(self.slots[i], self.values[i], self.hits[i])
        print(self.cnt)
        print()
