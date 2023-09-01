class aBST:

    def __init__(self, depth) -> None:
        tree_size = self.size_depth(depth)
        self.Tree = [None] * tree_size

    def size_depth(self, depth) -> int:
        if depth == 0:
            return 0
        if depth == 1:
            return 1
        return self.size_depth(depth - 1) * 2 + 1

    def print_arr(self) -> None:
        print(self.Tree)

    def FindKeyIndex(self, key) -> int:
        if key == 0 and self.Tree[0] is None:
            return 0
        i = 0
        while i < len(self.Tree):
            if self.Tree[i] is None:
                return -i
            if key == 0 and self.Tree[i] == 0:
                return -i
            if key > self.Tree[i]:
                i = i * 2 + 2
            elif key < self.Tree[i]:
                i = i * 2 + 1
        return None

    def AddKey(self, key) -> int:
        find = self.FindKeyIndex(key)
        if find is None:
            return -1
        if find <= 0:
            self.Tree[-find] = key
            return -find
        if find > 0 and self.Tree:
            return -1

    def create_arr_tree(self, arr: []):
        for i in range(0, len(arr)):
            self.AddKey(arr[i])
