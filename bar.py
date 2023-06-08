class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str):
        summ = 0
        for i in range(0, len(value)-1):
            summ += ord(value[i])
        return summ % self.size


    def seek_slot(self, value):
        if self.slots[self.hash_fun(value)] is None:
            return self.hash_fun(value)
        global j
        j = self.hash_fun(value)+self.step
        for i in range(0, self.step+2):
            for j in range(j, self.size, self.step):
                if self.slots[j] is None:
                    return j
            j = i
        return None

    def put(self, value):
        if self.seek_slot(value) is not None:
            temp = self.seek_slot(value)
            self.slots[self.seek_slot(value)] = value
            return temp
        return None

    def find(self, value):
        for i in range(0, self.size):
            if value == self.slots[i]:
                return i
        return None