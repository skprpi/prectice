class PowerSet:

    def __init__(self):
        self.storage = {}

    def size(self):
        return len(self.storage)

    def put(self, value):
        self.storage[value] = True

    def get(self, value):
        return value in self.storage.keys()

    def remove(self, value):
        if value in self.storage.keys():
            del self.storage[value]
            return True
        return False

    def intersection(self, set2):
        intersection_set = PowerSet()
        for key in self.storage:
            if set2.get(key):
                intersection_set.put(key)
        return intersection_set 

    def union(self, set2):
        union_set = PowerSet()
        for key in self.storage:
            union_set.put(key)
        for key in set2.storage:
            union_set.put(key)
        return union_set

    def difference(self, set2):
        difference_set = PowerSet()
        for key in self.storage:
            if not set2.get(key):
                difference_set.put(key)
        return difference_set

    def issubset(self, set2):
        for key in set2.storage:
            if not self.get(key):
                return False
        return True

    def show(self):
        print(self.storage)
        print(self.size())
