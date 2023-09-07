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
        self.Root: BSTNode = self.create_tree(a, self.Root, 0)

    def create_tree(self, arr: [int], parent: BSTNode, level: int) -> BSTNode:
        if not arr:
            return None
        mid: int = len(arr) // 2
        node: BSTNode = BSTNode(arr[mid], parent)
        node.Level = level
        node.LeftChild = self.create_tree(arr[:mid], node, level + 1)
        node.RightChild = self.create_tree(arr[mid + 1:], node, level + 1)
        return node

    def print_binary_tree(self, current_node: BSTNode) -> None:
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
