class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        summ = 0
        for i in range(0, len(key) - 1):
            summ += ord(key[i])
        return summ % self.size

    def is_key(self, key):
        for i in range(0, self.size):
            if self.slots[i] == key:
                return True
        return False

    def put(self, key, value):
        ind = self.hash_fun(key)
        self.slots[ind] = key
        self.values[ind] = value

    def get(self, key):
        for i in range(0, self.size):
            if key == self.slots[i]:
                return self.values[i]
        return None
    