import unittest
from task_8_Graph_matrix import Vertex
from task_8_Graph_matrix import SimpleGraph


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = SimpleGraph(4)
        self.graph.AddEdge(0, 1)

    def test_add_vertex(self):
        self.graph.AddEdge(0, 2)




if __name__ == "__main__":
    unittest.main()
