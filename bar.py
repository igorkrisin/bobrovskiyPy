class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        self.stack = self.stack[1:]
        if self.size() == 0:
            return None

    def push(self, value) -> None:
        self.stack = [value] + self.stack

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[0]
