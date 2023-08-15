class PowerSet:

    def __init__(self):
        self.pow_set = []

    def size(self) -> int:
        return len(self.pow_set)

    def put(self, value: object) -> None:
        if self.pow_set.count(value) == 0:
            self.pow_set.append(value)

    def get(self, value: object) -> bool:
        if value in self.pow_set:
            return True
        return False

    def remove(self, value) -> bool:
        for i in range(0, len(self.pow_set)):
            if value == self.pow_set[i]:
                self.pow_set.pop(i)
                return True
        return False

    def intersection(self, set2: 'PowerSet') -> 'PowerSet':
        set_summ: PowerSet = PowerSet()
        for i in range(0, len(self.pow_set)):
            if self.pow_set[i] in set2.pow_set:
                set_summ.put(self.pow_set[i])
        if len(set_summ.pow_set) > 0:
            return set_summ
        return set_summ

    def union(self, set2: 'PowerSet') -> 'PowerSet':
        summ_set: PowerSet = PowerSet()
        for i in range(0, set2.size()):
            summ_set.put(set2.pow_set[i])
        for i in range(0, self.size()):
            summ_set.put(self.pow_set[i])
        return summ_set

    def difference(self, set2: 'PowerSet') -> 'PowerSet':
        summ_set: PowerSet = PowerSet()
        for i in self.pow_set:
            if i not in set2.pow_set:
                summ_set.put(i)
        return summ_set

    def issubset(self, set2: 'PowerSet') -> bool:
        summ_set: PowerSet = PowerSet()
        for i in self.pow_set:
            if i in set2.pow_set:
                summ_set.put(i)
        if summ_set.size() == set2.size():
            return True
        return False


set_pow = PowerSet()
set_pow2 = PowerSet()
set_pow.put(53)
set_pow.put(5)
set_pow.put(67)
set_pow.put(67)
set_pow.put(89)
set_pow.put(0)
set_pow.put(22)

print(set_pow.pow_set)
print(set_pow2.pow_set)
print('union: ', set_pow.union(set_pow2).pow_set)
print('difference: ', set_pow.difference(set_pow2).pow_set)
print('issub:', set_pow.issubset(set_pow2))
print(set_pow.intersection(set_pow2).pow_set)


