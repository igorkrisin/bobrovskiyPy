import unittest
from bar import LinkedList
from bar import Node


def create_array_from_list(self):
    node = self.head
    arr = []
    while node is not None:
        arr.append(node.value)
        node = node.next
    return arr


def create_reference_to_val(self, arr):
    for i in range(0, len(arr)):
        arr[i] = arr[i].value
    return arr

def summ_value_node_two_lists(self, list_1, list_2): #задание со *
    node1 = list_1.head
    node2 = list_2.head
    list_summ = LinkedList()
    arr1 = []
    arr2 = []
    len_list_1 = 0
    len_list_2 = 0
    while node1 is not None:
        len_list_1 += 1
        arr1.append(node1.value)
        node1 = node1.next
    while node2 is not None:
        len_list_2 += 1
        arr2.append(node2.value)
        node2 = node2.next
    if node1 != node2:
        return
    else:
        for i in range(0, len(arr1)):
            arr1[i] = arr1[i] + arr2[i]
    return arr1


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.link = LinkedList()

    def test_find_all_el(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.assertEqual(self.link.create_reference_to_val(self.link.find_all(15)), [15, 15])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)


    def test_find_all_empty_list(self):
        self.link = LinkedList()
        self.assertEqual(self.link.create_reference_to_val(self.link.find_all(15)), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_find_all_single_list(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(15))
        self.assertEqual(self.link.create_reference_to_val(self.link.find_all(15)), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_delete_head_el(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_delete_tail_el(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(16))
        self.link.add_in_tail(Node(15))
        self.link.delete(15)
        self.assertEqual(self.link.create_array_from_list(), [10,16])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 16)

    def test_delete_middle_el(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(20))
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [20,15])
        self.assertEqual(self.link.head.value, 20)
        self.assertEqual(self.link.tail.value, 15)

    def test_delete_single_el(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_delete_empty_list(self):
        self.link = LinkedList()
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_clean_empty_list(self):
        self.link = LinkedList()
        self.link.clean()
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_clean_list(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(20))
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.clean()
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_len_three_el(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.assertEqual(self.link.len(), 3)
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)

    def test_len_single_el(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.assertEqual(self.link.len(), 1)
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 10)

    def test_len_empty_list(self):
        self.link = LinkedList()
        self.assertEqual(self.link.len(), 0)
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_insert_empty_list(self):
        self.link = LinkedList()
        self.link.insert(None, Node(15))
        self.assertEqual(self.link.create_array_from_list(), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_insert_not_empty_list_head(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(13))
        self.link.add_in_tail(Node(14))
        self.link.insert(None, Node(15))
        self.assertEqual(self.link.create_array_from_list(), [15,10,13,14])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 14)

    def test_insert_not_empty_list_tail(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(13))
        self.link.add_in_tail(Node(14))
        self.link.insert(Node(14), Node(15))
        self.assertEqual(self.link.create_array_from_list(), [10,13,14,15])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)

    def test_insert_not_empty_list_middle(self):
        self.link = LinkedList()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(13))
        self.link.add_in_tail(Node(14))
        self.link.insert(Node(13), Node(15))
        self.assertEqual(self.link.create_array_from_list(), [10, 13, 15, 14])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 14)

    def test_summ_value_node_two_lists(self):
        self.s_list = LinkedList()
        self.s_list.add_in_tail(Node(3))
        self.s_list.add_in_tail(Node(1))
        self.n_list = LinkedList()
        self.n_list.add_in_tail(Node(3))
        self.n_list.add_in_tail(Node(1))
        self.assertEqual(self.s_list.summ_value_node_two_lists(self.s_list, self.n_list), [6, 2])


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
