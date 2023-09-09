class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def size_depth(self, depth) -> int:
        if depth == 0:
            return 1
        if depth == 1:
            return 3
        return self.size_depth(depth - 1) * 2 + 1

    def MakeHeap(self, a: [int], depth: int) -> [int]:
        self.HeapArray = [None] * self.size_depth(depth)
        a.sort(reverse=True)
        if len(a) > len(self.HeapArray):
            for i in range(0, len(self.HeapArray)):
                self.HeapArray[i] = a[i]
        if len(a) < len(self.HeapArray):
            for i in range(0, len(a)):
                self.HeapArray[i] = a[i]


        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth

    def GetMax(self) -> int:
        if not self.HeapArray:
            return -1  # если куча пуста
        if self.HeapArray[0] is None:
            return -1
        i = 0
        len_arr = len(self.HeapArray)
        while i < len_arr and self.HeapArray[i] is not None:
            i += 1
        get_node = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[i - 1]
        self.HeapArray[i - 1] = None
        i = 0
        left_child = i * 2 + 1
        right_child = i * 2 + 2

        # print('i: ', i)
        # print('len(self.HeapArray) :',len_arr)
        # print('left_child: ', left_child)
        # print('HA: ', heap.HeapArray)
        if i < len_arr and self.HeapArray[i] < self.HeapArray[left_child]:
            while left_child < len_arr and self.HeapArray[i] < self.HeapArray[left_child] \
                    and self.HeapArray[left_child] is not None:
                print('i: ', i)
                print('left_child: ', left_child)
                print('HA2: ', heap.HeapArray)
                print('self.HeapArray[i]: ', self.HeapArray[i])
                print('self.HeapArray[left_child]: ', self.HeapArray[left_child])
                self.HeapArray[i], self.HeapArray[left_child] = self.HeapArray[left_child], self.HeapArray[i]
                i = left_child
                left_child = i * 2 + 1
                print(print('self.HeapArray[right_chld]: ', self.HeapArray[right_child]))
        if i < len_arr and self.HeapArray[i] < self.HeapArray[right_child]:
            while right_child < len_arr and self.HeapArray[i] < self.HeapArray[right_child] \
                    and self.HeapArray[right_child] is not None:
                # print(1111)
                self.HeapArray[i], self.HeapArray[right_child] = self.HeapArray[right_child], self.HeapArray[i]
                i = right_child
                right_child = i * 2 + 2
            return get_node
        return get_node

    def Add(self, key: int) -> bool:
        if None not in self.HeapArray:
            return False
        if self.HeapArray[0] is None:
            self.HeapArray[0] = key
        i = 0
        while self.HeapArray[i] is not None:
            i += 1
        self.HeapArray[i] = key
        par_for_right_chl = (i - 2) // 2
        par_for_left_chl = (i - 1) // 2
        if i % 2 == 0:
            while i != 0 and self.HeapArray[i] >= self.HeapArray[par_for_right_chl]:
                self.HeapArray[i], self.HeapArray[par_for_right_chl] = self.HeapArray[par_for_right_chl], \
                    self.HeapArray[i]
                i = par_for_right_chl
                par_for_right_chl = (i - 2) // 2
        if i % 2 == 1:
            while i != 0 and self.HeapArray[i] >= self.HeapArray[par_for_left_chl]:
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
arr = [10, 15, 20, 3, 8, 9, 22, 55]
print('MakeHeapA: ', heap.MakeHeap(arr, 2))
heap.print_heap()
print(heap.GetMax())
print(heap.GetMax())

# heap.Add(25)
# print(heap.Add(25))
heap.print_heap()

# print(heap.Add(14))
