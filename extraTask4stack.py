import unittest

#Задание 2. Переделайте реализацию стека так, чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой.

class Stack:
    def __init__(self):
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        temp = self.stack[0]
        del self.stack[0]
        return temp

    def push(self, value) -> None:
        self.stack = [value] + self.stack

    def peek(self) -> None:
        if self.size() == 0:
            return None
        return self.stack[0]

    def print_stack(self) -> None:
        for i in range(0, self.size()):
            print(self.stack[i])

    def append_mult(self, amount: int) -> None:
        for i in range(0, amount):
            self.push(i)

    def pop_mult(self, count: int) -> None:
        for i in range(0, count):
            self.pop()

    def append_str_in_stack(self, data: str) -> None:
        data = data.split()
        for i in reversed(range(0, len(data))):
            if data[i] != ' ':
                self.push(data[i])
            #print(stack.stack)



#тесты к заданию 2


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
        self.assertEqual(self.stack.stack, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
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
        self.assertEqual(self.stack.stack, [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
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
        self.assertEqual(self.stack.stack, [2, 1])
        self.assertEqual(self.stack.peek(), 2)
        self.stack.push(3)
        self.assertEqual(self.stack.stack, [3, 2, 1])
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

#Задание 5. Напишите функцию, которая получает на вход строку, состоящую
# из открывающих и закрывающих скобок (например, "(()((())()))" или "(()()(()") и,
# используя только стек и оператор цикла, определите, сбалансированы ли скобки в этой строке.
# Сбалансированной считается последовательность, в которой каждой открывающей обязательно соответствует закрывающая,
# а каждой закрывающей -- открывающая скобки, то есть последовательности "())(" , "))((" или "((())" будут несбалансированы.


def check_curly_braces(braces: str) -> bool:
    stack: Stack = Stack()
    if len(braces) == 0:
        return True
    if braces[0] != "(":
        return False
    for i in range(0, len(braces)):
        if stack.size() == 0 and braces[i] == ")":
            return False
        elif braces[i] == "(":
            stack.push(braces[i])
        elif braces[i] == ")":
            stack.pop()
    return True




class TestLinkedList(unittest.TestCase):

    def test_pop_single_el(self) -> None:
        self.assertEqual(check_curly_braces("())("), False)
        self.assertEqual(check_curly_braces("(()((())()))"), True)
        self.assertEqual(check_curly_braces("((())"), False)
        self.assertEqual(check_curly_braces("(()()(()))"), True)
        self.assertEqual(check_curly_braces("())("), False)
        self.assertEqual(check_curly_braces("()"), True)
        self.assertEqual(check_curly_braces("())()"), False)
        self.assertEqual(check_curly_braces("(((("), False)
        self.assertEqual(check_curly_braces(")))))))"), False)
        self.assertEqual(check_curly_braces("(((())))"), True)
        self.assertEqual(check_curly_braces(")"), False)
        self.assertEqual(check_curly_braces(""), True)


if __name__ == "__main__":
    unittest.main()


#Pадание 6 - необязательное, "Постфиксная запись выражения"

def postfix_expression(expr: str) -> int:
    stack1 = Stack()

    stack1.append_str_in_stack(expr)
    stack2: Stack = Stack()
    while stack1.size() != 0:

        char: str = stack1.pop()
        if char == "=":
            return int(stack2.stack[0])
        if char.isdigit():
            stack2.push(int(char))
        else:
            num1: int = stack2.pop()
            num2: int = stack2.pop()
            if char == "*":
                stack2.push(num2 * num1)
            elif char == "-":
                stack2.push(num2 - num1)
            elif char == "+":
                stack2.push(num2 + num1)
            elif char == "/":
                stack2.push(num2 / num1)


class TestLinkedList(unittest.TestCase):
    def test_postfix_expression(self) -> None:
        self.assertEqual(postfix_expression("8 2 + 5 * 9 + ="), 59)
        self.assertEqual(postfix_expression("12 3 + 5 / 4 + ="), 7)
        self.assertEqual(postfix_expression("22 20 - 8 + 5 / ="), 2)


if __name__ == "__main__":
    unittest.main()
