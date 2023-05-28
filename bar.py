import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
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
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm) -> None:
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == 0 and i == 0:
            self.array[0] = itm
            self.count += 1
            return
        elif self.count == self.capacity and i == self.count:
            self.resize(2 * self.capacity)
            self.array[i] = itm
            self.count += 1
            return
        elif i == self.count:
            self.array[i] = itm
            self.count += 1
            return
        elif self.count == self.capacity:
            self.resize(2 * self.capacity)
            self.count += 1
        else:
            self.count += 1

        for j in range(self.count-1, i, -1):
            self.array[j] = self.array[j-1]
        self.array[i] = itm

    def delete(self, i) -> None:
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        else:
            for j in range(i, self.count - 1):
                self.array[j] = self.array[j+1]
            self.count -= 1
            if self.count < 0:
                raise IndexError('Index is out of bounds')
        if self.count == 0:
            return
        if self.capacity/self.count > 2 and self.capacity > 16:
            self.capacity = int(self.capacity/1.5)
