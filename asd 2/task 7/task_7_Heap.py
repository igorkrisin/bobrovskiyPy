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
        a = [None] * self.size_depth(depth)
        size_heap = self.size_depth(depth)
        start_index = 0
        print(a)
        self.HeapArray = self.make_heap_recur(a, len(self.HeapArray), start_index)
        print('SH: ', self.HeapArray)
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth

    def make_heap_recur(self, arr: [int], size_heap: int, i: int):
        max_el = i
        #print(arr)
        #print('arr[max_El]: ', arr[max_el])
        #print(max_el)
        #print('sh: ', size_heap)
        left_node = 2 * i + 1
        right_node = 2 * i + 2
        if left_node < size_heap and arr[left_node] > arr[max_el]:
            max_el = left_node
        if right_node < size_heap and arr[right_node] > arr[max_el]:
            max_el = right_node
        if max_el != i:
            arr[i], arr[max_el] = arr[max_el], arr[i]

            self.make_heap_recur(arr, size_heap, max_el)
        #return arr

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        return -1  # если куча пуста

    def Add(self, key: int) -> bool:
        if None not in self.HeapArray:
            return False  # если куча вся заполнена

    def print_heap(self):
        print(self.HeapArray)


heap = Heap()
heap.HeapArray = [1, 2, 3, 4, 5, 6, 7, 8, 10]
heap.MakeHeap(heap.HeapArray, 3)

#print(heap.make_heap_recur(heap.HeapArray, heap.size_depth(3), 0))
heap.print_heap()

# print(heap.Add(14))
