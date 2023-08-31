class aBST:

    def __init__(self, depth) -> None:
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = self.size_depth(depth)
        self.Tree = [None] * tree_size  # массив ключей

    def size_depth(self, depth) -> int:
        if depth == 0:
            return 0
        if depth == 1:
            return 1
        return self.size_depth(depth - 1) * 2 + 1

    def print_arr(self) -> None:
        for node in self.Tree:
            print(node)

    def FindKeyIndex(self, key) -> int:
        current_key = self.Tree
        if self.Tree is None:
            return 0
        i = 0
        print('i000: ', i)
        if current_key[i] is None:
            print(3423423)
            return -i
        depth = 0
        print('i: ', i)
        if current_key[i] == 0 and key == 0 and self.Tree:
            return i*2+2    #add right node
        if current_key[i] is not None and key > current_key[i]:
            print('key>curr: ', i)
            return self.FindKeyIndex(current_key[i*2+2])
        if current_key[i] is not None and key < current_key[i]:
            print('key<curr: ', i)
            return self.FindKeyIndex(current_key[i*2+1])
        print(00000000000000)
        return None

    def AddKey(self, key):
        find = self.FindKeyIndex(key)
        print('find: ', find)
        if find is None:
            return -1
        if find <= 0:
            self.Tree[-find] = key
            return -find
        if find > 0 and self.Tree:
            return -1





arr_tree = aBST(4)

#arr_tree.print_arr()
#print(arr_tree.FindKeyIndex(4))
arr_tree.AddKey(50)


arr_tree.print_arr()
arr_tree.AddKey(25)
print('++++++++++++')
arr_tree.print_arr()




