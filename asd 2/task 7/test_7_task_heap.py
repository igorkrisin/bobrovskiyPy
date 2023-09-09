import unittest
from task_7_Heap import Heap


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.heap = Heap()
        self.heap.MakeHeap([1, 2, 3, 4, 5, 6, 7, 8], 2)

    def test_add_same_node_in_full_heap(self):
        self.assertEqual(self.heap.Add(4), False)

    def test_add_same_node(self):
        self.heap3 = Heap()
        self.heap3.MakeHeap([20, 2, 44, 5, 66, 7], 2)
        self.assertEqual(self.heap3.return_heap(), [66, 44, 20, 7, 5, 2, None])
        self.assertEqual(self.heap3.Add(44), True)
        self.assertEqual(self.heap3.return_heap(),[66, 44, 44, 7, 5, 2, 20])


    def test_make_empty_heap(self) -> None:
        self.empty_heap = Heap()
        self.heap.MakeHeap([], 3),
        self.assertEqual(self.heap.return_heap(), [None, None, None, None, None, None, None, None, None, None,
                                                   None, None, None, None, None])

    def test_add_to_full_heap(self) -> None:
        self.full_heap = Heap()
        self.full_heap.MakeHeap([0, 1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(self.full_heap.return_heap(), [6, 5, 4, 3, 2, 1, 0])
        self.assertEqual(self.full_heap.Add(15), False)
        self.assertEqual(self.full_heap.Add(15), False)

    def test_add_last_node(self):
        self.heap2 = Heap()
        self.heap2.MakeHeap([0, 1, 2, 3, 4, 5], 2)
        self.assertEqual(self.heap2.return_heap(), [5, 4, 3, 2, 1, 0, None])
        self.assertEqual(self.heap2.Add(15), True)
        self.assertEqual(self.heap2.return_heap(), [15, 4, 5, 2, 1, 0, 3])


if __name__ == "__main__":
    unittest.main()
