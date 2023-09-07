import unittest
from task_6_BTFNode import BSTNode
from task_6_BTFNode import BalancedBST


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.tree: BalancedBST = BalancedBST()
        self.node: BSTNode = BSTNode(10, None)
        self.tree.Root = self.node

    def test_generate_tree(self) -> None:
        self.arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(self.tree.GenerateTreeReturn(self.arr), [4, 2, 6, 1, 3, 5, 7])


if __name__ == "__main__":
    unittest.main()
