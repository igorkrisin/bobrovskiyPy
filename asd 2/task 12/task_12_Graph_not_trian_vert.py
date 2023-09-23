class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
        self.Parent = None


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
        # print('self.m_adjacency[v1][v2]: ', self.m_adjacency[v1][v2])
        if self.m_adjacency[v1][v2] == 1:
            self.m_adjacency[v1][v2] = 0
        if self.m_adjacency[v2][v1] == 1:
            self.m_adjacency[v2][v1] = 0
            # print('self.m_adjacency[v1][v2]2: ', self.m_adjacency[v1][v2])

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

    def print_parent(self):
        result = []
        for i in range(0, len(self.vertex)):
            result += [self.vertex[i].Parent if not self.vertex[i].Parent else self.vertex[i].Parent.Value]
        print(result)

    def get_one_neighbor_not_visited_vertex(self, VTo: int):
        for i in range(0, len(self.vertex)):
            if self.IsEdge(VTo, i) and not self.vertex[i].Hit:
                return self.vertex[i]

    def list_have_not_visited_neighbors(self):
        result = []
        for vert in self.vertex:
            if not vert.Hit:
                result += [vert]
        return result

    def switch_all_not_visited(self) -> None:
        for vert in self.vertex:
            vert.Hit = False

    def switch_all_parent_is_none(self) -> None:
        for vert in self.vertex:
            vert.Parent = None

    def bild_path(self, finish_vert: int, start_vert: int) -> [Vertex]:
        self.switch_all_not_visited()
        # print('not_vis: ', self.list_have_not_visited_neighbors())
        # print('fv:: ', finish_vert)
        # print('start_vert: ', start_vert)
        parent = self.vertex[finish_vert].Parent
        # print('parent: ', parent.Value)
        # print('self.vertex[start_vert]: ', self.vertex[start_vert].Value)
        result = []
        result.append(self.vertex[finish_vert])
        self.vertex[finish_vert].Hit = True
        if self.vertex[finish_vert].Parent == self.vertex[start_vert]:
            # print(11111111)
            result = [self.vertex[start_vert]] + result
            return result
        # print('par app2: ', self.vertex[finish_vert].Value)
        while parent and not parent.Hit:
            result = [parent] + result
            parent.Hit = True
            # print('prent app: ', self.convert_vert_list_to_value_list(result))
            # print('par3: ', parent.Value)
            parent = parent.Parent

        # print('self.vertex[start_vert]: ', self.vertex[start_vert].Value)
        # print('parent: ', (self.vertex[finish_vert].Value))

        return result

    def bfs(self, q: [Vertex], VFrom: int, VTo: int):

        start_vert: Vertex = self.vertex[VFrom]
        start_vert.Hit = True
        finish_vert = VFrom
        # q.append(start_vert)
        while self.list_have_not_visited_neighbors():

            list_all_neighbors = self.get_all_not_visited_neighbors(finish_vert)
            for vert in list_all_neighbors:
                vert.Parent = self.vertex[finish_vert]
                q.append(vert)
                vert.Hit = True
                if vert == self.vertex[VTo]:
                    vert.Parent = self.vertex[finish_vert]
                    # print("VFrom: ", VFrom)
                    # print("VTo: ", VTo)
                    # print('QQQ: ', self.convert_vert_list_to_value_list(q))
                    return self.bild_path(VTo, VFrom)
            # print('Q: ', self.convert_vert_list_to_value_list(q))
            if q:

                finish_vert = self.get_index_vertex(q.pop(0))
            else:
                return []

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> [Vertex]:
        if VFrom < 0 or VFrom >= len(self.vertex) or VTo < 0 or VTo >= len(self.vertex):
            return []
        self.switch_all_parent_is_none()
        self.switching_visit_vertex_for_false()
        self.switch_all_not_visited()
        q: [Vertex] = []
        return self.bfs(q, VFrom, VTo)

    def get_all_vert_neighbors(self, vert: int) -> [int]:
        result = []
        if vert < 0 or vert > len(self.vertex):
            return []
        for i in range(0, len(self.m_adjacency[0])):
            # print('vert: ', self.vertex[i].Value)
            if self.m_adjacency[vert][i] == 1:
                result.append(self.vertex[i])
        return result

    def is_edge_only_one(self, vert: int) -> bool:
        if len(self.get_all_vert_neighbors(vert)) > 1:
            return False
        return True

    def is_vertex_neighbors_not_connect(self, vert: Vertex) -> bool:
        # print('vert: ', vert.Value)
        list_neighbor: [Vertex] = self.get_all_vert_neighbors(self.get_index_vertex(vert))
        # print('list_neighbor: ', self.convert_vert_list_to_value_list(list_neighbor))
        for i in range(0, len(list_neighbor)):
            # print('list_neighbor[i]: ', list_neighbor[i].Value)
            if i+1 >= len(list_neighbor):
                # print('break: ')
                break
            if self.IsEdge(self.get_index_vertex(list_neighbor[i]), self.get_index_vertex(list_neighbor[i+1])):
                # print('neighb1: ', list_neighbor[i].Value, 'neighb2: ', list_neighbor[i+1].Value)
                return False
        # print('True')
        return True



    #TODO проверить корректность удаления, после удаления некорректный граф

    #проверить есть ли ребра среди ее соседей, если есть хотя бы у одного
    #бeрeм следующую непосещунную верщину. помечаем ее посешенной и смотрим ребра ее соседей
    #если ребра нет -  добавдяем в список элемент
    #и так пока все вершины не будут посещены


    def WeakVertices(self) -> [Vertex]:
        #self.switch_all_not_visited()
        #self.switching_visit_vertex_for_false()
        #self.switch_all_parent_is_none()
        result: [Vertex] = []
        for vert in self.vertex:
            if self.is_edge_only_one(self.get_index_vertex(vert)):
                result.append(vert)
            elif self.is_vertex_neighbors_not_connect(vert):
                result.append(vert)
        return result


