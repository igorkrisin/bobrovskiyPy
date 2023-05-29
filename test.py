import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

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
        if self.capacity/self.count > 2 and self.capacity > 16:
            self.resize(int(self.capacity/1.5))
        elif self.capacity/self.count > 2 and self.capacity == 16:
            self.resize(self.capacity * 1)



    def create_arr(self, size: int) -> None:
        for i in range(0, size):
            self.append(i)

    def convert_darr_to_list(self) -> [int]:
        arr: [int] = []
        #print('sc: ', self.count)
        for i in range(0, self.count):
            arr.append(self.array[i])
        return arr

    def print_da(self) -> None:
        for i in range(0, self.count):
            print(self.array[i])





da = DynArray()
da.create_arr(3)


print('da1: ', da.convert_darr_to_list())

print('dacap1: ', da.capacity)
print('daco1: ', da.count)

da.delete(0)


print('da2: ', da.convert_darr_to_list())
print('dacap2: ', da.capacity)
print('daco2: ', da.count)

da.print_da()
#da.delete(16)
#print('daco3: ',da.count)
#print('dacap3 :',da.capacity)
#print('da3: ', da.convert_darr_to_list())
#da.print_da()


'''import unittest
class DinamycArrTest(unittest.TestCase):
    #print('test')
    def test_insert_in_arr_in_tail_i_equal_len(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(16)
        self.arr.insert(16, 18)
        #print(self.arr.convert_darr_to_list())
        self.assertEqual(self.arr.convert_darr_to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18])
        self.assertEqual(self.arr.count, 17)
        self.assertEqual(self.arr.capacity, 32)

    def test_insert_in_arr_size_capacity_not_over_in_middle(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(15)
        self.arr.insert(3, 18)
        self.assertEqual(self.arr.convert_darr_to_list(), [0, 1, 2, 18, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(self.arr.count, 16)
        self.assertEqual(self.arr.capacity, 16)

    def test_insert_in_arr_size_capacity_not_over_in_boundary(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(15)
        self.arr.insert(15, 18)
        self.assertEqual(self.arr.convert_darr_to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18])
        self.assertEqual(self.arr.count, 16)
        self.assertEqual(self.arr.capacity, 16)

    def test_insert_in_arr_middle_i_equal_len(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(16)
        self.arr.insert(5, 18)
        self.assertEqual(self.arr.convert_darr_to_list(), [0, 1, 2, 3, 4, 18, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(self.arr.count, 17)
        self.assertEqual(self.arr.capacity, 32)

    def test_insert_in_empty_arr(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.insert(0, 18)
        self.assertEqual(self.arr.convert_darr_to_list(), [18])
        self.assertEqual(self.arr.count, 1)
        self.assertEqual(self.arr.capacity, 16)


    def test_index_of_range_insert(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(15)

        with self.assertRaises(Exception) as context:
            self.arr.insert(17, 99)
            self.assertTrue('Index is out of bounds' in context.exception)

    def test_delete_last_el(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(15)
        self.arr.delete(14)
        self.assertEqual(self.arr.convert_darr_to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        self.assertEqual(self.arr.count, 14)
        self.assertEqual(self.arr.capacity, 16)

    def test_delete_when_capacity_min(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(15)
        self.arr.delete(14)
        self.arr.delete(13)
        self.arr.delete(12)
        self.assertEqual(self.arr.convert_darr_to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        self.assertEqual(self.arr.count, 12)
        self.assertEqual(self.arr.capacity, 16)

    def test_delete_middle_el_capacity_min(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(16)
        self.arr.delete(12)
        self.assertEqual(self.arr.convert_darr_to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15])
        self.assertEqual(self.arr.count, 15)
        self.assertEqual(self.arr.capacity, 16)

    def test_delete_middle_el_capacity_from_32_to_16(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(33)
        self.arr.delete(14)
        self.arr.delete(14)
        self.assertEqual(self.arr.convert_darr_to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])
        self.assertEqual(self.arr.count, 31)
        self.assertEqual(self.arr.capacity, 42)

    def test_delete_first_el(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(15)
        self.arr.delete(0)
        self.assertEqual(self.arr.convert_darr_to_list(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(self.arr.count, 14)
        self.assertEqual(self.arr.capacity, 16)

    def test_index_of_range_delete(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(17)

        with self.assertRaises(Exception) as context:
            self.arr.delete(18)
            self.assertTrue('Index is out of bounds' in context.exception)

    def test_delete_single_el(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(1)
        self.arr.delete(0)
        self.assertEqual(self.arr.convert_darr_to_list(), [])
        self.assertEqual(self.arr.count, 0)
        self.assertEqual(self.arr.capacity, 16)

    def test_element_of_range_delete(self) -> None:
        self.arr: DynArray = DynArray()
        self.arr.create_arr(5)
        with self.assertRaises(Exception) as context:
            self.arr.delete(0)
            self.arr.delete(0)
            self.arr.delete(0)
            self.arr.delete(0)
            self.arr.delete(0)
            self.arr.delete(0)
            self.assertTrue('Index is out of bounds' in context.exception)


if __name__ == "__main__":
    unittest.main()'''

