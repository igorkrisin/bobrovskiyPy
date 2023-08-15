class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        summ = 0
        for i in range(0, len(key) - 1):
            summ += ord(key[i])
        return summ % self.size

    def is_key(self, key):
        for i in range(0, self.size):
            if self.slots[i] == key:
                return True
        return False

    def put(self, key, value):
        ind = self.hash_fun(key)
        self.slots[ind] = key
        self.values[ind] = value

    def get(self, key):
        for i in range(0, self.size):
            if key == self.slots[i]:
                return self.values[i]
        return None

    def seek_slot(self, key):
        if self.slots[self.hash_fun(key)] is None:
            return self.hash_fun(key)
        global j
        j = self.hash_fun(key)+2
        for i in range(0, 5):
            for j in range(j, self.size, 2):
                if self.slots[j] is None:
                    return j
            j = i
        return None


natDict = NativeDictionary(20)
natDict.put("grad", "35")
natDict.put("week", "22")
natDict.put("hour", "9")
natDict.put("day", "4")
natDict.put("hour", "10")
natDict.put("min", "8")
print('is: ', natDict.is_key("key 2"))
print('get:', natDict.get("gtr"))
print('get:', natDict.get("gr"))
print("val: ", natDict.values)
print("slot: ", natDict.slots)


import unittest
class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.h_table: NativeDictionary = NativeDictionary(20)

    def test_find_el_in_single_el(self) -> None:
        self.h_table: NativeDictionary = NativeDictionary(20)
        self.assertEqual(self.h_table.size, 20)
        self.assertEqual(self.h_table.get("re"), None)
        self.assertEqual(self.h_table.is_key("re"), False)
        self.h_table.put("key1", "14")
        self.assertEqual(self.h_table.is_key("key1"), True)
        self.assertEqual(self.h_table.is_key("rew"), False)
        self.assertEqual(self.h_table.get("key1"), "14")
        self.h_table.put("week", "22")
        self.h_table.put("day", "4")
        self.h_table.put("hour", "9")
        self.h_table.put("min", "8")
        print(self.h_table.values)
        self.assertEqual(self.h_table.size, 20)
        self.assertEqual(self.h_table.is_key("week"), True)
        self.assertEqual(self.h_table.is_key("wek"), False)
        self.assertEqual(self.h_table.get("day"), "4")
        self.assertEqual(self.h_table.get("min"), "8")
        self.h_table.put("grad", "35")
        self.assertEqual(self.h_table.get("grad"), "35")
        self.assertEqual(self.h_table.is_key("grad"), True)
        self.assertEqual(self.h_table.get("gra"), None)


if __name__ == "__main__":
    unittest.main()
