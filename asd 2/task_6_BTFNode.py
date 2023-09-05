class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева
    
    def GenerateTree(self, a) -> None:
        a.sort()
        self.create_tree(a, self.Root)
        
    
    def create_tree(self, arr, parent) -> BSTNode:
        if not arr:
            return 
        mid = len(arr)//2
        
        node = BSTNode(arr[mid], parent)
        print(node.NodeKey)
        print(arr)
        node.LeftChild = self.create_tree(arr[:mid], node)
        node.RightChild = self.create_tree(arr[mid+1:mid], node)
        return node
    
    def print_tree(self)-> None:
        pass

    def IsBalanced(self, root_node) -> bool:
        return False # сбалансировано ли дерево с корнем root_node
    
arr = [50, 25, 75, 13, 35, 65, 85, 0, 18, 30, 45, 60, 70, 80, 90]


    
    
tree: BalancedBST = BalancedBST()
tree.GenerateTree(arr)
print(tree.Root)
    
    
    