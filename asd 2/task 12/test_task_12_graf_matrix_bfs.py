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
        self.assertEqual(self.graph.convert_vert_list_to_value_list(self.graph.WeakVertices()), [0, 1, 2, 3, 4])
        self.graph.RemoveEdge(7, 5)
        self.assertEqual(self.graph.convert_vert_list_to_value_list(self.graph.WeakVertices()),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_empty_graf(self):
        self.graph2: SimpleGraph = SimpleGraph(0)
        self.assertEqual(self.graph.convert_vert_list_to_value_list(self.graph2.WeakVertices()), [])

    def test_graf_with_one_vertex(self):
        self.graph3: SimpleGraph = SimpleGraph(2)
        self.graph3.AddVertex(0)
        self.graph3.AddVertex(1)
        self.assertEqual(self.graph3.convert_vert_list_to_value_list(self.graph3.WeakVertices()), [0, 1])
        self.graph3.RemoveVertex(1)
        self.graph3.AddVertex(3)
        # self.graph3.print_graph()
        self.assertEqual(self.graph3.convert_vert_list_to_value_list(self.graph3.WeakVertices()), [0, 3])
        self.graph3.AddVertex(4)

    def test_two_triangle(self):
        self.graph4: SimpleGraph = SimpleGraph(6)
        self.graph4.AddVertex(0)
        self.graph4.AddVertex(1)
        self.graph4.AddVertex(2)
        self.graph4.AddVertex(3)
        self.graph4.AddVertex(4)
        self.graph4.AddVertex(5)
        self.graph4.AddEdge(0, 1)
        self.graph4.AddEdge(0, 2)
        self.assertEqual(self.graph4.convert_vert_list_to_value_list(self.graph4.WeakVertices()), [0, 1, 2, 3, 4, 5])
        self.graph4.AddEdge(1, 2)
        self.assertEqual(self.graph4.convert_vert_list_to_value_list(self.graph4.WeakVertices()), [3, 4, 5])
        self.graph4.AddEdge(2, 3)
        self.graph4.AddEdge(2, 4)
        self.assertEqual(self.graph4.convert_vert_list_to_value_list(self.graph4.WeakVertices()), [3, 4, 5])
        self.graph4.AddEdge(3, 4)
        self.assertEqual(self.graph4.convert_vert_list_to_value_list(self.graph4.WeakVertices()), [5])
        self.graph4.AddEdge(3, 5)
        self.assertEqual(self.graph4.convert_vert_list_to_value_list(self.graph4.WeakVertices()), [5])
        self.graph4.AddEdge(4, 5)
        self.assertEqual(self.graph4.convert_vert_list_to_value_list(self.graph4.WeakVertices()), [])

    def test_circle(self):
        self.graph5: SimpleGraph = SimpleGraph(7)
        self.graph5.AddVertex(0)
        self.graph5.AddVertex(1)
        self.graph5.AddVertex(2)
        self.graph5.AddVertex(3)
        self.graph5.AddVertex(4)
        self.graph5.AddVertex(5)
        self.graph5.AddVertex(6)
        self.graph5.AddEdge(0, 1)
        self.graph5.AddEdge(0, 4)
        self.graph5.AddEdge(0, 6)
        self.graph5.AddEdge(1, 2)
        self.graph5.AddEdge(1, 3)
        self.graph5.AddEdge(2, 3)
        self.graph5.AddEdge(3, 4)
        self.graph5.AddEdge(4, 5)
        self.graph5.AddEdge(5, 6)

        self.assertEqual(self.graph5.convert_vert_list_to_value_list(self.graph5.WeakVertices()), [0, 4, 5, 6])
        self.graph5.AddEdge(6, 1)
        self.assertEqual(self.graph5.convert_vert_list_to_value_list(self.graph5.WeakVertices()), [4, 5])
        self.graph5.AddEdge(5, 3)
        self.assertEqual(self.graph5.convert_vert_list_to_value_list(self.graph5.WeakVertices()), [])


if __name__ == "__main__":
    unittest.main()
