import unittest
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1: int, v2: int) -> int:
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1

    def add(self, value) -> None:
        new_node: Node = Node(value)
        node: Node = self.head
        if node is None:
            self.head = new_node
            self.tail = new_node
        elif self.__ascending is False:
            if self.compare(value, self.tail.value) == -1 or self.compare(value, self.tail.value) == 0:
                self.add_in_tail(new_node)
            elif self.compare(value, self.head.value) == 1 or self.compare(value, self.head.value) == 0:
                self.add_in_head(new_node)
            else:
                while node.next is not None:
                    if self.compare(node.value, value) == 1 and self.compare(value, node.next.value) == 1:
                        temp = node.next
                        node.next = new_node
                        new_node.prev = node
                        temp.prev = new_node
                        new_node.next = temp
                        return
                    elif node.next.next is None and self.compare(value, node.next.value) == 1 \
                            or self.compare(value, node.next.value) == 0:
                        temp = node.next
                        node.next = new_node
                        new_node.prev = node
                        new_node.next = temp
                        temp.prev = new_node
                        return
                    elif node.next.next is None and self.compare(value, node.next.value) == -1:
                        self.add_in_tail(new_node)
                        return
                    node = node.next
        elif self.__ascending is True:
            if self.compare(value, self.tail.value) == 1 or self.compare(value, self.tail.value) == 0:
                self.add_in_tail(new_node)
            elif self.compare(value, self.head.value) == -1 or self.compare(value, self.head.value) == 0:
                self.add_in_head(new_node)
            else:
                while node.next is not None:
                    if self.compare(node.value, value) == -1 and self.compare(value, node.next.value) == -1:
                        temp = node.next
                        node.next = new_node
                        new_node.prev = node
                        temp.prev = new_node
                        new_node.next = temp
                        return
                    elif node.next.next is None and self.compare(value, node.next.value) == -1 \
                            or self.compare(value, node.next.value) == 0:
                        temp = node.next
                        node.next = new_node
                        new_node.prev = node
                        new_node.next = temp
                        temp.prev = new_node
                        return
                    elif node.next.next is None and self.compare(value, node.next.value) == 1:
                        self.add_in_tail(new_node)
                    node = node.next
        return

    def find(self, val) -> Node:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def delete(self, val) -> None:
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

    def clean(self, asc) -> None:
        self.__ascending = asc
        node: Node = self.head
        while node is not None:
            temp: Node = node.next
            if temp is None:
                self.head = None
                self.tail = None
                return
            node.next.prev = None
            self.head = temp
            node = temp

    def len(self) -> int:
        node: Node = self.head
        if node is None:
            return 0
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self) -> [object]:
        r = []
        node: Node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def add_in_head(self, newNode: Node) -> None:
        node: Node = self.head
        if node is None:
            self.head = newNode
            self.tail = newNode
        else:
            node.prev = newNode
            newNode.next = node
            newNode.prev = None
            self.head = newNode

    def add_in_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def create_reference_to_val(self, arr) -> [int]:
        if arr is []:
            return []
        if arr is None:
            return []
        for i in range(0, len(arr)):
            arr[i]: [int] = arr[i].value
        return arr

    def create_array_from_list(self) -> [int]:
        node: Node = self.head
        arr: [int] = []
        while node is not None:
            arr.append(node.value)
            node = node.next
        return arr

    def print_all_nodes(self) -> None:
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find_asc(self, val):
        node = self.head
        while node is not None:
            if self.__ascending is False and node.value < val or self.__ascending is True and node.value > val:
                return
            if node.value == val:
                return node
            node = node.next



class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        v1 = self.del_first_and_last_space(v1)
        v2 = self.del_first_and_last_space(v2)
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1

    def del_first_and_last_space(self, v: str) -> str:
        v = v.lstrip(' ')
        v = v.rstrip(' ')
        return v


'''o_str_list = OrderedStringList(True)
o_str_list.add("  bssdd")
o_str_list.add("ac")
o_str_list.add("f")
o_str_list.add("aaa")

print('len: ', o_str_list.len())
o_str_list.print_all_nodes()
o_str_list.find_asc("")'''


'''o_str_list1 = OrderedStringList(False)

o_str_list1.add(" asdasdad ")
o_str_list1.add("asdasdada")
o_str_list1.add(o_str_list1.del_first_and_last_space("     asd "))
o_str_list1.print_all_nodes()'''


