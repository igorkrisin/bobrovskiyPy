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

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1

    def add(self, value: int) -> None:
        new_node: Node = Node(value)
        node: Node = self.head
        if node is None:
            self.head = new_node
            self.tail = new_node
        elif self.__ascending is False:
            if value >= self.head.value:
                self.add_in_head(new_node)
                #print('sh:', self.head.value)
            else:
                #print('val: ', value)
                #print('nval: ', node.value)
                #print('nnval: ', node.next.value)
                #print('test2')
                while node.next is not None:
                    #print('val: ', value)
                    #print('nval: ', node.value)
                    #print('nnval: ', node.next.value)
                    #print('test5')
                    #print('bool: nv>=v: ', node.value >= value, 'bool: v<=nnv: ', value >= node.next.value)
                    if node.value >= value >= node.next.value:
                        #print('TEST!!!!')
                        temp = node.next
                        node.next = new_node
                        new_node.prev = node
                        temp.prev = new_node
                        new_node.next = temp
                        return
                    elif node.next.next is None and value >= node.next.value:
                        temp = node.next
                        node.next = new_node
                        new_node.prev = node
                        new_node.next = temp
                        temp.prev = new_node
                        #print('test4')
                        return
                    elif node.next.next is None and value < node.next.value:
                        self.add_in_tail(new_node)
                        return
                    #print('node->next!!')
                    node = node.next



        elif self.__ascending is True:                  #!!!!TRUE!!!
            if value > self.tail.value:
                self.add_in_tail(new_node)
            elif value < self.head.value:
                self.add_in_head(new_node)
            else:
                while node.next is not None:
                    if node.value < value < node.next.value:
                        #print('TEST!!!!')
                        temp = node.next
                        node.next = new_node
                        new_node.prev = node
                        temp.prev = new_node
                        new_node.next = temp
                        return
                    elif node.next.next is None and value <= node.next.value:
                        temp = node.next
                        node.next = new_node
                        new_node.prev = node
                        new_node.next = temp
                        temp.prev = new_node
                        #print('test4')
                        return
                    elif node.next.next is None and value > node.next.value:
                        self.add_in_tail(new_node)
                    node = node.next






        #Не забудь про использование значения ask! его нужно учесть в этой фунуции!!!!!
        # автоматическая вставка value
        # в нужную позицию

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

    def clean(self, asc):
        self.__ascending = asc
        pass # здесь будет ваш код

    def len(self):
        node = self.head
        if node is None:
            return 0
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def add_in_head(self, newNode: Node):
        node = self.head
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

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0


oList = OrderedList(True)
oList.add(2)
oList.add(66)


oList.add(55)
oList.add(22)
oList.add(33)
oList.add(0)
oList.add(4)
oList.add(21)
oList.add(88)
oList.add(31)
oList.add(1)

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

    def test_delete_head_el(self) -> None:   #Остановился здесь - пишу тесты для delete. Надо еще написать clean и написать тесты н все остальные методы 
        self.link: OrderedList = OrderedList()
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

    '''def test_clean_list(self):
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
        self.assertEqual(self.link.tail.value, 15)'''


if __name__ == "__main__":
    unittest.main()
