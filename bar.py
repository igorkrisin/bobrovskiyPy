
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item: int) -> None:
        self.queue.append(item)

    def dequeue(self) -> object:
        if self.size() == 0:
            return None
        temp: object = self.queue[0]
        del self.queue[0]
        return temp

    def size(self):
        return len(self.queue)
    