oList = OrderedList(False)
oList.add(10)
oList.add(0)
oList.add(15)
oList.add(45)
print('find: ', oList.find_asc(9))
oList.print_all_nodes()
print('len: ', oList.len())

import unittest
class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.o_list: OrderedList = OrderedList(False)

    def test_find_el_in_single_el(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.o_list.add(15)
        self.assertEqual(self.o_list.find(15).value, 15)

    def test_find_el(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.o_list.add(1)
        self.o_list.add(22)
        self.o_list.add(15)
        self.o_list.add(0)
        self.o_list.add(100)
        self.o_list.add(5)
        self.assertEqual(self.o_list.find(15).value, 15)

    def test_find_missing_el(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.o_list.add(1)
        self.o_list.add(22)
        self.o_list.add(15)
        self.o_list.add(0)
        self.o_list.add(100)
        self.o_list.add(5)
        self.assertEqual(self.o_list.find(16), None)

    def test_find_el_empty_list(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.o_list.create_array_from_list()
        self.assertEqual(self.o_list.find(16), None)

    def test_add_in_empty_list_asc_false(self):
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(45)
        self.assertEqual(self.o_list.create_array_from_list(), [45])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 1)

    def test_add_in_list_two_el_asc_false(self):
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add(1023)
        self.assertEqual(self.o_list.create_array_from_list(), [1023, 45])
        self.assertEqual(self.o_list.head.value, 1023)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 2)

    def test_add_in_list_many_el_asc_false(self):
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add(1023)
        self.assertEqual(self.o_list.create_array_from_list(), [1023, 45])
        self.assertEqual(self.o_list.head.value, 1023)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 2)
        self.o_list.add(23)
        self.o_list.add(25)
        self.o_list.add(1)
        self.o_list.add(2)
        self.o_list.add(0)
        self.assertEqual(self.o_list.create_array_from_list(), [1023, 45, 25, 23, 2, 1, 0])
        self.assertEqual(self.o_list.head.value, 1023)
        self.assertEqual(self.o_list.tail.value, 0)
        self.assertEqual(self.o_list.len(), 7)

    def test_add_in_empty_list_asc_true(self):
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(45)
        self.assertEqual(self.o_list.create_array_from_list(), [45])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 1)

    def test_add_in_list_two_el_asc_true(self):
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add(1023)
        self.assertEqual(self.o_list.create_array_from_list(), [45, 1023])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 1023)
        self.assertEqual(self.o_list.len(), 2)

    def test_add_in_list_many_el_asc_true(self):
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add(1023)
        self.assertEqual(self.o_list.create_array_from_list(), [45, 1023])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 1023)
        self.assertEqual(self.o_list.len(), 2)
        self.o_list.add(23)
        self.o_list.add(25)
        self.o_list.add(1)
        self.o_list.add(2)
        self.o_list.add(0)
        self.assertEqual(self.o_list.create_array_from_list(), [0, 1, 2, 23, 25, 45, 1023])
        self.assertEqual(self.o_list.head.value, 0)
        self.assertEqual(self.o_list.tail.value, 1023)
        self.assertEqual(self.o_list.len(), 7)

    def test_add_in_same_el_asc_true(self):
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add(1023)
        self.o_list.add(1023)
        self.assertEqual(self.o_list.create_array_from_list(), [45, 1023, 1023])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 1023)
        self.assertEqual(self.o_list.len(), 3)

    def test_add_in_same_asc_false(self):
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add(1023)
        self.o_list.add(1023)
        self.assertEqual(self.o_list.create_array_from_list(), [1023, 1023, 45])
        self.assertEqual(self.o_list.head.value, 1023)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 3)

    def test_delete_head_el_false(self) -> None:   #Проверить добавление одинаоквых элементов, бак при добавлениии фалс, ноль не добавляется
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.o_list.add(15)
        self.assertEqual(self.o_list.len(), 2)
        self.assertEqual(self.o_list.head.value, 15)
        self.assertEqual(self.o_list.tail.value, 10)
        self.o_list.delete(15)
        self.assertEqual(self.o_list.len(), 1)
        self.assertEqual(self.o_list.create_array_from_list(), [10])
        self.assertEqual(self.o_list.head.value, 10)
        self.assertEqual(self.o_list.tail.value, 10)

    def test_delete_head_el_true(self) -> None:
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.o_list.add(15)
        self.assertEqual(self.o_list.head.value, 10)
        self.assertEqual(self.o_list.tail.value, 15)
        self.assertEqual(self.o_list.len(), 2)
        self.o_list.delete(10)
        self.assertEqual(self.o_list.len(), 1)
        self.assertEqual(self.o_list.create_array_from_list(), [15])
        self.assertEqual(self.o_list.head.value, 15)
        self.assertEqual(self.o_list.tail.value, 15)

    def test_delete_tail_el_true(self) -> None:
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.o_list.add(16)
        self.o_list.add(15)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 10)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 4)
        self.o_list.delete(45)
        self.assertEqual(self.o_list.len(), 3)
        self.assertEqual(self.o_list.create_array_from_list(), [10, 15, 16])
        self.assertEqual(self.o_list.head.value, 10)
        self.assertEqual(self.o_list.tail.value, 16)

    def test_delete_middle_el_true(self) -> None:
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.o_list.add(0)
        self.o_list.add(15)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 0)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 4)
        self.o_list.delete(15)
        self.assertEqual(self.o_list.len(), 3)
        self.assertEqual(self.o_list.create_array_from_list(), [0, 10, 45])
        self.assertEqual(self.o_list.head.value, 0)
        self.assertEqual(self.o_list.tail.value, 45)

    def test_delete_single_el_true(self) -> None:
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.assertEqual(self.o_list.head.value, 10)
        self.assertEqual(self.o_list.tail.value, 10)
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.delete(10)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.create_array_from_list(), [])
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)

    def test_delete_tail_el_false(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.o_list.add(16)
        self.o_list.add(15)
        self.o_list.add(45)
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 10)
        self.assertEqual(self.o_list.len(), 4)
        self.o_list.delete(10)
        self.assertEqual(self.o_list.len(), 3)
        self.assertEqual(self.o_list.create_array_from_list(), [45, 16, 15])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 15)

    def test_delete_middle_el_false(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.o_list.add(0)
        self.o_list.add(15)
        self.o_list.add(45)
        self.assertEqual(self.o_list.create_array_from_list(), [45, 15, 10, 0])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 0)
        self.assertEqual(self.o_list.len(), 4)
        self.o_list.delete(15)
        self.assertEqual(self.o_list.len(), 3)
        self.assertEqual(self.o_list.create_array_from_list(), [45, 10, 0])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 0)

    def test_delete_single_el_false(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.assertEqual(self.o_list.head.value, 10)
        self.assertEqual(self.o_list.tail.value, 10)
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.delete(10)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.create_array_from_list(), [])
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)

    def test_delete_el_in_empty_list_false(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.delete(10)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.create_array_from_list(), [])
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)

    def test_clean_empty_list_asc_false(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.clean(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.create_array_from_list(), [])
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)

    def test_clean_empty_list_asc_true(self) -> None:
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.clean(True)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.create_array_from_list(), [])
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)

    def test_clean_list_asc_false(self) -> None:
        self.o_list: OrderedList = OrderedList(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.o_list.add(0)
        self.o_list.add(15)
        self.o_list.add(45)
        self.assertEqual(self.o_list.create_array_from_list(), [45, 15, 10, 0])
        self.assertEqual(self.o_list.head.value, 45)
        self.assertEqual(self.o_list.tail.value, 0)
        self.assertEqual(self.o_list.len(), 4)
        self.o_list.clean(False)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.create_array_from_list(), [])
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)

    def test_clean_list_asc_true(self) -> None:
        self.o_list: OrderedList = OrderedList(True)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.o_list.add(10)
        self.o_list.add(0)
        self.o_list.add(15)
        self.o_list.add(45)
        self.assertEqual(self.o_list.create_array_from_list(), [0, 10, 15, 45])
        self.assertEqual(self.o_list.head.value, 0)
        self.assertEqual(self.o_list.tail.value, 45)
        self.assertEqual(self.o_list.len(), 4)
        self.o_list.clean(True)
        self.assertEqual(self.o_list.len(), 0)
        self.assertEqual(self.o_list.create_array_from_list(), [])
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)

    def test_add_str_in_empty_list_asc_false(self):
        self.o_list: OrderedStringList = OrderedStringList(False)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add("qwe  ")
        self.assertEqual(self.o_list.create_array_from_list(), ["qwe  "])
        self.assertEqual(self.o_list.head.value, "qwe  ")
        self.assertEqual(self.o_list.tail.value, "qwe  ")
        self.assertEqual(self.o_list.len(), 1)

    def test_add_str_in_list_two_el_asc_false(self):
        self.o_list: OrderedStringList = OrderedStringList(False)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add("  45")
        self.assertEqual(self.o_list.head.value, "  45")
        self.assertEqual(self.o_list.tail.value, "  45")
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add("1023")
        self.assertEqual(self.o_list.create_array_from_list(), ["  45", "1023"])
        self.assertEqual(self.o_list.head.value, "  45")
        self.assertEqual(self.o_list.tail.value, "1023")
        self.assertEqual(self.o_list.len(), 2)

    def test_add_str_in_list_many_el_asc_false(self):
        self.o_list: OrderedStringList = OrderedStringList(False)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add("45")
        self.assertEqual(self.o_list.head.value, "45")
        self.assertEqual(self.o_list.tail.value, "45")
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add("1023")
        self.assertEqual(self.o_list.create_array_from_list(), ["45", "1023"])
        self.assertEqual(self.o_list.head.value, "45")
        self.assertEqual(self.o_list.tail.value, "1023")
        self.assertEqual(self.o_list.len(), 2)
        self.o_list.add(" 23")
        self.o_list.add("  25")
        self.o_list.add("111 ")
        self.o_list.add("2")
        self.o_list.add("00000dsf ")
        self.assertEqual(self.o_list.create_array_from_list(), ["45", "  25", " 23", "2", "111 ", "1023", "00000dsf "])
        self.assertEqual(self.o_list.head.value, "45")
        self.assertEqual(self.o_list.tail.value, "00000dsf ")
        self.assertEqual(self.o_list.len(), 7)

    def test_add_str_in_empty_list_asc_true(self):
        self.o_list: OrderedStringList = OrderedStringList(True)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add("qwe")
        self.assertEqual(self.o_list.create_array_from_list(), ["qwe"])
        self.assertEqual(self.o_list.head.value, "qwe")
        self.assertEqual(self.o_list.tail.value, "qwe")
        self.assertEqual(self.o_list.len(), 1)

    def test_add_str_in_list_two_el_asc_true(self):
        self.o_list: OrderedStringList = OrderedStringList(True)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add("  45")
        self.assertEqual(self.o_list.head.value, "  45")
        self.assertEqual(self.o_list.tail.value, "  45")
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add("1023")
        self.assertEqual(self.o_list.create_array_from_list(), ["1023", "  45"])
        self.assertEqual(self.o_list.head.value, "1023")
        self.assertEqual(self.o_list.tail.value, "  45")
        self.assertEqual(self.o_list.len(), 2)

    def test_add_str_in_list_many_el_asc_true(self):
        self.o_list: OrderedStringList = OrderedStringList(True)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add("45")
        self.assertEqual(self.o_list.head.value, "45")
        self.assertEqual(self.o_list.tail.value, "45")
        self.assertEqual(self.o_list.len(), 1)
        self.o_list.add("1023")
        self.assertEqual(self.o_list.create_array_from_list(), ["1023", "45"])
        self.assertEqual(self.o_list.head.value, "1023")
        self.assertEqual(self.o_list.tail.value, "45")
        self.assertEqual(self.o_list.len(), 2)
        self.o_list.add(" 23")
        self.o_list.add("25")
        self.o_list.add("111 ")
        self.o_list.add("2")
        self.o_list.add("00000dsf ")
        self.assertEqual(self.o_list.create_array_from_list(), ["00000dsf ", "1023",  "111 ", "2",  " 23", "25", "45"])
        self.assertEqual(self.o_list.head.value, "00000dsf ")
        self.assertEqual(self.o_list.tail.value, "45")
        self.assertEqual(self.o_list.len(), 7)

    def test_add_str_in_empty_list_space_asc_true(self):
        self.o_list: OrderedStringList = OrderedStringList(True)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(" ")
        self.assertEqual(self.o_list.create_array_from_list(), [" "])
        self.assertEqual(self.o_list.head.value, " ")
        self.assertEqual(self.o_list.tail.value, " ")
        self.assertEqual(self.o_list.len(), 1)

    def test_add_str_in_empty_list_space_asc_false(self):
        self.o_list: OrderedStringList = OrderedStringList(False)
        self.assertEqual(self.o_list.head, None)
        self.assertEqual(self.o_list.tail, None)
        self.assertEqual(self.o_list.len(), 0)
        self.o_list.add(" ")
        self.assertEqual(self.o_list.create_array_from_list(), [" "])
        self.assertEqual(self.o_list.head.value, " ")
        self.assertEqual(self.o_list.tail.value, " ")
        self.assertEqual(self.o_list.len(), 1)


if __name__ == "__main__":
    unittest.main()

