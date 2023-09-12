import unittest
from task_8_Graph_matrix import Vertex
from task_8_Graph_matrix import SimpleGraph


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = SimpleGraph(4)
        self.graph.AddEdge(0, 1)
        self.assertEqual(self.graph.return_graph(), [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_add_edge(self):
        self.graph.AddEdge(0, 2)
        self.assertEqual(self.graph.return_graph(), [[0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]])

    def test_add_vertex(self):
        self.empty_graph = SimpleGraph(5)
        self.assertEqual(self.empty_graph.return_graph(),
                         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self.assertEqual(self.empty_graph.return_vertex(), [None, None, None, None, None])
        self.empty_graph.AddVertex(4)
        self.assertEqual(self.empty_graph.return_vertex(), [4, None, None, None, None])
        self.assertEqual(self.empty_graph.return_graph(),
                         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self.empty_graph.AddVertex(10)
        self.assertEqual(self.empty_graph.return_vertex(), [4, 10, None, None, None])
        self.assertEqual(self.empty_graph.return_graph(),
                         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_add_edge_2(self):
        self.graph = SimpleGraph(4)
        self.assertEqual(self.graph.return_graph(), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.graph.AddEdge(2, 3)
        self.assertEqual(self.graph.return_vertex(), [None, None, None, None])
        self.assertEqual(self.graph.return_graph(), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

    def test_remove_edge(self):
        self.graph = SimpleGraph(4)
        self.assertEqual(self.graph.return_graph(), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.graph.AddEdge(2, 3)
        self.assertEqual(self.graph.return_vertex(), [None, None, None, None])
        self.assertEqual(self.graph.return_graph(), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        self.graph.RemoveEdge(2,3)
        self.assertEqual(self.graph.return_vertex(), [None, None, None, None])

    def test_remove_vertex(self):
        self.graph = SimpleGraph(4)
        self.assertEqual(self.graph.return_graph(), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.graph.AddVertex(3)
        self.assertEqual(self.graph.return_vertex(), [3, None, None, None])
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.assertEqual(self.graph.return_graph(), [[0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]])
        self.graph.RemoveVertex(0)
        self.assertEqual(self.graph.return_graph(), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(self.graph.return_vertex(), [None, None, None, None])


if __name__ == "__main__":
    unittest.main()
