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