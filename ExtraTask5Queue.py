#from bar import Queue
#from Task4stack import Stack
import unittest


#6.2
# сложность enqueue O(1): Вставка в конец(append) происходит по индексу за счет увеличения размера памяти и добаления элементов без сдвига.
# сложность dequeue O(n): Удаление на низком уровне происходит с перекопированием всех элементов в новый массив, а значит время опервции будет завитсеть от размера массива (list).

#6.3. Напишите функцию, которая "вращает" очередь по кругу на N элементов.

#qu = Queue()


def rotate_queue(self, quant):
    if self.size() == 0:
        return None
    for i in range(0, quant):
        self.enqueue(self.dequeue())


'''que = Queue()
que.enqueue(5)
que.enqueue(6)
que.enqueue(7)
que.enqueue(8)
que.enqueue(9)
rotate_queue(que, 4)
print(que.queue)


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.que: Queue = Queue()

    def test_dequeue_single_el(self) -> None:
        self.que: Queue = Queue()
        self.assertEqual(self.que.size(), 0)
        self.que.enqueue(4)
        self.assertEqual(self.que.size(), 1)
        self.assertEqual(self.que.dequeue(), 4)
        self.assertEqual(self.que.queue, [])
        self.assertEqual(self.que.size(), 0)

    def test_enqueue_few_el_dequeue_few_el(self) -> None:
        self.que: Queue = Queue()
        self.assertEqual(self.que.size(), 0)
        self.que.enqueue(0)
        self.que.enqueue(1)
        self.que.enqueue(2)
        self.que.enqueue(3)
        self.que.enqueue(4)
        self.que.enqueue(5)
        self.assertEqual(self.que.size(), 6)
        self.que.dequeue()
        self.assertEqual(self.que.queue, [1, 2, 3, 4, 5])
        self.assertEqual(self.que.size(), 5)
        self.que.dequeue()
        self.assertEqual(self.que.queue, [2, 3, 4, 5])
        self.assertEqual(self.que.size(), 4)
        self.que.dequeue()
        self.que.dequeue()
        self.que.dequeue()
        self.que.dequeue()
        self.assertEqual(self.que.queue, [])
        self.assertEqual(self.que.size(), 0)

    def test_rotation_queue(self) -> None:
        self.qu: Queue = Queue()
        self.assertEqual(self.que.size(), 0)
        self.qu.enqueue(0)
        self.qu.enqueue(1)
        self.qu.enqueue(2)
        self.qu.enqueue(3)
        self.qu.enqueue(4)
        self.qu.enqueue(5)
        self.assertEqual(self.qu.queue, [0, 1, 2, 3, 4, 5])
        self.assertEqual(self.qu.size(), 6)
        rotate_queue(3)
        self.assertEqual(self.qu.queue, [3, 4, 5, 0, 1, 2])
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.dequeue()
        self.qu.rotate_queue(3)
        self.assertEqual(self.qu.queue, [])


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()'''


class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        temp = self.stack[self.size()-1]
        del self.stack[self.size()-1]
        return temp


    def push(self, value) -> None:
        self.stack = self.stack + [value]


class Queue2Stack:

    def __int__(self):
        
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
#print(st.push(5))


class Stack2:
    def __init__(self):
        self.stack = []
    def push(self, elem):
        if self.stack:
            self.stack.append((elem, min(elem, self.stack[-1][1])))
        else:
            self.stack.append((elem, elem))

    def pop(self):
        return self.stack.pop()[0]

    def size(self) -> int:
        return len(self.stack)

class Queue2:
    def __init__(self):
        self.s1 = Stack2()
        self.s2 = Stack2()

    def push(self, elem):
        self.s1.push(elem)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()




qu1 = Queue2()

qu1.push(45)
qu1.push(55)

print(qu1)

