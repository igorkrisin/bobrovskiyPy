class Vertex:

    def __init__(self, val):
        self.Value = val


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

        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex

        # здесь и далее, параметры v -- индекс вершины

    # в списке  vertex
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
        for i in range(0, len(self.m_adjacency)):
            for j in range(0, len(self.m_adjacency[i])):
                if i == v1 and j == v2:
                    self.m_adjacency[i][j] = 1
                    self.m_adjacency[j][i] = 1


    # добавление ребра между вершинами v1 и v2

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
            print(vertex.Value if vertex is not None else None,  end=" ")

        print("]")

    def return_graph(self):
        return


graph: SimpleGraph = SimpleGraph(3)
graph.print_graph()
graph.AddVertex(10)
graph.AddVertex(10)
graph.AddVertex(10)
graph.AddEdge(0, 0)
graph.AddEdge(0, 1)
graph.AddEdge(1, 2)
graph.AddEdge(1, 1)
graph.AddEdge(2, 2)
graph.RemoveVertex(0)


graph.print_graph()
graph.print_vert()

