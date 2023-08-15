class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item) -> None:
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val) -> Node:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next


    def find_all(self, val):
        node = self.head
        arr = []
        while node is not None:
            if node.value == val:
                arr.append(node)
            node = node.next
        return arr

    def delete(self, val, all=False):
        node = self.head
        if node is None:
            return
        if node.next is None:
            if node.value == val:
                self.head = None
                self.tail = None
                return
            else:

                return
        if not all:
            if node.value == val:
                self.head = node.next
                self.head.prev = None
                return
            while node.next is not None:
                if node.value == val:
                    break
                node = node.next
            if node.next is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                if node.value == val:
                    node.prev.next = None
                    self.tail = node.prev
            return
        if all:
            node = self.head
            if node.value == val:
                node.prev = None
                self.head = node.next
            while node.next is not None:
                if node.next.value == val and node.next.next is not None:
                    node.next = node.next.next
                    node.next.prev = node
                elif node.next.value == val and node.next.next is None:
                    node.next = None
                    self.tail = node
                    return
                node = node.next
            return

    def clean(self):
        node = self.head
        while node is not None:
            temp = node.next
            if temp is None:
                self.head = None
                self.tail = None
                return
            node.next.prev = None
            self.head = temp
            node = temp


    def len(self):
        node = self.head
        count: int = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode) -> None:
        node = self.head

        if node is None and afterNode is not None:
            return
        if afterNode is None and node is None:
            self.head = newNode
            self.tail = newNode
            return
        if afterNode is None and node is not None:
            node = self.tail
            node.next = newNode
            newNode.prev = node
            newNode.next = None
            self.tail = newNode
            return
        while node is not None:
            if node.next is None:
                node.next = newNode
                newNode.prev = node
                newNode.next = None
                self.tail = newNode
                return
            if node.value is afterNode.value:
                temp = node.next
                node.next = newNode
                newNode.prev = node
                newNode.next = temp
                temp.prev = newNode
                return
            node = node.next
        return

    def add_in_head(self, newNode):
        node = self.head
        if node is None:
            self.head = newNode
            self.tail = newNode
        else:
            node.prev = newNode
            newNode.next = node
            newNode.prev = None
            self.head = newNode

    def create_array_from_list(self) -> [int]:
        node: Node = self.head
        arr: [int] = []
        while node is not None:
            arr.append(node.value)
            node = node.next
        return arr

    def create_reference_to_val(self, arr) -> [int]:
        if arr is []:
            return []
        if arr is None:
            return []
        for i in range(0, len(arr)):
            arr[i]: [int] = arr[i].value
        return arr

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next




s_list = LinkedList2()

s_list.add_in_head(Node(55))
s_list.print_all_nodes()
#s_list.insert(Node(77), Node(5))
#print(s_list.len())
#print('answer:')
#s_list.print_all_nodes()

import unittest
class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.link: LinkedList2 = LinkedList2()

    def test_find_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.link.create_array_from_list()
        self.assertEqual(self.link.find(15).value, 15)
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)

    def test_find_one_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.create_array_from_list()
        self.assertEqual(self.link.find(10).value, 10)
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 10)


    def test_find_empty_list(self)-> None:
        self.link: LinkedList2 = LinkedList2()
        self.assertEqual(self.link.find(15), None)
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)


    def test_find_all_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.assertEqual(self.link.create_reference_to_val(self.link.find_all(15)), [15, 15])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)


    def test_find_all_empty_list(self)-> None:
        self.link: LinkedList2 = LinkedList2()
        self.assertEqual(self.link.create_reference_to_val(self.link.find_all(15)), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_delete_head_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_delete_tail_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(16))
        self.link.add_in_tail(Node(15))
        self.link.delete(15)
        self.assertEqual(self.link.create_array_from_list(), [10, 16])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 16)

    def test_delete_middle_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(20))
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [20,15])
        self.assertEqual(self.link.head.value, 20)
        self.assertEqual(self.link.tail.value, 15)

    def test_delete_single_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_delete_empty_list(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.delete(10)
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_clean_empty_list(self):
        self.link = LinkedList2()
        self.link.clean()
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_clean_list(self):
        self.link = LinkedList2()
        self.link.add_in_tail(Node(20))
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.clean()
        self.assertEqual(self.link.create_array_from_list(), [])
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)
    def test_len_three_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.assertEqual(self.link.len(), 3)
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)

    def test_len_single_el(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.assertEqual(self.link.len(), 1)
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 10)

    def test_len_empty_list(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.assertEqual(self.link.len(), 0)
        self.assertEqual(self.link.head, None)
        self.assertEqual(self.link.tail, None)

    def test_insert_empty_list(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.insert(None, Node(15))
        self.assertEqual(self.link.create_array_from_list(), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_insert_empty_list_head_after_node_none(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.insert(None, Node(15))
        self.assertEqual(self.link.create_array_from_list(), [15])
        self.assertEqual(self.link.head.value, 15)
        self.assertEqual(self.link.tail.value, 15)

    def test_insert_empty_list_tail_after_node_not_none(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.link.insert(None, Node(16))
        self.assertEqual(self.link.create_array_from_list(), [10, 15, 15, 16])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 16)

    def test_insert_list_tail(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(17))
        self.link.add_in_tail(Node(15))
        self.link.insert(Node(15), Node(99))
        self.assertEqual(self.link.create_array_from_list(), [10, 17, 15, 99])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 99)

    def test_insert_in_middle_list(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.link.insert(Node(15), Node(99))
        self.assertEqual(self.link.create_array_from_list(), [10, 15, 99, 15])
        self.assertEqual(self.link.head.value, 10)
        self.assertEqual(self.link.tail.value, 15)

    def test_add_in_head(self) -> None:
        self.link: LinkedList2 = LinkedList2()
        self.link.add_in_tail(Node(10))
        self.link.add_in_tail(Node(15))
        self.link.add_in_tail(Node(15))
        self.link.add_in_head(Node(17))
        self.assertEqual(self.link.create_array_from_list(), [17, 10, 15, 15])
        self.assertEqual(self.link.head.value, 17)
        self.assertEqual(self.link.tail.value, 15)


if __name__ == "__main__":
    unittest.main()
