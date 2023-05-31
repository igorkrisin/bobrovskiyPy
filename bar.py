class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        temp = self.stack[self.size()-1]
        del self.stack[self.size()-1]
        return temp


    def push(self, value) -> None:
        self.stack = self.stack + [value]

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[self.size()-1]