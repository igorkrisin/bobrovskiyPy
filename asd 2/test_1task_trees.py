import unittest
from simple_trees_task_1 import SimpleTreeNode
from simple_trees_task_1 import SimpleTree


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.tree: SimpleTree = SimpleTree(self.root_node)

    def test_add_node_in_start(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.first_child_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.tree: SimpleTree = SimpleTree(self.root_node)
        self.tree.AddChild(self.root_node, self.first_child_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1, 2])
        self.second_child_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.root_node, self.second_child_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1, 2, 3])

    def test_delete_node(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.first_child_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.tree: SimpleTree = SimpleTree(self.root_node)
        self.tree.AddChild(self.root_node, self.first_child_node)
        self.second_child_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.root_node, self.second_child_node)
        self.tree.DeleteNode(self.first_child_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1, 3])
        self.tree.DeleteNode(self.root_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1, 3])
        self.tree.DeleteNode(self.second_child_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1])
        self.first_child_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.tree.AddChild(self.root_node, self.first_child_node)
        self.second_child_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.first_child_node, self.second_child_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1, 2, 3])
        self.tree.DeleteNode(self.first_child_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1])

    def test_get_all_nodes(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.first_child_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.tree: SimpleTree = SimpleTree(self.root_node)
        self.tree.AddChild(self.root_node, self.first_child_node)
        self.second_child_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.root_node, self.second_child_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1, 2, 3])

    def test_find_nodes_by_value(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.first_child_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.tree: SimpleTree = SimpleTree(self.root_node)
        self.tree.AddChild(self.root_node, self.first_child_node)
        self.second_child_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.root_node, self.second_child_node)
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.FindNodesByValue(3)), [3])
        self.third_child_node: SimpleTreeNode = SimpleTreeNode(3, self.second_child_node)
        self.tree.AddChild(self.second_child_node, self.third_child_node)
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.FindNodesByValue(3)), [3, 3])
        self.assertEqual(self.tree.FindNodesByValue(4), [])

    def test_find_nodes_by_none_root_value(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(None, None)
        self.tree: SimpleTree = SimpleTree(self.root_node)
        self.assertEqual(self.tree.convert_lst_nodes_to_lst_val(self.tree.FindNodesByValue(None)), [None])

    def test_moved_node(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.first_child_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.tree: SimpleTree = SimpleTree(self.root_node)
        self.tree.AddChild(self.root_node, self.first_child_node)
        self.second_child_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.first_child_node, self.second_child_node)
        self.third_child_node: SimpleTreeNode = SimpleTreeNode(4, self.root_node)
        self.tree.AddChild(self.second_child_node, self.third_child_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1, 2, 3, 4])
        self.tree.MoveNode(self.third_child_node, self.root_node)
        self.assertEqual(self.tree.GetAllNodesValue(), [1, 2, 4])

    def test_count(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.first_child_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.tree: SimpleTree = SimpleTree(self.root_node)
        self.tree.AddChild(self.root_node, self.first_child_node)
        self.second_child_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.first_child_node, self.second_child_node)
        self.third_child_node: SimpleTreeNode = SimpleTreeNode(4, self.root_node)
        self.tree.AddChild(self.second_child_node, self.third_child_node)
        self.assertEqual(self.tree.Count(), 4)

    def test_count_leaf(self) -> None:
        self.root_node: SimpleTreeNode = SimpleTreeNode(1, None)
        self.first_child_node: SimpleTreeNode = SimpleTreeNode(2, self.root_node)
        self.tree: SimpleTree = SimpleTree(self.root_node)
        self.tree.AddChild(self.root_node, self.first_child_node)
        self.second_child_node: SimpleTreeNode = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.first_child_node, self.second_child_node)
        self.third_child_node: SimpleTreeNode = SimpleTreeNode(4, self.root_node)
        self.tree.AddChild(self.second_child_node, self.third_child_node)
        self.assertEqual(self.tree.LeafCount(), 1)
        self.fourth_child_node: SimpleTreeNode = SimpleTreeNode(5, self.root_node)
        self.tree.AddChild(self.second_child_node, self.fourth_child_node)
        self.assertEqual(self.tree.LeafCount(), 2)



if __name__ == "__main__":
    unittest.main()
