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
        lst: [object] = [] 
        lst.append(self.Root)
        while len(child) != 0:
            for y in range(0, len(child)):
                lst.append(child[y])
            child = child[i].Children
            if i < len(child):
                i += 1
            if i == len(child):
                i = 0
        return lst

    def FindNodesByValue(self, val:int) -> [object]:
        if self.Root is None:
            return []
        if len(self.Root.Children) == 0 and self.Root.NodeValue != val:
            return []
        elif len(self.Root.Children) == 0 and self.Root.NodeValue == val:
            return [self.Root]
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

    def add_level_for_tree(self) -> [object]:
        level: int =0
        child: SimpleTreeNode = self.Root.Children
        if len(child) == 0:
            return [self.Root.NodeValue]
        lst: [object] = [] + [self.Root.NodeValue]
        while len(child) != 0:
            for i in range(0, len(child)):
                lst.append(child[i].NodeValue)
            lst
            child = child[i].Children
        return lst

