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

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[self.size()-1]

    def print_stack(self):
        for i in range(0, self.size()):
            print(self.stack[i])

    def append_mult(self, amount):
        for i in range(0, amount):
            self.push(i)

    def pop_mult(self, count):
        for i in range(0, count):
            self.pop()


'''st = Stack()
st.push(1)
st.push(2)
st.push(3)
#st.append_mult(10)
print(st.stack)
print(st.peek())
print('pop ', st.pop())
print('pop ', st.pop())
print('pop ', st.pop())
print('stack: ', st.stack)
print('peek: ', st.peek())
st.append_mult(20)
#print('mp: ', st.pop_mult(10))
print(st.stack)
#print(st.peek())
print('pop ', st.pop())
print('pop ', st.pop())
print('pop ', st.pop())
print(st.stack)
#print(st.stack)'''


'''print('sp: ', stack.peek())
stack.print_stack()
stack.pop()
print("\n")
stack.print_stack()
print('sp: ', stack.peek())'''

import unittest

class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.stack: Stack = Stack()

    def test_pop_single_el(self) -> None:
        self.stack: Stack = Stack()
        self.assertEqual(self.stack.peek(), None)
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(4)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.peek(), 4)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.stack, [])
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.peek(), None)
        
    def test_add_mult_el_pop_mult_el(self) -> None:
        self.stack: Stack = Stack()
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.peek(), None)
        self.stack.append_mult(20)
        self.assertEqual(self.stack.size(), 20)
        self.assertEqual(self.stack.peek(), 19)
        self.stack.pop_mult(10)
        self.assertEqual(self.stack.stack, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(self.stack.size(), 10)
        self.assertEqual(self.stack.peek(), 9)

    def test_add_mult_el_pop_single_el(self) -> None:
        self.stack: Stack = Stack()
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.peek(), None)
        self.stack.append_mult(20)
        self.assertEqual(self.stack.size(), 20)
        self.assertEqual(self.stack.peek(), 19)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 19)
        self.assertEqual(self.stack.stack, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        self.assertEqual(self.stack.peek(), 18)

    def test_add_mult_el_pop_all_el(self) -> None:
        self.stack: Stack = Stack()
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.peek(), None)
        self.stack.append_mult(20)
        self.assertEqual(self.stack.size(), 20)
        self.assertEqual(self.stack.peek(), 19)
        self.stack.pop_mult(20)
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.stack, [])
        self.assertEqual(self.stack.peek(), None)

    def test_add_three_el_pop_all_el(self) -> None:
        self.stack: Stack = Stack()
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.peek(), None)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.stack, [1])
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.stack, [1, 2])
        self.assertEqual(self.stack.peek(), 2)
        self.stack.push(3)
        self.assertEqual(self.stack.stack, [1, 2, 3])
        self.assertEqual(self.stack.size(), 3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.stack, [])
        self.assertEqual(self.stack.peek(), None)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()




