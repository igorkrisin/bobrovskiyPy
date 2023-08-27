class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key: object) -> [BSTFind]:
        find_node = BSTFind().Node
        find_has_key = BSTFind().NodeHasKey
        find_to_left = BSTFind().ToLeft
        if self.Root is None:
            #print('ret_start:', [find_node, find_has_key, find_to_left])
            return [find_node, find_has_key, find_to_left]
        current_node: BSTNode = self.Root
        #print(current_node.NodeKey)
        if key == current_node.NodeKey:
            return [current_node, True, False]
        elif key > current_node.NodeKey and current_node.RightChild:
            #print('ret_start1:', [find_node, find_has_key, find_to_left])
            return BST(current_node.RightChild).FindNodeByKey(key)
        elif key < current_node.NodeKey and current_node.LeftChild:
            #print('ret_start2:', [find_node, find_has_key, find_to_left])
            return BST(current_node.LeftChild).FindNodeByKey(key)
        #print('finish: ', [find_node, find_has_key, find_to_left])
        return [current_node, find_has_key, False if key > current_node.NodeKey else True]

    def AddKeyValue(self, key: object, val: object):
        is_find_node = self.FindNodeByKey(key)[1]
        if self.FindNodeByKey(key)[0] is None:
            print('!!!!!!!!!!!!!!!!!!!None in find key!!!!!!!!!!!!!!!!!!!')
            return
        if is_find_node:
            return False
        current_node: BSTNode = self.FindNodeByKey(key)[0]
        is_to_left = self.FindNodeByKey(key)[2]
        if not is_find_node and is_to_left:
            left_child_node: BSTNode = BSTNode(key, val, current_node)
            left_child_node.NodeValue = val
            left_child_node.NodeKey = key
            left_child_node.Parent = current_node
            current_node.LeftChild = left_child_node
        if not is_find_node and not is_to_left:

            right_child_node:  BSTNode = BSTNode(key, val, current_node)
            right_child_node.NodeValue = val
            right_child_node.NodeKey = key
            right_child_node.Parent = current_node
            current_node.RightChild = right_child_node

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool):
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

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self):
        return 0  # количество узлов в дереве


    def print_binary_tree(self):
        current_node = self.Root

        #print('pbt1: ', current_node)
        if current_node is None:
            return
        print('pbt2: ', current_node.NodeKey, '|RTCHL: ', current_node.RightChild if current_node.RightChild is None else current_node.RightChild.NodeKey, '|LFCHL: ', current_node.LeftChild if current_node.LeftChild is None else current_node.LeftChild.NodeKey)
        BST(current_node.LeftChild).print_binary_tree()

        BST(current_node.RightChild).print_binary_tree()




root_node: BSTNode = BSTNode(10, 0, None)
binary_tree: BST = BST(root_node)
#first_node = BSTNode(1, 1, root_node)
binary_tree.AddKeyValue(12, 1)
binary_tree.AddKeyValue(9, 1)
binary_tree.AddKeyValue(11, 1)
binary_tree.AddKeyValue(8, 1)
print('Root Node: ', root_node)
print('MAX NODE: ', binary_tree.FinMinMax(root_node, False).NodeKey)
#print(binary_tree.FindNodeByKey(-1))
binary_tree.print_binary_tree()
print('root: ', binary_tree.Root)
print('chld_root_lft: ', root_node.LeftChild)
print('chld_root_rght :', root_node.RightChild)
