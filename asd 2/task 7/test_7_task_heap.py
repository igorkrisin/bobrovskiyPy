import unittest
from task_7_Heap import Heap


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.heap = Heap()
        self.assertEqual(self.heap.GetMax(), -1)
        self.heap.MakeHeap([1, 2, 3, 4, 5, 6, 7, 8], 2)

    def test_make_heap(self):
        self.main_heap = Heap()
        self.main_heap.MakeHeap([], 1)
        self.assertEqual(self.main_heap.return_heap(), [None, None, None])
        self.main_heap.MakeHeap([], 0)
        self.assertEqual(self.main_heap.return_heap(), [None])
        self.main_heap.MakeHeap([], 2)
        self.assertEqual(self.main_heap.return_heap(), [None, None, None, None, None, None, None])
        self.main_heap.MakeHeap([1, 22, 34, 56, 77, 22, 11, 22, 34, 65, 60, 43, 20, 55, 77], 3)
        self.assertEqual(self.main_heap.return_heap(),
                         [77, 65, 77, 34, 60, 22, 55, 1, 22, 34, 56, 22, 20, 11, 43])

    def test_add_same_node_in_full_heap(self):
        self.assertEqual(self.heap.Add(4), False)

    def test_add_same_node(self):
        self.heap3 = Heap()
        self.heap3.MakeHeap([20, 2, 44, 5, 66, 7], 2)
        self.assertEqual(self.heap3.return_heap(), [66, 44, 20, 2, 5, 7, None])
        self.assertEqual(self.heap3.Add(44), True)
        self.assertEqual(self.heap3.return_heap(), [66, 44, 44, 2, 5, 7, 20])

    def test_make_empty_heap(self) -> None:
        self.empty_heap = Heap()
        self.heap.MakeHeap([], 3),
        self.assertEqual(self.heap.return_heap(), [None, None, None, None, None, None, None, None, None, None,
                                                   None, None, None, None, None])

    def test_add_to_full_heap(self) -> None:
        self.full_heap = Heap()
        self.full_heap.MakeHeap([0, 1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(self.full_heap.return_heap(), [6, 3, 5, 0, 2, 1, 4])
        self.assertEqual(self.full_heap.Add(15), False)
        self.assertEqual(self.full_heap.Add(15), False)

    def test_add_last_node(self):
        self.heap2 = Heap()
        self.heap2.MakeHeap([0, 1, 2, 3, 4, 5], 2)
        self.assertEqual(self.heap2.return_heap(), [5, 3, 4, 0, 2, 1, None])
        self.assertEqual(self.heap2.Add(15), True)
        self.assertEqual(self.heap2.return_heap(), [15, 3, 5, 0, 2, 1, 4])

    def test_add_heap_to_full_plus_1_node(self):
        self.empty_heap_2 = Heap()
        self.empty_heap_2.MakeHeap([], 2)
        self.assertEqual(self.empty_heap_2.Add(34), True)
        self.assertEqual(self.empty_heap_2.return_heap(), [34, None, None, None, None, None, None])
        self.assertEqual(self.empty_heap_2.Add(42), True)
        self.assertEqual(self.empty_heap_2.Add(54), True)
        self.assertEqual(self.empty_heap_2.Add(2), True)
        self.assertEqual(self.empty_heap_2.return_heap(), [54, 34, 42, 2, None, None, None])
        self.assertEqual(self.empty_heap_2.Add(50), True)
        self.assertEqual(self.empty_heap_2.Add(100), True)
        self.assertEqual(self.empty_heap_2.Add(40), True)
        self.assertEqual(self.empty_heap_2.return_heap(), [100, 50, 54, 2, 34, 42, 40])
        self.assertEqual(self.empty_heap_2.Add(34), False)

    def test_get_from_empty_heap(self):
        self.empty_heap = Heap()
        self.heap.MakeHeap([], 3)
        self.assertEqual(self.empty_heap.GetMax(), -1)

    def test_get_from_empty_heap_depth_zero(self):
        self.empty_heap = Heap()
        self.empty_heap.MakeHeap([], 0)
        self.assertEqual(self.empty_heap.GetMax(), -1)

    def test_get_from_last_node_depth_zero(self):
        self.empty_heap = Heap()
        self.empty_heap.MakeHeap([5], 0)
        self.assertEqual(self.empty_heap.GetMax(), 5)
        self.assertEqual(self.empty_heap.return_heap(), [None])

    def test_get_from_full_heap(self):
        self.full_heap = Heap()
        self.full_heap.MakeHeap([0, 1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(self.full_heap.return_heap(), [6, 3, 5, 0, 2, 1, 4])
        self.assertEqual(self.full_heap.GetMax(), 6)
        self.assertEqual(self.full_heap.return_heap(), [5, 3, 4, 0, 2, 1, None])

    def test_get_last_node(self):
        self.heap_one_node = Heap()
        self.heap_one_node.MakeHeap([0], 2)
        self.assertEqual(self.heap_one_node.return_heap(), [0, None, None, None, None, None, None])
        self.assertEqual(self.heap_one_node.GetMax(), 0)
        self.assertEqual(self.heap_one_node.return_heap(), [None, None, None, None, None, None, None])

    def test_get_all_node_from_full_heap_and_add_to_full_heap(self):
        self.full_heap = Heap()
        self.full_heap.MakeHeap([22, 46, 78, 109, 2, 5, 67], 2)
        self.assertEqual(self.full_heap.return_heap(), [109, 78, 67, 22, 2, 5, 46])
        self.assertEqual(self.full_heap.GetMax(), 109)
        self.assertEqual(self.full_heap.return_heap(), [78, 46, 67, 22, 2, 5, None])
        self.assertEqual(self.full_heap.GetMax(), 78)
        self.assertEqual(self.full_heap.return_heap(), [67, 46, 5, 22, 2, None, None])
        self.assertEqual(self.full_heap.GetMax(), 67)
        self.assertEqual(self.full_heap.return_heap(), [46, 22, 5, 2, None, None, None])
        self.assertEqual(self.full_heap.GetMax(), 46)
        self.assertEqual(self.full_heap.return_heap(), [22, 2, 5, None, None, None, None])
        self.assertEqual(self.full_heap.GetMax(), 22)
        self.assertEqual(self.full_heap.return_heap(), [5, 2, None, None, None, None, None])
        self.assertEqual(self.full_heap.GetMax(), 5)
        self.assertEqual(self.full_heap.return_heap(), [2, None, None, None, None, None, None])
        self.assertEqual(self.full_heap.GetMax(), 2)
        self.assertEqual(self.full_heap.return_heap(), [None, None, None, None, None, None, None])
        self.assertEqual(self.full_heap.GetMax(), -1)
        self.assertEqual(self.full_heap.return_heap(), [None, None, None, None, None, None, None])
        self.assertEqual(self.full_heap.Add(34), True)
        self.assertEqual(self.full_heap.return_heap(), [34, None, None, None, None, None, None])
        self.assertEqual(self.full_heap.Add(42), True)
        self.assertEqual(self.full_heap.Add(54), True)
        self.assertEqual(self.full_heap.Add(2), True)
        self.assertEqual(self.full_heap.return_heap(), [54, 34, 42, 2, None, None, None])
        self.assertEqual(self.full_heap.Add(50), True)
        self.assertEqual(self.full_heap.Add(100), True)
        self.assertEqual(self.full_heap.Add(40), True)
        self.assertEqual(self.full_heap.return_heap(), [100, 50, 54, 2, 34, 42, 40])
        self.assertEqual(self.full_heap.Add(34), False)
        self.assertEqual(self.full_heap.GetMax(), 100)
        self.assertEqual(self.full_heap.return_heap(), [54, 50, 42, 2, 34, 40, None])

    def test_get_depth_three(self):
        self.full_heap2 = Heap()
        self.full_heap2.MakeHeap([22, 46, 78, 109, 2, 5, 67, 100, 150, 160, 180, 2, 3, 1, 22], 3)
        self.full_heap2.print_heap()
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.Add(900)
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.Add(222)
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.print_heap()  # here error 5 in leaf node, 2 him parent
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.GetMax()
        self.full_heap2.print_heap()

    def test_get_when_key_equal_each_other(self):
        self.full_heap3 = Heap()
        self.full_heap3.MakeHeap([22, 22], 1)
        self.assertEqual(self.full_heap3.GetMax(), 22)
        self.assertEqual(self.full_heap3.return_heap(), [22, None, None])
        self.assertEqual(self.full_heap3.GetMax(), 22)
        self.assertEqual(self.full_heap3.GetMax(), -1)
        self.full_heap3 = Heap()
        self.full_heap3.MakeHeap([0, 0], 1)
        self.assertEqual(self.full_heap3.GetMax(), 0)
        self.assertEqual(self.full_heap3.return_heap(), [0, None, None])
        self.assertEqual(self.full_heap3.GetMax(), 0)
        self.assertEqual(self.full_heap3.GetMax(), -1)


if __name__ == "__main__":
    unittest.main()
