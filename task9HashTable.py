class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str):
        summ = 0
        for i in range(0, len(value)-1):
            summ += ord(value[i])
        return summ % self.size


    def seek_slot(self, value):
        if self.slots[self.hash_fun(value)] is None:
            return self.hash_fun(value)
        global j
        j = self.hash_fun(value)+self.step
        for i in range(0, self.step+2):
            for j in range(j, self.size, self.step):
                if self.slots[j] is None:
                    return j
            j = i
        return None

    def put(self, value):
        if self.seek_slot(value) is not None:
            temp = self.seek_slot(value)
            self.slots[self.seek_slot(value)] = value
            return temp
        return None

    def find(self, value):
        for i in range(0, self.size):
            if value == self.slots[i]:
                return i
        return None



tabl = HashTable(19, 3)
print('hf: ', tabl.hash_fun("ass"))
print(tabl.put("re"))
print(tabl.put("we"))
print(tabl.put("ass"))
print(tabl.put("rwe"))
print(tabl.put("fd"))
print(tabl.put("asgfs"))
print(tabl.put("c"))
print(tabl.put("sdf"))
print(tabl.put("ashgs"))
print(tabl.put("askjs"))
print(tabl.put("f"))
print(tabl.put("asfdfs"))
print(tabl.put("df"))
print(tabl.put("agfss"))
print(tabl.put("adfss"))
print(tabl.put("afdgfdss"))
print(tabl.put("ascvs"))
print(tabl.put("axcvss"))
print(tabl.put("asnvbns"))
print(tabl.put("asmns"))

print(tabl.slots)
print(tabl.find("ascvs"))
#print(tabl.hash_fun(' '))

import unittest
class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.h_table: HashTable = HashTable(19, 3)

    def test_find_el_in_single_el(self) -> None:
        self.h_table: HashTable = HashTable(19, 3)
        self.assertEqual(self.h_table.size, 19)
        self.assertEqual(self.h_table.step, 3)
        self.h_table.put("15")
        self.assertEqual(self.h_table.slots,
                         [None, None, None, None, None, None, None, None, None, None, None, '15', None, None, None,
                          None, None, None, None])
        self.assertEqual(self.h_table.find('15'), 11)
        self.assertEqual(self.h_table.seek_slot('15'), 14)
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.assertEqual(self.h_table.slots,
                         ['15', '15', None, '15', None, None, '15', None, None, '15', None, '15', '15', None, '15',
                          '15', None, '15', '15'])
        self.assertEqual(self.h_table.find('15'), 0)
        self.assertEqual(self.h_table.hash_fun('a'), 0)
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("14")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.h_table.put("15")
        self.assertEqual(self.h_table.slots,
                         ['15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '14', '15',
                          '15', '15', '15', '15'])
        self.assertEqual(self.h_table.seek_slot('dfdf'), None)
        self.assertEqual(self.h_table.find('14'), 13)





if __name__ == "__main__":
    unittest.main()

