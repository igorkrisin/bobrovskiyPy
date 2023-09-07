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
        print('current_node: ', current_node.NodeKey)
        if current_node.Parent is None:
            print('root: ', current_node.NodeKey, 'level: ', current_node.Level)
        print('nk: ', current_node.NodeKey, '|LFCHL: ', current_node.LeftChild if current_node.LeftChild is None
        else current_node.LeftChild.NodeKey, '|RTCHL: ', current_node.RightChild if current_node.RightChild is None
              else current_node.RightChild.NodeKey, 'level: ', current_node.Level)
        BalancedBST().print_binary_tree(current_node.RightChild)
        BalancedBST().print_binary_tree(current_node.LeftChild)

        return None

    def IsBalanced(self, root_node: BSTNode) -> bool:
        if root_node is None:
            return True
        left_max_level = self.max_node_level(root_node.LeftChild)
        right_max_level = self.max_node_level(root_node.RightChild)
        if abs(left_max_level - right_max_level) <= 1 and self.IsBalanced(root_node.RightChild) is True \
                and self.IsBalanced(root_node.LeftChild) is True:
            return True
        return False

    def max_node_level(self, node: BSTNode) -> int:
        if node is None:
            return 0
        return max(self.max_node_level(node.RightChild), self.max_node_level(node.LeftChild)) + 1
