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
                    elif node.next.next is None and self.compare(value, node.next.value) == 1:
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


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        v1 = self.del_first_and_last_space(v1)
        v2 = self.del_first_and_last_space(v2)

        if len(v1) < len(v2):
            return -1
        if len(v1) == len(v2):
            return 0
        if len(v1) > len(v2):
            return 1
        return 0

    def del_first_and_last_space(self, v: str) -> str:
        v = v.lstrip(' ')
        v = v.rstrip(' ')
        return v