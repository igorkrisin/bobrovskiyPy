class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey: object = key
        self.NodeValue: object = val
        self.Parent: BSTNode = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key: object) -> [object]:
        if key == self.Root.NodeKey:
            return [self.Root, True, False]

        find_node: BSTNode = BSTFind().Node
        find_has_key: bool = BSTFind().NodeHasKey
        find_to_left: bool = BSTFind().ToLeft
        if self.Root is None:
            return [find_node, find_has_key, find_to_left]
        current_node: BSTNode = self.Root
        if key == current_node.NodeKey:
            return [current_node, True, False]
        elif key > current_node.NodeKey and current_node.RightChild:
            return BST(current_node.RightChild).FindNodeByKey(key)
        elif key < current_node.NodeKey and current_node.LeftChild:
            return BST(current_node.LeftChild).FindNodeByKey(key)
        return [current_node, find_has_key, False if key > current_node.NodeKey else True]

    def convert_find_node(self, lst_from_find: [object]):
        lst_from_find[0] = lst_from_find[0].NodeKey
        return [lst_from_find[0], lst_from_find[1], lst_from_find[2]]

    def AddKeyValue(self, key: object, val: object):
        is_find_node: bool = self.FindNodeByKey(key)[1]
        if self.FindNodeByKey(key)[0] is None:
            return
        if is_find_node:
            return False
        current_node: BSTNode = self.FindNodeByKey(key)[0]
        is_to_left: bool = self.FindNodeByKey(key)[2]
        if not is_find_node and is_to_left:
            left_child_node: BSTNode = BSTNode(key, val, current_node)
            left_child_node.NodeValue = val
            left_child_node.NodeKey = key
            left_child_node.Parent = current_node
            current_node.LeftChild = left_child_node
        if not is_find_node and not is_to_left:
            right_child_node: BSTNode = BSTNode(key, val, current_node)
            right_child_node.NodeValue = val
            right_child_node.NodeKey = key
            right_child_node.Parent = current_node
            current_node.RightChild = right_child_node

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        if FindMax:
            while FromNode.RightChild is not None:
                FromNode = FromNode.RightChild
                self.FinMinMax(FromNode, FindMax)
            return FromNode
        else:
            while FromNode.LeftChild is not None:
                FromNode = FromNode.LeftChild
                self.FinMinMax(FromNode, FindMax)
            return FromNode

    def convert_min_max_result(self, node: BSTNode) -> object:
        return node.NodeKey

    def del_leaf(self, delete_node: BSTNode, parent: BSTNode) -> bool:
        if parent.LeftChild == delete_node:
            delete_node.Parent = None
            parent.LeftChild = None
        elif parent.RightChild == delete_node:
            delete_node.Parent = None
            parent.RightChild = None

    def del_one_chld(self, delete_node: BSTNode, parent: BSTNode) -> None:
        if parent is None and delete_node.LeftChild is not None and delete_node.RightChild is None:
            self.Root = delete_node.LeftChild
        elif parent is None and delete_node.RightChild is not None and delete_node.LeftChild is None:
            self.Root = delete_node.RightChild
        elif parent is None and delete_node.RightChild is not None and delete_node.LeftChild is not None:
            self.Root = delete_node.RightChild
        elif parent.LeftChild == delete_node and delete_node.LeftChild is None:
            delete_node.Parent = None
            parent.LeftChild = delete_node.RightChild
            if delete_node.RightChild is not None:
                delete_node.RightChild.Parent = parent

        elif parent.LeftChild == delete_node and delete_node.RightChild is None:
            delete_node.Parent = None
            parent.LeftChild = delete_node.LeftChild
            if delete_node.LeftChild is not None:
                delete_node.LeftChild.Parent = parent

        elif parent.RightChild == delete_node and delete_node.LeftChild is None:
            delete_node.Parent = None
            parent.RightChild = delete_node.RightChild
            if delete_node.RightChild is not None:
                delete_node.RightChild.Parent = parent

        elif parent.RightChild == delete_node and delete_node.RightChild is None:
            delete_node.Parent = None
            parent.RightChild = delete_node.LeftChild
            if delete_node.LeftChild is not None:
                delete_node.LeftChild.Parent = parent

    def DeleteNodeByKey(self, key) -> bool:
        is_key_in_tree: bool = self.FindNodeByKey(key)[1]
        if not is_key_in_tree:
            return False
        delete_node: BSTNode = self.FindNodeByKey(key)[0]
        if delete_node.Parent is None and delete_node.LeftChild is None and delete_node.RightChild is None:
            return False
        if delete_node.RightChild is None and delete_node.LeftChild is None:
            self.del_leaf(delete_node, delete_node.Parent)
        elif delete_node.RightChild is None or delete_node.LeftChild is None:
            self.del_one_chld(delete_node, delete_node.Parent)
        else:
            parent_min_key_node = delete_node.RightChild
            min_key_node = self.FinMinMax(parent_min_key_node, False)
            delete_node.NodeKey = min_key_node.NodeKey
            self.del_one_chld(min_key_node, min_key_node.Parent)

    def Count(self) -> int:
        count = 1
        current_node = self.Root
        if current_node is None:
            return 0

        count += BST(current_node.LeftChild).Count()
        count += BST(current_node.RightChild).Count()
        return count

    def print_binary_tree(self):
        current_node = self.Root
        if current_node is None:
            return
        print('pbt2: ', current_node.NodeKey, '|RTCHL: ', current_node.RightChild if current_node.RightChild is None
        else current_node.RightChild.NodeKey, '|LFCHL: ', current_node.LeftChild if current_node.LeftChild is None
              else current_node.LeftChild.NodeKey)
        BST(current_node.LeftChild).print_binary_tree()
        BST(current_node.RightChild).print_binary_tree()

    def create_tree(self, node_store: [], summ_node: int, trees):
        for i in range(0, summ_node - 1):
            trees.AddKeyValue(node_store[i], node_store[i])
        return trees
