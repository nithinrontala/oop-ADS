class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def add_first(self, s):
        new_node = Node(s)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def contains(self, s):
        c = self.head
        while c:
            if c.data == s:
                return True
            c = c.next
        return False

    def find_middle(self):
        if self.size == 0:
            return None
        middle_index = self.size // 2
        c = self.head
        for i in range(middle_index):
            c = c.next
        # print(c.data)
        return c.data
    
    def nth_from_end(self, n):
        if n <= 0 or n > self.size:
            return None
        first = self.head
        second = self.head
        for _ in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        return second.data

    def insert_at_position(self, pos, data):
        if pos < 0 or pos > self.size:
            return
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        else:
            c = self.head
            for _ in range(pos - 1):
                c = c.next
            new_node.next = c.next
            c.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self.size += 1

    def insert_before(self,before_data,data):

        if self.head.data == before_data:
            self.add_first(data)
            return

        c = self.head
        while c.next:
            if c.next.data == before_data:
                new_node = Node(data)
                new_node.next = c.next
                c.next = new_node
                self.size += 1
                return
            c = c.next

        print(f"{before_data} not found in the list.")

    def delete_before(self, data, before_data):
        c = self.head
        while c.next and c.next.next:
            if c.next.next.data == before_data:
                c.next = c.next.next
                self.size -= 1
                return
            c = c.next

    def delete_after(self, data):
        c = self.head
        while c:
            if c.data == data and c.next:
                c.next = c.next.next
                if c.next is None:
                    self.tail = c
                self.size -= 1
                return
            c = c.next

    def get_first(self):
        if self.head:
            return self.head.data
        return None

    def get_last(self):
        if self.tail:
            return self.tail.data
        return None

    def size(self):
        print(self.size)
        return self.size

    def remove(self):
        removable = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return removable

    def remove_last(self):
        if not self.head:
            return None

        if self.head == self.tail:
            removable = self.head.data
            self.head = self.tail = None
            self.size -= 1
            return removable

        c = self.head
        while c.next != self.tail:
            c = c.next

        removable = self.tail.data
        self.tail = c
        self.tail.next = None
        self.size -= 1
        return removable

    def get(self, index):
        c = self.head
        for i in range(index):
            c = c.next
        return c.data

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def to_string(self):
        if self.size == 0:
            return "LinkedList is empty"

        c = self.head
        e = []

        while c:
            e.append(f"[{c.data}]")
            c = c.next
        # print("".join(e))
        return "".join(e)
