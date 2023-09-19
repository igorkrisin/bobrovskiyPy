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
        if not vert_list:
            print('vert is None')
        else:
            for vert in vert_list:
                print(vert if vert is None else vert.Value, end=' ')



    # def dfs2(self, stack: [Vertex], VFrom: int, VTo: int) -> [Vertex]:
    #     start_vert: int = VFrom
    #     #next_ver: int = VFrom + 1
    #     # print('sV: :', start_vert)
    #     # print('nV: ', next_ver)
    #     self.vertex[VFrom].Hit = True
    #     # self.print_vert_hit()
    #     stack.append(self.vertex[VFrom])  # убрать поле Value!!!!!!!
    #     # print(stack)
    #     for i in range(0, len(self.m_adjacency)):
    #         #print('self.vertex[i]: ', self.vertex[i].Value)
    #         if self.m_adjacency[start_vert][i] == 1 and not self.vertex[i].Hit and self.vertex[i].Value == VTo:
    #             # print(1111)
    #             stack.append(self.vertex[i])
    #             return stack
    #     for i in range(0, len(self.m_adjacency)):
    #         if self.m_adjacency[start_vert][i] == 1 and not self.vertex[i].Hit and self.vertex[i].Value != VTo:
    #             print('i: ', i)
    #             self.dfs(stack, i, VTo)
    #     for i in range(0, len(self.m_adjacency)):
    #
    #         if self.m_adjacency[start_vert][i] == 1 and self.vertex[i].Hit and self.vertex[i].Value != VTo:
    #                 # print('stack: ', self.convert_vert_list_to_value_list(stack))
    #             print('i2: ', i)
    #             print('pop: ', stack.pop(len(stack) - 1).Value)
    #             if not stack:
    #                 return []
    #                 #print(self.vertex.index(stack[len(stack) -1]))
    #             start_vert = self.vertex.index(stack[len(stack) -1])
    #             print('SV: ', start_vert)
    #             self.vertex[start_vert].Hit = True
    #             self.dfs(stack, start_vert, VTo)
    #
    #     return stack

    # def dfs(self, stack: [Vertex], VFrom: int, VTo: int) -> [Vertex]:
    #     start_vert: int = VFrom
    #     #next_ver: int = VFrom + 1
    #     # print('sV: :', start_vert)
    #     # print('nV: ', next_ver)
    #     self.vertex[VFrom].Hit = True
    #     # self.print_vert_hit()
    #     stack.append(self.vertex[VFrom])  # убрать поле Value!!!!!!!
    #     # print(stack)
    #     i: int = 0
    #     while stack:
    #         if self.m_adjacency[start_vert][i] == 1 and not self.vertex[i].Hit and self.vertex[i].Value == VTo:
    #                 # print(1111)
    #                 stack.append(self.vertex[i])
    #                 return stack
    #         #print('search_ind: ', self.search_index_not_visited_node(self.m_adjacency[start_vert]))
    #         i += 1
    #
    # def search_index_not_visited_node(self, vert: int):
    #     for i in range(0, len(self.m_adjacency[0])):
    #         if self.m_adjacency[vert][i] == 1:
    #             pass

    def get_all_not_visited_neighbors(self, v_from: int) -> [Vertex]:
        result = []
        if v_from < 0 or v_from > len(self.vertex):
            return []
        for i in range(0, len(self.m_adjacency[0])):
            if self.m_adjacency[v_from][i] == 1 and not self.vertex[i].Hit:
                result.append(self.vertex[i])
        return result

    def is_neighbours_equal_v_to(self, v_from,  v_to: int) -> bool:
        if v_from < 0 or v_from > len(self.vertex) or v_to < 0 or v_to > len(self.vertex):
            return False
        return self.vertex[v_to] in self.get_all_not_visited_neighbors(v_from)

    def get_index_neighbours_equal_v_to(self, v_from, v_to) -> int:
        for i in range(0, len(self.get_all_not_visited_neighbors(v_from))):
            if self.vertex[v_to] == self.get_all_not_visited_neighbors(v_from)[i]:
                return self.vertex.index(self.vertex[v_to])


    def dfs(self,   stack: [int], VFrom: int, VTo: int, ) -> [Vertex]:
        if VFrom < 0 or VFrom > len(self.vertex)-1 or VTo < 0 or VTo > len(self.vertex)-1:
            return []
        print('vFrom0:', self.vertex[VFrom].Value)
        self.vertex[VFrom].Hit = True
        stack.append(self.vertex[VFrom])
        for i in range(0, len(self.vertex)):
            #self.print_vert_hit()
            #self.print_vert()
            if self.is_neighbours_equal_v_to(VFrom, VTo):
                print('self.get_index_neighbours_equal_v_to(VFrom, VTo): ', self.get_index_neighbours_equal_v_to(VFrom, VTo))
                stack.append(self.vertex[self.get_index_neighbours_equal_v_to(VFrom, VTo)])
                return stack

            if self.m_adjacency[VFrom][i] == 1 and not self.vertex[i].Hit and self.vertex[i].Value != VTo:
                print('i: ', i)
                VFrom = i
                print('vFrom:', self.vertex[VFrom].Value)
                self.dfs(stack, i, VTo)
            if self.m_adjacency[VFrom][i] == 1 and self.vertex[i].Hit:
                #print('stack: ', self.convert_vert_list_to_value_list(stack))
                stack.pop()
                #print('stack2: ', self.convert_vert_list_to_value_list(stack))
                if not stack:
                    return []
                VFrom = stack.index(stack[-1])
                #print('vFrom:', self.vertex[VFrom].Value )
                self.vertex[VFrom].Hit = True

                #self.dfs(stack, VFrom, VTo)
        return stack



    def DepthFirstSearch(self, VFrom: int, VTo: int) -> [Vertex]:
        self.switching_visit_vertex_for_false()
        simple_stack: [Vertex] = []
        return self.dfs(simple_stack, VFrom, VTo)


graph: SimpleGraph = SimpleGraph(7)
# graph.print_graph()
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
# graph.RemoveVertex(0)
#print(graph.dfs([], 3, 0))
# graph.print_graph()
#graph.print_vert()
# graph.print_vert_hit()

graph.convert_vert_list_to_value_list(graph.DepthFirstSearch(2,6))

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