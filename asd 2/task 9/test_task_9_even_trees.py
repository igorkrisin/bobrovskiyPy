import unittest
from task_9_even_trees import SimpleTree
from task_9_even_trees import SimpleTreeNode


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.second_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.third_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.fourth_node: SimpleTreeNode = SimpleTreeNode(4, self.third_node)
        self.fifth_node: SimpleTreeNode = SimpleTreeNode(5, self.second_node)
        self.sixth_node: SimpleTreeNode = SimpleTreeNode(6, self.root_node)
        self.seventh_node: SimpleTreeNode = SimpleTreeNode(7, self.second_node)
        self.eight_node: SimpleTreeNode = SimpleTreeNode(8, self.sixth_node)
        self.ninth_node: SimpleTreeNode = SimpleTreeNode(9, self.eight_node)
        self.tenth_node: SimpleTreeNode = SimpleTreeNode(10, self.eight_node)

        self.tree: SimpleTree = SimpleTree(self.root_node)

        self.tree.AddChild(self.root_node, self.second_node)
        self.tree.AddChild(self.root_node, self.third_node)
        self.tree.AddChild(self.root_node, self.sixth_node)
        self.tree.AddChild(self.sixth_node, self.eight_node)
        self.tree.AddChild(self.eight_node, self.ninth_node)
        self.tree.AddChild(self.eight_node, self.tenth_node)
        self.tree.AddChild(self.third_node, self.fourth_node)
        self.tree.AddChild(self.second_node, self.seventh_node)
        self.tree.AddChild(self.second_node, self.fifth_node)

    def test_check_tree(self):
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.GetAllNodes()),
                         [1, 2, 7, 5, 3, 4, 6, 8, 9, 10])

    def test_even_tree_check_return_value(self):
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.EvenTrees()), [1, 3, 1, 6])
        self.eleventh_node = SimpleTreeNode(11, self.seventh_node)
        self.tree.AddChild(self.seventh_node, self.eleventh_node)
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.EvenTrees()), [1, 2, 1, 3, 1, 6])
        self.twelth_node = SimpleTreeNode(12, self.fourth_node)
        self.tree.AddChild(self.fourth_node, self.twelth_node)
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.EvenTrees()), [1, 2, 1, 6])
        self.tree.DeleteNode(self.twelth_node)
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.EvenTrees()), [1, 2, 1, 3, 1, 6])
        self.tree.DeleteNode(self.second_node)
        self.tree.DeleteNode(self.third_node)
        self.tree.DeleteNode(self.sixth_node)
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.GetAllNodes()),
                         [1])
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.EvenTrees()), [])
        self.tree.DeleteNode(self.root_node)
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.GetAllNodes()),
                         [1])




if __name__ == "__main__":
    unittest.main()
