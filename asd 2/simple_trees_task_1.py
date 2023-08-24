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

    def GetAllNodes(self) -> [object]:
        child: SimpleTreeNode = self.Root.Children
        if len(child) == 0:
            return [self.Root]
        lst: [object] = [] + [child[0].Parent]
        while len(child) != 0:
            for i in range(0, len(child)):
                lst.append(child[i])
            child = child[i].Children

        return lst


    def FindNodesByValue(self, val:int) -> [object]:
        if self.Root is None:
            return []
        if len(self.Root.Children) == 0 and self.Root.NodeValue != val:
            return []
        elif len(self.Root.Children) == 0 and self.Root.NodeValue == val:
            return [self.Root.NodeValue]
        child_lst: SimpleTreeNode = self.Root.Children
        summ_list_value: [object] = []
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
        return len(self.GetAllNodes())

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
    def convert_lst_nodes_to_lst_val(self, lst: [object])->[object]:
        lst_summ = []
        for i in range(0, len(lst)):
            lst_summ.append(lst[i].NodeValue)
        return lst_summ

parent_node: SimpleTreeNode = SimpleTreeNode('PARENT', None)
child_node: SimpleTreeNode = SimpleTreeNode('CHILD_NODE', parent_node)
new_child_node: SimpleTreeNode = SimpleTreeNode('PARENT', child_node)
new_child_node2: SimpleTreeNode = SimpleTreeNode('NEW_CHILD_NODE2', child_node)
#new_child_node3: SimpleTreeNode = SimpleTreeNode('new_child_node3', child_node)
first_tree: SimpleTree = SimpleTree(parent_node)
first_tree.AddChild(parent_node, child_node)
first_tree.AddChild(child_node, new_child_node)
first_tree.AddChild(new_child_node, new_child_node2)
#first_tree.AddChild(new_child_node2, new_child_node3)


#print(first_tree.GetAllNodes())
#first_tree.MoveNode(new_child_node2, parent_node)
#first_tree.AddChild(parent_node, new_child_node2)
#print('count leafs: ', first_tree.LeafCount())

#print('count nodes: ', first_tree.Count())

print('find: ', first_tree.convert_lst_nodes_to_lst_val(first_tree.FindNodesByValue('PARENT')))
print('find: ', first_tree.FindNodesByValue('PARENT'))
print(parent_node.NodeValue)
print(child_node.NodeValue)
print(first_tree.Root.NodeValue)
#print(first_tree.GetAllNodesValue())
#first_tree.DeleteNode(child_node)
#print(first_tree.GetAllNodes())
#print(first_tree.GetAllNodes())
print('            ')


#parent_node.print_tree_nodes()
#child_node.print_tree_nodes()
#new_child_node.print_tree_nodes()
#new_child_node2.print_tree_nodes()
#new_child_node3.print_tree_nodes()