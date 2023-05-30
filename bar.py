class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

<<<<<<< HEAD
    def pop(self):
        if self.size() == 0:
            return None
        self.stack = self.stack[1:]

    def push(self, value) -> None:
        self.stack = [value] + self.stack

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[0]
=======
    def make_array(self, new_capacity: int):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i: int) -> None:
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity: int) -> None:
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

    def delete(self, i: int) -> None:
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
        self.check_capacity_and_resize()

    def check_capacity_and_resize(self) -> None:
        if self.capacity / self.count > 2 and int(self.capacity / 1.5) > 16:
            self.resize(int(self.capacity / 1.5))
        elif self.capacity / self.count > 2 and int(self.capacity / 1.5) < 16:
            self.resize(16)
>>>>>>> 75454354e2c38e7116f516447f38820b33a20292
