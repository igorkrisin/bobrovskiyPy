import unittest


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item: int) -> None:
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        temp = self.queue[0]
        del self.queue[0]
        return temp

    def size(self):
        return len(self.queue)

    def rotate_queue(self, quant):
        if self.size() == 0:
            return None
        for i in range(0, quant):
            self.enqueue(self.dequeue())


qu = Queue()
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.enqueue(8)
qu.enqueue(9)
qu.rotate_queue(4)
print(qu.queue)


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.que: Queue = Queue()

    def test_dequeue_single_el(self) -> None:
        self.que: Queue = Queue()
        self.assertEqual(self.que.size(), 0)
        self.que.enqueue(4)
        self.assertEqual(self.que.size(), 1)
        self.assertEqual(self.que.dequeue(), 4)
        self.assertEqual(self.que.queue, [])
        self.assertEqual(self.que.size(), 0)

    def test_enqueue_few_el_dequeue_few_el(self) -> None:
        self.que: Queue = Queue()
        self.assertEqual(self.que.size(), 0)
        self.que.enqueue(0)
        self.que.enqueue(1)
        self.que.enqueue(2)
        self.que.enqueue(3)
        self.que.enqueue(4)
        self.que.enqueue(5)
        self.assertEqual(self.que.size(), 6)
        self.que.dequeue()
        self.assertEqual(self.que.queue, [1, 2, 3, 4, 5])
        self.assertEqual(self.que.size(), 5)
        self.que.dequeue()
        self.assertEqual(self.que.queue, [2, 3, 4, 5])
        self.assertEqual(self.que.size(), 4)
        self.que.dequeue()
        self.que.dequeue()
        self.que.dequeue()
        self.que.dequeue()
        self.assertEqual(self.que.queue, [])
        self.assertEqual(self.que.size(), 0)

    def test_rotation_queue(self) -> None:
        self.qu: Queue = Queue()
        self.assertEqual(self.que.size(), 0)
        self.qu.enqueue(0)
        self.qu.enqueue(1)
        self.qu.enqueue(2)
        self.qu.enqueue(3)
        self.qu.enqueue(4)
        self.qu.enqueue(5)
        self.assertEqual(self.qu.queue, [0, 1, 2, 3, 4, 5])
        self.assertEqual(self.qu.size(), 6)
        self.qu.rotate_queue(3)
        self.assertEqual(self.qu.queue, [3, 4, 5, 0, 1, 2])
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.rotate_queue(3)
        self.assertEqual(self.qu.queue, [])


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
