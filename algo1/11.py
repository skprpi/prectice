class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.arr = [False] * f_len

    def hash_func(self, string, n):
        res = 0
        for ch in string:
            res = (res * n + ord(ch)) % self.filter_len
        return res

    def hash1(self, str1):
        return self.hash_func(str1, 17)

    def hash2(self, str1):
        return self.hash_func(str1, 223)

    def add(self, str1):
        h1, h2 = self.hash1(str1), self.hash2(str1)
        self.arr[h1] = True
        self.arr[h2] = True

    def is_value(self, str1):
        h1, h2 = self.hash1(str1), self.hash2(str1)
        return self.arr[h1] and self.arr[h2]
