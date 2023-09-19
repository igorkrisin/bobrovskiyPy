import unittest
from task_10_Graph_matrix import Vertex
from task_10_Graph_matrix import SimpleGraph


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.graph: SimpleGraph = SimpleGraph(7)
        self.graph.AddVertex(0)
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        self.graph.AddVertex(6)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 4)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)
        self.graph.AddEdge(4, 5)
        self.graph.AddEdge(5, 6)
        self.graph.AddEdge(6, 0)

    def test_search_path_for_vert(self):
        self.assertEqual(self.graph.return_vertex(), [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(self.graph.convert_vert_list_to_value_list(self.graph.DepthFirstSearch(0, 4)), [0, 4])
        self.assertEqual(self.graph.convert_vert_list_to_value_list(self.graph.DepthFirstSearch(2, 6)), [2, 1, 0, 6])


if __name__ == "__main__":
    unittest.main()
