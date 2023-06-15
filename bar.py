class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        summ = 0
        for i in range(0, len(key) - 1):
            summ += ord(key[i])
        return summ % self.size

    def is_key(self, key):
        for i in range(0, self.size):
            if self.slots[i] == key:
                self.hits[i] += 1
                return True
        return False

    def put(self, key, value):
        ind = self.hash_fun(key)
        if self.is_crowded():
            min_ind = self.min_hits()
            self.slots[min_ind] = None
            self.values[min_ind] = None
            self.hits[min_ind] = 0
            self.slots[min_ind] = key
            self.values[min_ind] = value
            return
        self.slots[ind] = key
        self.values[ind] = value

    def get(self, key):
        for i in range(0, self.size):
            if key == self.slots[i]:
                self.hits[i] += 1
                return self.values[i]
        return None

    def is_crowded(self) -> bool:
        for i in range(0, self.size):
            if self.values[i] is None:
                return False
        return True

    def min_hits(self) -> int:
        min_hits: int = self.hits[0]
        min_ind = 0
        for i in range(0, self.size):
            if self.hits[i] < min_hits:
                min_hits = self.hits[i]
                min_ind = i
        return min_ind
    