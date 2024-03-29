class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []

    def PrintNodesField(self) -> None:
        print('val: ', self.NodeValue)
        print('par: ', self.Parent.NodeValue)
        print('child: ', self.Children)


class SimpleTree:

    def __init__(self, root) -> None:
        self.Root = root

    def AddChild(self, ParentNode, NewChild) -> None:
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete) -> None:
        if NodeToDelete.Parent is None:
            return None
        if NodeToDelete in self.GetAllNodes():
            NodeToDelete.Parent.Children.remove(NodeToDelete)
        if NodeToDelete.Children:
            self.DeleteNode(NodeToDelete.Children[0])

    def GetAllNodes(self) -> [SimpleTreeNode]:
        chld_lst = self.Root
        result_lst = []
        if chld_lst.Parent is None:
            result_lst += [self.Root]
        if not chld_lst.Children:
            return result_lst
        for chld in chld_lst.Children:
            if chld_lst:
                result_lst += [chld]
            result_lst += SimpleTree(chld).GetAllNodes()
        return result_lst

    def FindNodesByValue(self, val: object) -> [SimpleTreeNode]:
        if val not in self.convert_lst_nodes_to_lst_val(self.GetAllNodes()):
            return []
        result_lst: [SimpleTreeNode] = []
        for val_chld in self.GetAllNodes():
            if val_chld.NodeValue == val:
                result_lst += [val_chld]
        return result_lst

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode) -> None:
        if not self.FindNodesByValue(OriginalNode.NodeValue):
            return None
        OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
        # NewParent.PrintNodesField()

    def Count(self):
        chld_lst = self.Root
        count = 0
        if chld_lst.Parent is None:
            count += 1
        if not chld_lst.Children:
            return count
        for chld in chld_lst.Children:
            if chld_lst:
                count += 1
            count += SimpleTree(chld).Count()
        return count

    def LeafCount(self):
        chld_lst = self.GetAllNodes()
        count = 0
        for child in chld_lst:
            if child.Children == []:
                count += 1
        return count

    def convert_lst_nodes_to_lst_val(self, lst: [object]) -> [object]:
        lst_summ = []
        for i in range(0, len(lst)):
            lst_summ.append(lst[i].NodeValue)
        return lst_summ

    def add_level_for_tree(self) -> [object]:
        chld_lst = self.Root
        result_lst = []
        level: int = 0
        if chld_lst.Parent is None:
            level += 1
            result_lst += [self.Root] + [f'level: {level}']
        if not chld_lst.Children:
            return result_lst
        for chld in chld_lst.Children:
            if chld_lst:
                result_lst += [chld] + [f'level: {level}']
            level += 1
            result_lst += SimpleTree(chld).GetAllNodes() + [f'level: {level}']
        return result_lst

    def EvenTrees(self) -> [SimpleTreeNode]:
        chld_lst = self.Root
        result_lst = []
        # if chld_lst.Parent is None:
        #     result_lst += [self.Root]
        if not chld_lst.Children:
            return result_lst
        for chld in chld_lst.Children:
            # print(chld.NodeValue)
            # print(chld.Children)
            if chld_lst and SimpleTree(chld).Count() % 2:
                result_lst.append(chld.Parent)
                result_lst.append(chld)

            SimpleTree(chld).EvenTrees()
        return result_lst

#
# root_node: SimpleTreeNode = SimpleTreeNode(1, None)
# second_node: SimpleTreeNode = SimpleTreeNode(2, root_node)
# third_node: SimpleTreeNode = SimpleTreeNode(3, root_node)
# fourth_node: SimpleTreeNode = SimpleTreeNode(4, third_node)
# fifth_node: SimpleTreeNode = SimpleTreeNode(5, second_node)
# sixth_node: SimpleTreeNode = SimpleTreeNode(6, root_node)
# seventh_node: SimpleTreeNode = SimpleTreeNode(7, second_node)
# eight_node: SimpleTreeNode = SimpleTreeNode(8, sixth_node)
# ninth_node: SimpleTreeNode = SimpleTreeNode(9, eight_node)
# tenth_node: SimpleTreeNode = SimpleTreeNode(10, eight_node)
#
#
# tree: SimpleTree = SimpleTree(root_node)
#
# tree.AddChild(root_node, second_node)
# tree.AddChild(root_node, third_node)
# tree.AddChild(root_node, sixth_node)
# tree.AddChild(sixth_node, eight_node)
# tree.AddChild(eight_node, ninth_node)
# tree.AddChild(eight_node, tenth_node)
# tree.AddChild(third_node, fourth_node)
# tree.AddChild(second_node, seventh_node)
# tree.AddChild(second_node, fifth_node)
#
# print(tree.convert_lst_nodes_to_lst_val(tree.EvenTrees()))
# print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))
# # tree.DeleteNode(fifth_node)
# fourth_node.PrintNodesField()
# tree.MoveNode(fourth_node, first_node)
# fourth_node.PrintNodesField()
# print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))
# print(tree.Count())
# print('leaf: ', tree.LeafCount())
# print(tree.add_level_for_tree())
# print('findByV: ',tree.convert_lst_nodes_to_lst_val(tree.FindNodesByValue(3)))

#
# for i in range(0, len(chld.Children)):
#             if i == len(chld.Children)-1:
#                 print(1)
#                 result_lst += (SimpleTree(chld[i].Children).GetAllNodes())
#             else:
#                 result_lst += chld
# if not chld_lst.Children:
#     print('\n')
#     print(11111111)
#     return result_lst
# temp_count: int = 0
# for chld in chld_lst.Children:
#     # print('cC: ', chld.NodeValue, 'Count: ', chld.Count)
#     for i in range(0, len(chld.Children)): print('chCH: ', chld.Children[i].NodeValue, end=' ')
#     if SimpleTree(chld).Count() >= 2 and SimpleTree(chld).Count() % 2 == 0 and chld.Children != []:
#         print(chld.NodeValue, SimpleTree(chld).Count())
#         print('ch.NV: ', chld.NodeValue)
#         print('par: ', chld.Parent.NodeValue)
#         result_lst.append(chld)
#         result_lst.append(chld.Parent)
#
#     result_lst += SimpleTree(chld).EvenTrees()
# print('RL: ', result_lst)
