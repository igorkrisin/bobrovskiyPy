class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
        
        
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
        if not self.FindNodesByValue(OriginalNode):
            return None
        OriginalNode.Parent.Children.remove(OriginalNode.NodeValue)
        
        
   
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
    
    
    
root_node: SimpleTreeNode = SimpleTreeNode(1, None)
first_node: SimpleTreeNode = SimpleTreeNode(2, root_node)
second_node: SimpleTreeNode = SimpleTreeNode(3, root_node)
third_node: SimpleTreeNode = SimpleTreeNode(4, root_node)
fourth_node: SimpleTreeNode = SimpleTreeNode(5, root_node)
fifth_node: SimpleTreeNode = SimpleTreeNode(6, root_node)
    
tree: SimpleTree = SimpleTree(root_node)

tree.AddChild(root_node, first_node)
tree.AddChild(root_node, second_node)
tree.AddChild(second_node, third_node)
tree.AddChild(third_node, fourth_node)
tree.AddChild(first_node, fifth_node)

print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))
#tree.DeleteNode(fifth_node)
print(tree.convert_lst_nodes_to_lst_val(tree.GetAllNodes()))
print(tree.Count())
print('leaf: ', tree.LeafCount())
#print('findByV: ',tree.convert_lst_nodes_to_lst_val(tree.FindNodesByValue(3)))



'''for i in range(0, len(chld.Children)):
            if i == len(chld.Children)-1:
                print(1)
                result_lst += (SimpleTree(chld[i].Children).GetAllNodes())
            else:
                result_lst += chld'''
