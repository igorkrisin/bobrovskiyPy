import unittest
from binary_trees_task_2 import BST
from binary_trees_task_2 import BSTNode
from binary_trees_task_2 import BSTFind


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.root_node: BSTNode = BSTNode(0, 2, None)
        self.tree: BST = BST(self.root_node)

    def test_find_by_key(self) -> None:
        self.root_node: BSTNode = BSTNode(7, 2, None)
        self.v = [6, 8, 5, 9, 10, 23, 44, 11, 3, 2]
        self.tree: BST = BST(self.root_node)
        self.tree.create_tree(self.v, 10, self.tree)
        self.assertEqual(self.tree.convert_find_node(self.tree.FindNodeByKey(5)), [5, True, False])
        self.assertEqual(self.tree.convert_find_node(self.tree.FindNodeByKey(12)), [11, False, False])
        self.assertEqual(self.tree.convert_find_node(self.tree.FindNodeByKey(1)), [3, False, True])
        self.root_node2: BSTNode = BSTNode(7, 2, None)
        self.tree2: BST = BST(self.root_node2)
        self.tree2.create_tree(self.v, 1, self.tree)
        self.assertEqual(self.tree2.convert_find_node(self.tree2.FindNodeByKey(12)), [7, False, False])
        self.root_node3: BSTNode = BSTNode(7, 2, None)
        self.tree3: BST = BST(self.root_node3)
        self.tree3.create_tree(self.v, 0, self.tree)
        self.assertEqual(self.tree3.convert_find_node(self.tree3.FindNodeByKey(12)), [7, False, False])

    def test_add_node(self) -> None:
        self.root_node: BSTNode = BSTNode(7, 2, None)
        self.v = [6, 8, 5, 9, 10, 23, 44, 11, 3, 2]
        self.tree: BST = BST(self.root_node)
        self.tree.create_tree(self.v, 10, self.tree)
        self.assertEqual(self.tree.AddKeyValue(5, 0), False)
        self.assertEqual(self.tree.convert_find_node(self.tree.FindNodeByKey(4)), [3, False, False])
        self.tree.AddKeyValue(4, 4)
        self.assertEqual(self.tree.convert_find_node(self.tree.FindNodeByKey(4)), [4, True, False])
        self.assertEqual(self.tree.convert_find_node(self.tree.FindNodeByKey(12)), [11, False, False])
        self.tree.AddKeyValue(12, 4)
        self.assertEqual(self.tree.convert_find_node(self.tree.FindNodeByKey(12)), [12, True, False])
        self.assertEqual(self.tree.Count(), 12)
        self.tree.AddKeyValue(23, 0)
        self.assertEqual(self.tree.Count(), 12)

    def test_delete_node(self) -> None:
        self.root_node: BSTNode = BSTNode(7, 2, None)
        self.v = [6, 8, 5, 9, 10, 23, 44, 11, 3, 2]
        self.tree: BST = BST(self.root_node)
        self.tree.create_tree(self.v, 0, self.tree)
        self.tree.DeleteNodeByKey(7)
        self.assertEqual(self.tree.convert_find_node(self.tree.FindNodeByKey(7)), [7, True, False])




if __name__ == "__main__":
    unittest.main()