graph: SimpleGraph = SimpleGraph(2)
graph.AddVertex(0)
graph.AddVertex(1)
# graph.AddVertex(2)
# graph.AddVertex(3)
# graph.AddVertex(4)
# graph.AddVertex(5)
# graph.AddVertex(6)
# graph.AddVertex(7)
# graph.AddVertex(8)
# graph.AddEdge(0, 1)
# graph.AddEdge(1, 2)
# graph.AddEdge(1, 3)
# graph.AddEdge(2, 3)
# graph.AddEdge(3, 4)
# graph.AddEdge(3, 5)
# graph.AddEdge(4, 8)
# graph.AddEdge(8, 5)
# graph.AddEdge(8, 7)
# graph.AddEdge(7, 5)
# graph.AddEdge(5, 6)
# graph.AddEdge(6, 7)
graph.print_graph()
# graph.RemoveEdge(0, 1)
#graph.RemoveEdge(7, 5)
# graph.RemoveEdge(2, 3)
# graph.print_graph()
print(graph.convert_vert_list_to_value_list(graph.WeakVertices()))
# #
# graph: SimpleGraph = SimpleGraph(7)
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
#
# #graph.print_parent()
# graph.RemoveEdge(6, 0)
# print('neighb: ', graph.convert_vert_list_to_value_list(graph.get_all_vert_neighbors(2)))
# print('only_one_neighb: ', graph.is_edge_only_one(6))
# print('WeakVertices: ', graph.convert_vert_list_to_value_list(graph.WeakVertices()))
# # graph.vertex[0].Hit = True
#print(graph.convert_vert_list_to_value_list(graph.is_have_not_visited_neighbors()))
# print(graph.bild_path(0, 3))
#print('list path: ', graph.convert_vert_list_to_value_list(graph.BreadthFirstSearch(1, 5)))
#
# for i in range(0, len(self.m_adjacency)):
#     if self.m_adjacency[start_vert][i] == 1 and not self.vertex[i].Hit and self.vertex[i].Value != VTo:
#         print('i: ', i)
#         self.dfs(stack, i, VTo)
# for i in range(0, len(self.m_adjacency)):
#
#     if self.m_adjacency[start_vert][i] == 1 and self.vertex[i].Hit and self.vertex[i].Value != VTo:
#         # print('stack: ', self.convert_vert_list_to_value_list(stack))
#         print('i2: ', i)
#         print('pop: ', stack.pop(len(stack) - 1).Value)
#         if not stack:
#             return []
#             # print(self.vertex.index(stack[len(stack) -1]))
#         start_vert = self.vertex.index(stack[len(stack) - 1])
#         print('SV: ', start_vert)
#         self.vertex[start_vert].Hit = True
#         self.dfs(stack, start_vert, VTo)
