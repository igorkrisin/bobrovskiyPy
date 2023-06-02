class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item) -> None:
        self.deque.append(item)

    def addTail(self, item) -> None:
        self.deque = [item] + self.deque

    def removeFront(self) -> object:
        if self.size() == 0:
            return None
        temp: object = self.deque[self.size()-1]
        del self.deque[self.size()-1]
        return temp

    def removeTail(self) -> object:
        if self.size() == 0:
            return None
        temp: object = self.deque[0]
        self.deque.pop(0)
        return temp

    def size(self) -> int:
        return len(self.deque)
