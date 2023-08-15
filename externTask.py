class Node:
    def __init__(self, v):
        self.value = v
        self.next = None



class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item) -> None:
        node = self.head
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            item.next = node
            self.head = item

    def pop(self) -> None:
        node = self.tail
        if node is None:
            return None
        else:
            while node.next is not None:
                node = node.next
            self.tail = node
            node.next = None


stack = Stack()
print('sh: ', stack.head)
print('st: ', stack.tail)
stack.push(10)
stack.push(10)
stack.push(10)
stack.push(10)
stack.pop()
print('sh2: ', stack.head.value)
print('st2: ', stack.tail.value)
stack.print_all_nodes()


