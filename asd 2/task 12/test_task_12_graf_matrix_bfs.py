import unittest
from task_12_Graph_not_trian_vert import Vertex
from task_12_Graph_not_trian_vert import SimpleGraph


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.graph: SimpleGraph = SimpleGraph(9)
        self.graph.AddVertex(0)
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        self.graph.AddVertex(6)
        self.graph.AddVertex(7)
        self.graph.AddVertex(8)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)
        self.graph.AddEdge(3, 5)
        self.graph.AddEdge(4, 8)
        self.graph.AddEdge(8, 5)
        self.graph.AddEdge(8, 7)
        self.graph.AddEdge(7, 5)
        self.graph.AddEdge(5, 6)
        self.graph.AddEdge(6, 7)

    def test_search_not_triangle_vert(self):
        self.assertEqual(self.graph.return_vertex(), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.graph.convert_vert_list_to_value_list(self.graph.WeakVertices()), [0, 4])

    def test_remove_edge_end_find_not_triangle_vert(self):
        self.graph.RemoveEdge(2, 3)
        self.assertEqual(self.graph.convert_vert_list_to_value_list(self.graph.WeakVertices()), [0, 1, 2, 4])
    def test_empty_graf(self):
        self.graph2: SimpleGraph = SimpleGraph(0)
        self.assertEqual(self.graph.convert_vert_list_to_value_list(self.graph2.WeakVertices()), [])

if __name__ == "__main__":
    unittest.main()
