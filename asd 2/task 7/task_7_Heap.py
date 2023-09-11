class Heap:

    def __init__(self):
        self.HeapArray = []

    def size_depth(self, depth) -> int:
        if depth == 0:
            return 1
        if depth == 1:
            return 3
        return self.size_depth(depth - 1) * 2 + 1

    def MakeHeap(self, a: [int], depth: int) -> None:
        len_heap = self.size_depth(depth)
        self.HeapArray = [None] * len_heap
        for i in range(0, len(a)):
            self.Add(a[i])

    def GetMax(self) -> int:
        if not self.HeapArray:
            return -1
        if self.HeapArray[0] is None:
            return -1
        if len(self.HeapArray) > 1 and self.HeapArray[1] is None:
            get_return = self.HeapArray[0]
            self.HeapArray[0] = None
            return get_return
        elif len(self.HeapArray) == 1:
            get_return = self.HeapArray[0]
            self.HeapArray[0] = None
            return get_return
        y = 0
        len_arr = len(self.HeapArray)
        while y < len_arr and self.HeapArray[y] is not None:
            y += 1
        get_node = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[y - 1]
        self.HeapArray[y - 1] = None
        i = 0
        left_child = i * 2 + 1
        right_child = i * 2 + 2
        while right_child < len_arr \
                and i < len_arr \
                and self.HeapArray[right_child] is not None and self.HeapArray[i] is not None\
                and self.HeapArray[left_child] is not None \
                and self.HeapArray[i] < max(self.HeapArray[left_child], self.HeapArray[right_child]):
            if self.HeapArray[left_child] > self.HeapArray[right_child]:
                self.HeapArray[i], self.HeapArray[left_child] = self.HeapArray[left_child], self.HeapArray[i]
                i = left_child
                left_child = i * 2 + 1
            else:
                self.HeapArray[i], self.HeapArray[right_child] = self.HeapArray[right_child], self.HeapArray[i]
                i = right_child
                right_child = i * 2 + 2
        if self.HeapArray[i * 2 + 2] is None and self.HeapArray[i] is not None \
                and self.HeapArray[left_child] is not None and self.HeapArray[i] < self.HeapArray[left_child]:
            self.HeapArray[i], self.HeapArray[left_child] = self.HeapArray[left_child], self.HeapArray[i]
        return get_node

    def Add(self, key: int) -> bool:
        if None not in self.HeapArray:
            return False
        if self.HeapArray[0] is None:
            self.HeapArray[0] = key
            return True
        i = 0
        while self.HeapArray[i] is not None:
            i += 1
        self.HeapArray[i] = key
        par_for_right_chl = (i - 2) // 2
        par_for_left_chl = (i - 1) // 2
        if i % 2 == 0:
            while i != 0 and self.HeapArray[par_for_right_chl] is not None \
                    and self.HeapArray[i] >= self.HeapArray[par_for_right_chl]:
                self.HeapArray[i], self.HeapArray[par_for_right_chl] = self.HeapArray[par_for_right_chl], \
                    self.HeapArray[i]
                i = par_for_right_chl
                par_for_right_chl = (i - 2) // 2
        if i % 2 == 1:
            while i != 0 and self.HeapArray[par_for_left_chl] is not None \
                    and self.HeapArray[i] >= self.HeapArray[par_for_left_chl]:
                self.HeapArray[i], self.HeapArray[par_for_left_chl] = self.HeapArray[par_for_left_chl], \
                    self.HeapArray[i]
                i = par_for_left_chl
                par_for_left_chl = (i - 1) // 2
        return True

    def print_heap(self):
        print(self.HeapArray)

    def return_heap(self):
        return self.HeapArray


heap = Heap()
print(heap.GetMax())