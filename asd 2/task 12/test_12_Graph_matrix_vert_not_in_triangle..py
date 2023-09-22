import unittest
# from task_12_Graph_matrix_vert_not_in_triangle import Vertex
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
        self.graph.AddEdge(5, 8)
        self.graph.AddEdge(4, 8)
        self.graph.AddEdge(5, 7)
        self.graph.AddEdge(7, 8)
        self.graph.AddEdge(7, 6)
        self.graph.AddEdge(6, 5)

    # def test_search_path_for_vert(self):
    #     print(111111111)
    #     self.assertEqual(self.graph.return_vertex(), [0, 1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == "__main__":
    unittest.main()
