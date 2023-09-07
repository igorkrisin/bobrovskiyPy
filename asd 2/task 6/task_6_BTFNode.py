class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None  

    def GenerateTree(self, a: [int]) -> None:
        a.sort()
        self.Root = self.create_tree(a, self.Root, 0)

    def GenerateTreeReturn(self, a: [int]) -> None:
        return self.GenerateTree(a)

    def create_tree(self, arr: [int], parent: BSTNode, level: int) -> BSTNode:
        if not arr:
            return None
        mid: int = len(arr) // 2
        node: BSTNode = BSTNode(arr[mid], parent)
        node.Level = level
        node.LeftChild = self.create_tree(arr[:mid], node, level + 1)
        node.RightChild = self.create_tree(arr[mid + 1:], node, level + 1)
        return node

    def print_binary_tree(self, current_node) -> None:
        if current_node is None:
            return None
        # print('current_node: ', current_node.NodeKey)
        if current_node.Parent is None:
            print('root: ', current_node.NodeKey, 'level: ', current_node.Level)
        print('nk: ', current_node.NodeKey, '|LFCHL: ', current_node.LeftChild if current_node.LeftChild is None
        else current_node.LeftChild.NodeKey, '|RTCHL: ', current_node.RightChild if current_node.RightChild is None
              else current_node.RightChild.NodeKey, 'level: ', current_node.Level)
        BalancedBST().print_binary_tree(current_node.RightChild)
        BalancedBST().print_binary_tree(current_node.LeftChild)

        return None

    def IsBalanced(self, root_node: BSTNode) -> bool:
        # print('current_node: ', root_node.NodeKey)
        if root_node is None:
            return True
        # print('current_node: ', root_node.NodeKey)
        # print(root_node.Level, root_node.Level)

        left_lev: int = BalancedBST().IsBalanced(root_node.LeftChild) + 1
        right_lev: int = BalancedBST().IsBalanced(root_node.RightChild) + 1
        if abs(left_lev - right_lev) > 1:
            return False
        # print('ll: ', left_lev)
        # print('rl: ', right_lev)

        return True
        # return False  # сбалансировано ли дерево с корнем root_node


arr1 = [50, 22, 22, 22, 22, 22, 22, 22, 22, 23, 43, 54, 65, 77]

tree: BalancedBST = BalancedBST()

# tree.print_binary_tree()


# tree.Root = node
tree.GenerateTree(arr1)
# print('tree_root: ', tree.Root.LeftChild.LeftChild.LeftChild.NodeKey)
tree.print_binary_tree(tree.Root)
print('is_bal: ', tree.IsBalanced(tree.Root))
# tree.print_binary_tree()

# node = BSTNode(10, None)
# tree.Root = node
# node1 = BSTNode(15, node)
# node2 = BSTNode(25, node)
# node3 = BSTNode(35, node2)
# node4 = BSTNode(45, node3)
# node.RightChild = node1
# node.LeftChild = node2
# node2.RightChild = node3
# node3.RightChild = node4

# tree.print_binary_tree(tree.Root)

# print(tree.IsBalanced(tree.Root))
