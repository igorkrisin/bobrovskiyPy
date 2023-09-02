import unittest
from binary_trees_in_arr import aBST


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.tree: aBST = aBST(3)

    def test_add_by_key(self) -> None:
        self.tre_arr: aBST = aBST(3)
        self.assertEqual(self.tree.FindKeyIndex(50), 0)
        self.assertEqual(self.tree.AddKey(50), 0)
        self.assertEqual(self.tree.AddKey(25), 1)
        self.assertEqual(self.tree.AddKey(75), 2)
        self.assertEqual(self.tree.AddKey(13), 3)
        self.assertEqual(self.tree.AddKey(35), 4)
        self.assertEqual(self.tree.AddKey(65), 5)
        self.assertEqual(self.tree.AddKey(85), 6)
        self.assertEqual(self.tree.AddKey(0), 7)
        self.assertEqual(self.tree.AddKey(18), 8)
        self.assertEqual(self.tree.AddKey(30), 9)
        self.assertEqual(self.tree.AddKey(45), 10)
        self.assertEqual(self.tree.AddKey(60), 11)
        self.assertEqual(self.tree.AddKey(70), 12)
        self.assertEqual(self.tree.AddKey(80), 13)
        self.assertEqual(self.tree.AddKey(90), 14)
        self.assertEqual(self.tree.AddKey(80), 13)
        self.assertEqual(self.tree.AddKey(100), -1)
        self.assertEqual(self.tree.AddKey(-100), -1)
        self.assertEqual(self.tree.FindKeyIndex(100), None)
        self.assertEqual(self.tree.FindKeyIndex(80), 13)
        self.assertEqual(self.tree.FindKeyIndex(0), 7)
        self.assertEqual(self.tree.FindKeyIndex(17), None)
        self.assertEqual(self.tree.AddKey(18), 8)
        self.assertEqual(self.tree.AddKey(50), 0)


    def test_find_by_key(self) -> None:
        self.tre_arr: aBST = aBST(3)
        self.assertEqual(self.tree.AddKey(0), 0)
        self.tree.print_arr()
        print('st: ', self.tree is None)
        self.assertEqual(self.tree.AddKey(0), 0)








if __name__ == "__main__":
    unittest.main()
