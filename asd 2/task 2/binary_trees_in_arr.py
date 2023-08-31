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

    def FindKeyIndex(self, key) -> object:
        current_key = self.Tree
        i = 0
        depth = 0
        if not current_key[i]:
            return i
        if key > current_key[i] and current_key:
            i = i*2+1
            return aBST(depth+1).FindKeyIndex(current_key[i])
        if key < current_key[i] and current_key:
            i = i*2-1
            return aBST(depth+1).FindKeyIndex(current_key[i])
        return None




        return None  # не найден

    def AddKey(self, key):
        # добавляем ключ в массив
        return -1;
        # индекс добавленного/существующего ключа или -1 если не удалось


arr_tree = aBST(4)

#arr_tree.print_arr()
print(arr_tree.FindKeyIndex(4))




