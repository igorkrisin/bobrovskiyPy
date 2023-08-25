class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

    def PrintNodesField(self) -> None:
        print('val: ', self.NodeValue)
        print('par: ', self.Parent.NodeValue)
        print('child: ', self.Children)
        
        
class SimpleTree:

    def __init__(self, root) -> None:
        self.Root = root # корень, может быть None
	
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
        #NewParent.PrintNodesField()
        

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
    
    