from bar import Queue
from Task4stack import Stack
import unittest


#6.2
# сложность enqueue O(1): Вставка в конец(append) происходит по индексу за счет увеличения размера памяти и добаления элементов без сдвига.
# сложность dequeue O(n): Удаление на низком уровне происходит с перекопированием всех элементов в новый массив, а значит время опервции будет завитсеть от размера массива (list).

#6.3. Напишите функцию, которая "вращает" очередь по кругу на N элементов.

#qu = Queue()


def rotate_queue(self, quant: int):
    if self.size() == 0:
        return None
    for i in range(0, quant):
        self.enqueue(self.dequeue())


que = Queue()
que.enqueue(5)
que.enqueue(6)
que.enqueue(7)
que.enqueue(8)
que.enqueue(9)
rotate_queue(que, 4)
print(que.queue)


class Queue2Stack:

    def __init__(self):
        
        self.stack1 = Stack()
        self.stack2 = Stack()

    def size_stack2(self) -> int:
        return self.stack2.size()

    def push(self, value) -> None:
        self.stack1.push(value)

    def pop(self) -> Stack:
        if len(self.stack2.stack) == 0:
            while len(self.stack1.stack) != 0:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def print_2_stack(self) -> None:
        print('stack1: ', self.stack1.stack)
        print('stack2: ', self.stack2.stack)


st = Queue2Stack()
st.push(55)
st.push(76)
st.push(57)
st.push(90)
st.push(48)
st.print_2_stack()
st.pop()
st.print_2_stack()
st.pop()
st.print_2_stack()
st.pop()
st.print_2_stack()
st.push(567)
st.print_2_stack()
