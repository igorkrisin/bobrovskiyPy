class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []

    def print_tree_nodes(self):
        print('node_val: ', self.NodeValue)
        print('parent: ', self.Parent)
        print('children: ', self.Children)
        print('       ')


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode) -> None:
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode) -> None:
        if NodeToDelete.Parent is None:
            return None
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        if NodeToDelete.Children:
            self.DeleteNode(NodeToDelete.Children[0])

    def GetAllNodes(self) -> [SimpleTreeNode]:
        child: SimpleTreeNode = self.Root.Children
        i = 0
        if len(child) == 0:
            return [self.Root]
        lst: [SimpleTreeNode] = []
        lst.append(self.Root)
        while len(child) != 0:
            for y in range(0, len(child)):
                lst.append(child[y])
            if i == len(child):
                i = 0
            child = child[i].Children
            i += 1

        return lst

    def GetAllNodesRecur(self) -> [SimpleTreeNode]:
        child: SimpleTreeNode = self.Root.Children
        if not self.Root.Children:
            return [self.Root]
        lst = [self.Root]
        for i in range(0, len(child)):
            if len(child[i].Children) != 0:
                lst.append(child[i])
                child = child[i].Children
                lst += self.GetAllNodesRecur()
        return lst


    def FindNodesByValue(self, val: int) -> [SimpleTreeNode]:
        if self.Root is None:
            return []
        if len(self.Root.Children) == 0 and self.Root.NodeValue != val:
            return []
        elif len(self.Root.Children) == 0 and self.Root.NodeValue == val:
            return [self.Root]
        child_lst: SimpleTreeNode = self.Root.Children
        summ_list_value: [SimpleTreeNode] = []
        if self.Root.NodeValue == val:
            summ_list_value.append(self.Root)
        while len(child_lst) != 0:
            for i in range(0, len(child_lst)):
                if val == child_lst[i].NodeValue:
                    summ_list_value.append(child_lst[i])
            child_lst = child_lst[i].Children
        return summ_list_value


    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode) -> None:
        for i in range(0, len(OriginalNode.Parent.Children)):
            if OriginalNode == OriginalNode.Parent.Children[i]:
                OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self) -> int:
        child_lst = self.Root.Children
        count_nodes = 1

        if not child_lst:
            return count_nodes
        for i in range(0, len(child_lst)):
            count_nodes += 1
            if i == len(child_lst)-1:
                count_nodes += self.Root.Count()

        return count_nodes

    def LeafCount(self) -> int:
        lst_nodes: [object] = self.GetAllNodes()
        count = 0
        for i in range(0, len(lst_nodes)):
            if not lst_nodes[i].Children:
                count += 1
        return count

    def GetAllNodesValue(self) -> [object]:
        child: SimpleTreeNode = self.Root.Children
        if len(child) == 0:
            return [self.Root.NodeValue]
        lst: [object] = [] + [self.Root.NodeValue]
        while len(child) != 0:
            for i in range(0, len(child)):
                lst.append(child[i].NodeValue)
            child = child[i].Children
        return lst

    def convert_lst_nodes_to_lst_val(self, lst: [object]) -> [object]:
        lst_summ = []
        for i in range(0, len(lst)):
            lst_summ.append(lst[i].NodeValue)
        return lst_summ

    def add_level_for_tree(self) -> [object]:
        level: int = 0
        child: SimpleTreeNode = self.Root.Children
        if len(child) == 0:
            return [self.Root.NodeValue]
        lst: [object] = [] + [self.Root.NodeValue]
        while len(child) != 0:
            for i in range(0, len(child)):
                lst.append(child[i].NodeValue)
            child = child[i].Children
        return lst




root_node: SimpleTreeNode = SimpleTreeNode(1, None)
first_child_node: SimpleTreeNode = SimpleTreeNode(2, root_node)

tree: SimpleTree = SimpleTree(root_node)
#print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))
tree.AddChild(root_node, first_child_node)
fifth_child: SimpleTreeNode = SimpleTreeNode(3, root_node)
tree.AddChild(fifth_child, fifth_child)
#print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))
second_child_node: SimpleTreeNode = SimpleTreeNode(4, root_node)
tree.AddChild(root_node, second_child_node)
#print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))
third_node: SimpleTreeNode = SimpleTreeNode(5, second_child_node)
tree.AddChild(second_child_node, third_node)
#print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))

print(tree.Count())
#print(tree.GetAllNodes())
#print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))
#print('find: ', tree.FindNodesByValue(3))

#second_child_node.print_tree_nodes()
#third_node.print_tree_nodes()

#print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodesRecur()))



'''parent_node: SimpleTreeNode = SimpleTreeNode('Parnt', None)
child_node: SimpleTreeNode = SimpleTreeNode('CHILD_NODE', parent_node)
new_child_node: SimpleTreeNode = SimpleTreeNode('NEW_CHILD_NODE', child_node)
new_child_node2: SimpleTreeNode = SimpleTreeNode('Parent', child_node)
new_child_node3: SimpleTreeNode = SimpleTreeNode('new_child_node3', child_node)
new_child_node4: SimpleTreeNode = SimpleTreeNode('Parent', child_node)
new_child_node5: SimpleTreeNode = SimpleTreeNode('NEW_CHILD_NODE5', child_node)
new_child_node6: SimpleTreeNode = SimpleTreeNode('Parent', child_node)

first_tree: SimpleTree = SimpleTree(parent_node)
first_tree.AddChild(parent_node, child_node)
first_tree.AddChild(child_node, new_child_node)
first_tree.AddChild(new_child_node, new_child_node2)
first_tree.AddChild(new_child_node2, new_child_node3)
first_tree.AddChild(parent_node, new_child_node4)
first_tree.AddChild(parent_node, new_child_node5)
first_tree.AddChild(new_child_node2, new_child_node6)

print('find: ', first_tree.FindNodesByValue('Parent'))
print('find: ', first_tree.convert_lst_nodes_to_lst_val(first_tree.FindNodesByValue('Parent')))
print(first_tree.GetAllNodes())
print(first_tree.add_level_for_tree())
#first_tree.MoveNode(new_child_node2, parent_node)
#first_tree.AddChild(parent_node, new_child_node2)
#print('count leafs: ', first_tree.LeafCount())

#print('count nodes: ', first_tree.Count())

#print('find: ' ,first_tree.FindNodesByValue('parent'))
#print(first_tree.GetAllNodesValue())
#first_tree.DeleteNode(child_node)
#print(first_tree.GetAllNodes())
#print(first_tree.GetAllNodes())
print('            ')


#parent_node.print_tree_nodes()
#child_node.print_tree_nodes()
#new_child_node.print_tree_nodes()
#new_child_node2.print_tree_nodes()
#new_child_node3.print_tree_nodes()'''


