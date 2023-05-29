import unittest

from externTask import Node
from externTask import LinkedList


def summ_value_node_two_lists(self, list_1, list_2) -> LinkedList: #задание со звездочкой
    node1: Node = list_1.head
    node2: Node = list_2.head
    if list_1.len() == list_2.len():
        while node1 is not None:
            node1.value = node1.value + node2.value
            node1 = node1.next
            node2 = node2.next
        return list_1
    else:
        list_1.head = None
        list_1.tail = None
        return list_1

def create_array_from_list(self) -> [int]:
    node: Node = self.head
    arr: [int] = []
    while node is not None:
        arr.append(node.value)
        node = node.next
    return arr


def create_reference_to_val(self, arr) -> [int]:
    for i in range(0, len(arr)):
        arr[i]: [int] = arr[i].value
    return arr





class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.link: LinkedList = LinkedList()

    def test_find_all_el(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.assertEqual(self.link.create_reference_to_val(self.link.find_all(15)), [15, 15])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)


    def test_find_all_empty_list(self)-> None:
        self.link: LinkedList = LinkedList()
        self.assertEqual(self.link.create_reference_to_val(self.link.find_all(15)), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_find_all_single_list(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(15))
        self.assertEqual(self.link.create_reference_to_val(self.link.find_all(15)), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_delete_head_el(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_delete_tail_el(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(16))
        self.link.add_in_tail(Node(15))
        self.link.delete(15)
        self.assertEqual(self.link.create_array_from_list(), [10,16])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 16)

    def test_delete_middle_el(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(20))
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [20,15])
        self.assertEqual(self.link.head.value, 20)
        self.assertEqual(self.link.tail.value, 15)

    def test_delete_single_el(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_delete_empty_list(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_clean_empty_list(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.clean()
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_clean_list(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(20))
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.clean()
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_len_three_el(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.assertEqual(self.link.len(), 3)
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)

    def test_len_single_el(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.assertEqual(self.link.len(), 1)
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 10)

    def test_len_empty_list(self) -> None:
        self.link: LinkedList = LinkedList()
        self.assertEqual(self.link.len(), 0)
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_insert_empty_list(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.insert(None, Node(15))
        self.assertEqual(self.link.create_array_from_list(), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_insert_not_empty_list_head(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(13))
        self.link.add_in_tail(Node(14))
        self.link.insert(None, Node(15))
        self.assertEqual(self.link.create_array_from_list(), [15,10,13,14])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 14)

    def test_insert_not_empty_list_tail(self) -> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(13))
        self.link.add_in_tail(Node(14))
        self.link.insert(Node(14), Node(15))
        self.assertEqual(self.link.create_array_from_list(), [10,13,14,15])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)

    def test_insert_not_empty_list_middle(self)-> None:
        self.link: LinkedList = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(13))
        self.link.add_in_tail(Node(14))
        self.link.insert(Node(13), Node(15))
        self.assertEqual(self.link.create_array_from_list(), [10, 13, 15, 14])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 14)

    def test_summ_value_node_two_lists(self) -> None:
        self.s_list: LinkedList = LinkedList()
        self.s_list.add_in_tail(Node(3))
        self.s_list.add_in_tail(Node(1))
        self.n_list: LinkedList = LinkedList()
        self.n_list.add_in_tail(Node(3))
        self.n_list.add_in_tail(Node(1))
        self.summ_list = summ_value_node_two_lists(self, self.n_list, self.n_list)
        self.assertEqual(self.summ_list.create_array_from_list(), [6, 2])


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
