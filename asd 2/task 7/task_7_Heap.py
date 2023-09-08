class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a: [int], depth: int) -> [int]:
        pass
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth

    def make_heap_recur(self, a: [int], ):

    def size_depth(self, depth) -> int:
        if depth == 0:
            return 1
        if depth == 1:
            return 3
        return self.size_depth(depth - 1) * 2 + 1

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        return -1  # если куча пуста

    def Add(self, key: int) -> bool:
        if None not in self.HeapArray:
            return False  # если куча вся заполнена
        # self.HeapArray = self.add_recur(key, 0, self.HeapArray)

    # def add_recur(self, key, i: int, arr: [int]) -> [int]:
    #     max_ind: int = i
    #     left_prnt_ind: int = 2*i+1
    #     right_prnt_ind: int = 2*i+2
    #     while arr[i] is not None:
    #         i += 1
    #     print('i: ', i)
    #     print('mi',max_ind)
    #     print('li', left_prnt_ind)
    #
    #     arr[i] = key
    #     if left_prnt_ind < len(arr) and arr[left_prnt_ind] > arr[max_ind]:
    #         max_ind = left_prnt_ind
    #         print(max_ind)
    #         return


    def print_heap(self):
        print(self.HeapArray)


heap = Heap()
heap.HeapArray = [1, 4, 3, 4, 6, 6, 7, 8, 10]
heap.print_heap()
print(heap.Add(14))
