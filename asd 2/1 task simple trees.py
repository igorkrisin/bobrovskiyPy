class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def print_tree_nodes(self):
        print('node_val: ', self.NodeValue)
        print('parent: ', self.Parent)
        print('children: ', self.Children)
        print('       ')



class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode) -> None:
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode) -> None:
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
        else:
            return None
        if NodeToDelete.Children:
            self.DeleteNode(NodeToDelete.Children[0])
        NodeToDelete.Parent = None
        NodeToDelete.NodeValue = None

    def GetAllNodes(self) -> [object]:
        child: SimpleTreeNode = self.Root.Children
        if len(child) == 0:
            return []
        lst: [object] = [] + [child[0].Parent]
        while len(child) != 0:
            for i in range(0, len(child)):
                lst.append(child[i])
            child = child[i].Children

        return lst


    def FindNodesByValue(self, val:int) -> [object]:
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
        children_nodes = OriginalNode.Children
        self.AddChild(NewParent, OriginalNode)
        while len(children_nodes):
            for i in range(0, len(children_nodes)):
                self.AddChild(children_nodes[i], children_nodes.Children[i])
            children_nodes = children_nodes[i].Children




        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        pass

    def Count(self) -> int:
        return len(self.GetAllNodes())


    def LeafCount(self) -> int:
        lst_nodes: [object] = self.GetAllNodes()
        count = 0
        for i in range(0, len(lst_nodes)):
            if not lst_nodes[i].Children:
                count += 1
        return count




parent_node: SimpleTreeNode = SimpleTreeNode(5, None)
child_node: SimpleTreeNode = SimpleTreeNode(10,parent_node)
new_child_node: SimpleTreeNode = SimpleTreeNode(5, child_node)
new_child_node2: SimpleTreeNode = SimpleTreeNode(12, child_node)
new_child_node3: SimpleTreeNode = SimpleTreeNode(5, child_node)
first_tree: SimpleTree = SimpleTree(parent_node)
first_tree.AddChild(parent_node, child_node)
first_tree.AddChild(child_node, new_child_node)
first_tree.AddChild(new_child_node, new_child_node2)
first_tree.AddChild(new_child_node, new_child_node3)
first_tree.MoveNode(new_child_node, new_child_node3)
#print('count leafs: ', first_tree.LeafCount())

#print('count nodes: ', first_tree.Count())

#print(first_tree.FindNodesByValue(5))
#print(first_tree.GetAllNodes())
#first_tree.DeleteNode(new_child_node2)
#print(first_tree.GetAllNodes())
print('            ')


parent_node.print_tree_nodes()
child_node.print_tree_nodes()
new_child_node.print_tree_nodes()
new_child_node2.print_tree_nodes()
new_child_node3.print_tree_nodes()
