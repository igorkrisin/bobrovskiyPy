class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v: int) -> None:
        for i in range(0, len(self.vertex)):
            if self.vertex[i] is None:
                vert = Vertex(v)
                self.vertex[i] = vert
                break

    def RemoveVertex(self, v: int) -> None:
        self.vertex[v] = None
        for i in range(0, len(self.m_adjacency)):
            for j in range(0, len(self.m_adjacency[i])):
                if j == v:
                    self.m_adjacency[i][j] = 0
                    self.m_adjacency[j][i] = 0

    # v1 - begin, v2 - end
    def IsEdge(self, v1: int, v2: int) -> bool:
        if self.m_adjacency[v1][v2] == 1:
            return True
        return False

    def AddEdge(self, v1: int, v2: int) -> None:
        if v1 < len(self.m_adjacency[0]) and v2 < len(self.m_adjacency[0]):
            for i in range(0, len(self.m_adjacency)):
                for j in range(0, len(self.m_adjacency[i])):
                    if i == v1 and j == v2:
                        self.m_adjacency[i][j] = 1
                        self.m_adjacency[j][i] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if self.m_adjacency[v1][v2] == 1:
            self.m_adjacency[v1][v2] = 0

    def print_graph(self) -> None:
        for i in range(0, len(self.m_adjacency)):
            print(self.m_adjacency[i])
        print('----------')

    def print_vert(self):
        print('vertex: [', end=" ")
        for vertex in self.vertex:
            print(vertex.Value if vertex is not None else None, end=" ")

        print("]")

    def print_vert_hit(self):
        print('vertex: [', end=" ")
        for vertex in self.vertex:
            print(vertex.Hit if vertex is not None else None, end=" ")

        print("]")

    def return_graph(self):
        return self.m_adjacency

    def return_vertex(self) -> [Vertex]:
        result = []
        for vertex in self.vertex:
            if not vertex:
                result += [None]
            else:
                result += [vertex.Value]

        return result



    def return_vertex_hit(self) -> [Vertex]:
        result = []
        for vertex in self.vertex:
            if not vertex:
                result += [None]
            else:
                result += [vertex.Hit]

        return result

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> [Vertex]:
        pass

    def switching_visit_vertex_for_true(self) -> None:
        for vertex in self.vertex:
            vertex.Hit = False


graph: SimpleGraph = SimpleGraph(7)
graph.print_graph()
graph.AddVertex(0)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
graph.AddVertex(5)
graph.AddVertex(6)
graph.AddEdge(0, 1)
graph.AddEdge(0, 4)
graph.AddEdge(1, 2)
graph.AddEdge(1, 3)
graph.AddEdge(2, 3)
graph.AddEdge(3, 4)
graph.AddEdge(4, 5)
graph.AddEdge(5, 6)
graph.AddEdge(6, 0)
#graph.RemoveVertex(0)

graph.print_graph()
graph.print_vert()
graph.print_vert_hit()

