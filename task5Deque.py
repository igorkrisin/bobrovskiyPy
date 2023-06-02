import unittest


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
        self.deque.pop()

    def removeTail(self) -> object:
        if self.size() == 0:
            return None
        temp = self.deque[0]
        self.deque.pop(0)
        return temp

    def size(self) -> int:
        return len(self.deque)




deq = Deque()

deq.addTail(5)
deq.addTail(6)
print(deq.deque)
deq.addTail(8)
deq.addTail(9)
print(deq.deque)
deq.removeFront()
print(deq.deque)
deq.removeTail()
print(deq.deque)

class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.link: Deque = Deque()

    def test_deque(self) -> None:
        self.dequ: Deque = Deque()
        self.assertEqual(self.dequ.size(), 0)
        self.dequ.addFront(0)
        self.assertEqual(self.dequ.size(), 1)
        self.assertEqual(self.dequ.deque, [0])
        self.dequ.addFront(1)
        self.dequ.addFront(2)
        self.dequ.addFront(3)
        self.assertEqual(self.dequ.size(), 4)
        self.assertEqual(self.dequ.deque, [0, 1, 2, 3])
        self.dequ.addTail(4)
        self.dequ.addTail(5)
        self.dequ.addTail(6)
        self.assertEqual(self.dequ.size(), 7)
        self.assertEqual(self.dequ.deque, [6, 5, 4, 0, 1, 2, 3])
        self.dequ.removeFront()
        self.dequ.removeFront()
        self.assertEqual(self.dequ.size(), 5)
        self.assertEqual(self.dequ.deque, [6, 5, 4, 0, 1])
        self.dequ.removeTail()
        self.dequ.removeTail()
        self.dequ.removeTail()
        self.dequ.removeTail()
        self.assertEqual(self.dequ.size(), 1)
        self.assertEqual(self.dequ.deque, [1])
        self.dequ.removeFront()
        self.assertEqual(self.dequ.size(), 0)
        self.assertEqual(self.dequ.deque, [])





    if __name__ == "__main__":
        unittest.main()
