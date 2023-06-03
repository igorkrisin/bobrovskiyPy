from task5Deque import Deque
import unittest

#7.1 потому, что работая с головой списка при удалении и добавлении нужно скопировать его (на низком уровне) в новый массив
# а при добавлении в хвост достаочно увелчичить размер существующего массива и добавить еще один элемент

#7.2Напишите функцию, которая с помощью deque проверяет,
# является ли некоторая строка палиндромом (читается одинаково слева направо и справа налево).


def is_palindrom(deque: Deque):
    while deque.size() != 0:
        if deque.removeFront() != deque.removeTail():
            return False
    return True


d = Deque()
d.add_str_in_deque(" ")

print(is_palindrom(d))

class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.dequ: Deque = Deque()

    def test_deque_is_palindrom(self) -> None:
        self.dequ: Deque = Deque()
        self.dequ.add_str_in_deque("asddsa")
        self.assertEqual(is_palindrom(self.dequ), True)
        self.dequ.add_str_in_deque("asdfdsa")
        self.assertEqual(is_palindrom(self.dequ), False)
        self.dequ.add_str_in_deque("")
        self.assertEqual(is_palindrom(self.dequ), True)
        self.dequ.add_str_in_deque(" ")
        self.assertEqual(is_palindrom(self.dequ), False)
        self.dequ.add_str_in_deque("qwertyuioppoiuytrewq")
        self.assertEqual(is_palindrom(self.dequ), True)

    if __name__ == "__main__":
        unittest.main()