'''import unittest
class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.o_list: PowerSet = PowerSet()

    def test_put_single_el_in_empty_set(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.assertEqual(self.p_set.pow_set, [15])
        self.assertEqual(self.p_set.size(), 1)
        self.assertEqual(self.p_set.get(15), True)
        self.p_set.remove(15)
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)

    def test_put_single_multy_in_empty_set(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.assertEqual(self.p_set.pow_set, [15, 16, 17, 18])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set.get(17), True)
        self.p_set.remove(17)
        self.assertEqual(self.p_set.size(), 3)
        self.assertEqual(self.p_set.get(17), False)

    def test_put_same_el(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.assertEqual(self.p_set.pow_set, [15, 16, 17, 18])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set.get(17), True)
        self.p_set.remove(17)
        self.assertEqual(self.p_set.size(), 3)
        self.assertEqual(self.p_set.get(17), False)
        self.p_set.put(15)
        self.assertEqual(self.p_set.pow_set, [15, 16, 18])

    def test_intersection(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set2: PowerSet = PowerSet()
        self.p_set2.put(19)
        self.p_set2.put(29)
        self.p_set2.put(17)
        self.p_set2.put(2)
        self.assertEqual(self.p_set2.pow_set, [19, 29, 17, 2])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set.get(17), True)
        self.assertEqual(self.p_set.intersection(self.p_set2).pow_set, [17])

    def test_intersection_empty_second_set(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set2: PowerSet = PowerSet()
        self.p_set2.put(45)
        self.p_set2.put(67)
        self.p_set2.put(89)
        self.p_set2.put(0)
        self.assertEqual(self.p_set2.pow_set, [45, 67, 89, 0])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set.get(17), True)
        self.assertEqual(self.p_set.intersection(self.p_set2).pow_set, [])

    def test_union(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set2: PowerSet = PowerSet()
        self.p_set2.put(19)
        self.p_set2.put(29)
        self.p_set2.put(17)
        self.p_set2.put(2)
        self.assertEqual(self.p_set2.pow_set, [19, 29, 17, 2])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set.get(17), True)
        self.assertEqual(self.p_set.union(self.p_set2).pow_set, [15, 16, 17, 18, 19, 29, 2])
        self.assertEqual(self.p_set.size(), 7)

    def test_union_empty_set_2(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set2: PowerSet = PowerSet()
        self.assertEqual(self.p_set2.pow_set, [])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set.get(17), True)
        self.assertEqual(self.p_set.union(self.p_set2).pow_set, [15, 16, 17, 18])

    def test_union_empty_set_1(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.p_set2: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set2.put(15)
        self.p_set2.put(16)
        self.p_set2.put(17)
        self.p_set2.put(18)
        self.assertEqual(self.p_set.pow_set, [])
        self.assertEqual(self.p_set2.size(), 4)
        self.assertEqual(self.p_set2.get(17), True)
        self.assertEqual(self.p_set.union(self.p_set2).pow_set, [15, 16, 17, 18])

    def test_difference(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set2: PowerSet = PowerSet()
        self.p_set2.put(19)
        self.p_set2.put(29)
        self.p_set2.put(17)
        self.p_set2.put(2)
        self.assertEqual(self.p_set2.pow_set, [19, 29, 17, 2])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set.get(18), True)
        self.assertEqual(self.p_set.difference(self.p_set2).pow_set, [15, 16, 18])

    def test_difference_empty_set_1(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set2: PowerSet = PowerSet()
        self.p_set2.put(19)
        self.p_set2.put(29)
        self.p_set2.put(17)
        self.p_set2.put(2)
        self.assertEqual(self.p_set2.pow_set, [19, 29, 17, 2])
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set2.get(19), True)
        self.assertEqual(self.p_set.difference(self.p_set2).pow_set, [])

    def test_difference_is_empty_set_2(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set2: PowerSet = PowerSet()
        self.assertEqual(self.p_set2.pow_set, [])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set.get(15), True)
        self.assertEqual(self.p_set.difference(self.p_set2).pow_set, [15, 16, 17, 18])

    def test_issubset_false(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set2: PowerSet = PowerSet()
        self.p_set2.put(19)
        self.p_set2.put(29)
        self.p_set2.put(17)
        self.p_set2.put(2)
        self.assertEqual(self.p_set2.pow_set, [19, 29, 17, 2])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set2.get(123), False)
        self.assertEqual(self.p_set.issubset(self.p_set2), False)

    def test_issubset_false_dont_all_el_in_set1(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set2: PowerSet = PowerSet()
        self.p_set2.put(15)
        self.p_set2.put(16)
        self.p_set2.put(17)
        self.p_set2.put(2)
        self.assertEqual(self.p_set2.pow_set, [15, 16, 17, 2])
        self.assertEqual(self.p_set.size(), 4)
        self.assertEqual(self.p_set2.get(123), False)
        self.assertEqual(self.p_set.issubset(self.p_set2), False)

    def test_issubset_true(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set.put(15)
        self.p_set.put(16)
        self.p_set.put(17)
        self.p_set.put(18)
        self.p_set.put(53)
        self.p_set.put(78)
        self.p_set2: PowerSet = PowerSet()
        self.p_set2.put(18)
        self.p_set2.put(78)
        self.p_set2.put(17)
        self.assertEqual(self.p_set2.pow_set, [18, 78, 17])
        self.assertEqual(self.p_set.size(), 6)
        self.assertEqual(self.p_set2.get(123), False)
        self.assertEqual(self.p_set.issubset(self.p_set2), True)

    def test_issubset_set_in_set2(self) -> None:
        self.p_set: PowerSet = PowerSet()
        self.p_set2: PowerSet = PowerSet()
        self.assertEqual(self.p_set.size(), 0)
        self.assertEqual(self.p_set.get(15), False)
        self.p_set2.put(15)
        self.p_set2.put(16)
        self.p_set2.put(17)
        self.p_set2.put(18)
        self.p_set2.put(53)
        self.p_set2.put(78)
        self.p_set.put(18)
        self.p_set.put(78)
        self.p_set.put(17)
        self.assertEqual(self.p_set.pow_set, [18, 78, 17])
        self.assertEqual(self.p_set2.size(), 6)
        self.assertEqual(self.p_set2.get(123), False)
        self.assertEqual(self.p_set.issubset(self.p_set2), False)


if __name__ == "__main__":
    unittest.main()'''

