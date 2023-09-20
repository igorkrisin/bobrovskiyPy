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
        return self.m_adjacency[v1][v2] == 1


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
        arr = []
        for i in range(0, len(self.m_adjacency)):
            arr.append(i)
        # print(arr, end=' ')
        print(f'\033[2;0;43m{arr}\033[0;0m')

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

    def switching_visit_vertex_for_false(self) -> None:
        for vertex in self.vertex:
            vertex.Hit = False

    def convert_vert_list_to_value_list(self, vert_list: [Vertex]) -> None:
        return [vertex.Value for vertex in vert_list]

    def get_all_not_visited_neighbors(self, v_from: int) -> [Vertex]:
        result = []
        if v_from < 0 or v_from > len(self.vertex):
            return []
        for i in range(0, len(self.m_adjacency[0])):

            if self.m_adjacency[v_from][i] == 1 and not self.vertex[i].Hit:
                result.append(self.vertex[i])
        return result

    def is_neighbours_not_visited_equal_v_to_(self, v_from, v_to: int) -> bool:
        if v_from < 0 or v_from > len(self.vertex) or v_to < 0 or v_to > len(self.vertex):
            return False
        return self.vertex[v_to] in self.get_all_not_visited_neighbors(v_from)

    def get_index_neighbours_equal_v_to(self, v_from, v_to) -> int:
        for i in range(0, len(self.get_all_not_visited_neighbors(v_from))):
            if self.vertex[v_to] == self.get_all_not_visited_neighbors(v_from)[i]:
                return self.vertex.index(self.vertex[v_to])

    def get_index_vertex(self, vert: Vertex):
        for i in range(0, len(self.vertex)):
            if vert == self.vertex[i]:
                return i

    def dfs(self, stack: [int], VFrom: int, VTo: int, ) -> [Vertex]:
        if VFrom < 0 or VFrom >= len(self.vertex) or VTo < 0 or VTo >= len(self.vertex):
            return []
        start_vert = VFrom
        self.vertex[start_vert].Hit = True
        stack.append(self.vertex[start_vert])
        if self.is_neighbours_not_visited_equal_v_to_(VFrom, VTo):
            stack.append(self.vertex[self.get_index_neighbours_equal_v_to(VFrom, VTo)])
            return stack
        for i in range(0, len(self.get_all_not_visited_neighbors(start_vert))):
            if stack[-1] == self.vertex[VTo]:
                return stack
            if self.get_all_not_visited_neighbors(start_vert):
                start_vert = self.vertex.index(self.get_all_not_visited_neighbors(start_vert)[0])
                self.dfs(stack, start_vert, VTo)
            if not self.get_all_not_visited_neighbors(start_vert):
                stack.pop()
                if not stack:
                    return []
                start_vert = self.vertex.index(stack[-1])
                self.vertex[start_vert].Hit = True
        return stack


    def DepthFirstSearch(self, VFrom: int, VTo: int) -> [Vertex]:
        self.switching_visit_vertex_for_false()
        simple_stack: [Vertex] = []
        return self.dfs(simple_stack, VFrom, VTo)

    def bfs(self, q: [Vertex], path: [Vertex], VFrom: int, VTo: int):
        pass


    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> [Vertex]:
        self.switching_visit_vertex_for_false()
        q: [Vertex] = []
        path: [Vertex] = []
        return self.bfs(q, path, VFrom, VTo)
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

#
# graph: SimpleGraph = SimpleGraph(7)
# # graph.print_graph()
# graph.AddVertex(0)
# graph.AddVertex(1)
# graph.AddVertex(2)
# graph.AddVertex(3)
# graph.AddVertex(4)
# graph.AddVertex(5)
# graph.AddVertex(6)
# graph.AddEdge(0, 1)
# graph.AddEdge(0, 4)
# graph.AddEdge(1, 2)
# graph.AddEdge(1, 3)
# graph.AddEdge(2, 3)
# graph.AddEdge(3, 4)
# graph.AddEdge(4, 5)
# graph.AddEdge(5, 6)
# graph.AddEdge(6, 0)
# # graph.RemoveVertex(0)
# #print(graph.dfs([], 3, 0))
# # graph.print_graph()
# #graph.print_vert()
# # graph.print_vert_hit()
# print('finish: ')
# graph.convert_vert_list_to_value_list(graph.DepthFirstSearch(4, 6))
#
# # for i in range(0, len(self.m_adjacency)):
# #     if self.m_adjacency[start_vert][i] == 1 and not self.vertex[i].Hit and self.vertex[i].Value != VTo:
# #         print('i: ', i)
# #         self.dfs(stack, i, VTo)
# # for i in range(0, len(self.m_adjacency)):
# #
# #     if self.m_adjacency[start_vert][i] == 1 and self.vertex[i].Hit and self.vertex[i].Value != VTo:
# #         # print('stack: ', self.convert_vert_list_to_value_list(stack))
# #         print('i2: ', i)
# #         print('pop: ', stack.pop(len(stack) - 1).Value)
# #         if not stack:
# #             return []
# #             # print(self.vertex.index(stack[len(stack) -1]))
# #         start_vert = self.vertex.index(stack[len(stack) - 1])
# #         print('SV: ', start_vert)
# #         self.vertex[start_vert].Hit = True
# #         self.dfs(stack, start_vert, VTo)
