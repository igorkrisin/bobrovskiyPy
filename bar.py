class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

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
        if node == None:
            return
        if all:
            if node.value == val:
                self.head = node.next
                node = self.head
            if node == None:
                return
            while node is not None:
                if node.value == val:
                    self.head = node.next
                    node = self.head
                    continue
                if node == None:
                    return
                if node.next == None:
                    return
                if node.next.value == val:
                    if node.next.next == None:
                        node.next = None
                        break
                    node.next = node.next.next
                node = node.next
        if not all:
            if node.value == val:
                self.head = node.next
                return
            while node is not None:
                if node.next == None:
                    return
                if node.next.value == val:
                    node.next = node.next.next
                    node = None
                    return 
                node = node.next
            if node == None:
                return
        
    def clean(self):
       node = self.head
       while node is not None:
           temp = node.next
           node = None
           self.head = temp
           if temp == None:
               return
           node = temp
           
    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count 

    def insert(self, afterNode, newNode):
        node = self.head
        if node == None:
            return
        while node.value is not afterNode.value:
            if node.next == None:
                return
            node = node.next
        temp = node.next
        node.next = newNode
        newNode.next = temp

