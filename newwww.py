from test import DynArray
import unittest


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.arr = DynArray()

    print('test')

    def test_insert_in_arr_in_tail_i_equal_len(self) -> None:
        arr = DynArray()
        arr.print_da()
        arr.create_arr(16)
        print('!!!:: ', arr.convert_darr_to_list(arr))
        arr.insert(16, 18)
        print(arr.convert_darr_to_list(arr))
        self.assertEqual(arr.convert_darr_to_list(arr), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18])
        self.assertEqual(arr.count, 17)
        self.assertEqual(arr.capacity, 32)

    def test_insert_in_arr_middle_i_equal_len(self) -> None:
        arr = DynArray()
        arr.create_arr(16)
        arr.insert(5, 18)
        self.assertEqual(arr.convert_darr_to_list(arr), [0, 1, 2, 3, 4, 18, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(arr.count, 17)
        self.assertEqual(arr.capacity, 32)


if __name__ == "__main__":
    unittest.main()

