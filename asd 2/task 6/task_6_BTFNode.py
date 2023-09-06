class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a: [int]) -> None:
        a.sort()
        print(self.create_tree(a, self.Root))
        self.print_binary_tree()

    def create_tree(self, arr: [int], parent: BSTNode) -> BSTNode:
        if not arr:
            return parent
        mid: int = len(arr) // 2
        node: BSTNode = BSTNode(arr[mid], parent)
        node.LeftChild = self.create_tree(arr[:mid], node)
        node.RightChild = self.create_tree(arr[mid + 1:], node)
        return node



    def print_binary_tree(self):
        print('pbt: ', self.Root)
        current_node: BalancedBST = self.Root
        if current_node is None:
            return
        if current_node.Parent is None:
            print('root: ', current_node)
        print('nk: ', current_node.NodeKey, '|RTCHL: ', current_node.RightChild if current_node.RightChild is None
        else current_node.RightChild.NodeKey, '|LFCHL: ', current_node.LeftChild if current_node.LeftChild is None
              else current_node.LeftChild.NodeKey)
        BalancedBST().print_binary_tree()

    def IsBalanced(self, root_node) -> bool:
        return False  # сбалансировано ли дерево с корнем root_node


arr = [50, 25, 75, 13, 35, 65, 85, 0, 18, 30, 45, 60, 70, 80, 90]

tree: BalancedBST = BalancedBST()

#node = BSTNode(10, None)
# node1 = BSTNode(15, node)
# node2 = BSTNode(25, node)
# node.RightChild = node1
# node.LeftChild = node2
# tree.Root = node
tree.GenerateTree(arr)
tree.print_binary_tree()

