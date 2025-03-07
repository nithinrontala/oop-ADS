class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add_to_front(self, s):
        new_node = Node(s)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def add_to_end(self,s):
        # print("hi")
        new_node = Node(s)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None
        self._size+=1

    def remove_from_front(self):        
        if not self.head:
            return None

        removable = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self._size -= 1
        # print(self.tail.data)
        return removable

    def remove_from_end(self):
        if not self.head:  
            return None
        
        removable = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            # print(self.tail.)

        self._size -= 1
        # print(removable)
        return removable

    def find(self, value):
        c = self.head
        while c != None:
            if c.value == value:
                return True
            c = c.next
        return False

    def check_empty(self):
        if self.head == None:
            return True
        return False

    def get_size(self):
        # print(self._size)
        return self._size

    def insert_at(self, i, value):
        if i < 0 or i > self._size:
            return
        if  i == 0:
            self.add_to_front(value)
            return
        if i == self._size:
            self.add_to_end(value)
            return
        new_node = Node(value)
        c = self.head
        for i in range(i-1):
            c = c.next
        c.next.prev = new_node
        new_node.prev = c
        new_node.next = c.next
        c.next = new_node
        self._size+=1

    def get_at(self, i):
        if i < 0 or i >= self._size:
            return
        c = self.head
        for i in range(i):
            c = c.next
        return c.value

    def get_node_at(self, i):
        if i < 0 or i >= self._size:
            return
        c = self.head
        for i in range(i):
            c = c.next
        return c

    def remove_at(self, i):
        if i < 0 or i >= self._size:
            return
        if self.head == self.tail:
            return None
        
        c = self.head
        for i in range(i):
            c = c.next
        if c.next is None:
            self.remove_from_end()
            return
        a = c.next
        b = c.prev
        c.prev.next = a
        c.next.prev = b
        self._size-=1

    def reverse_traversal(self):
        c =self.tail
        while c:
            print(c.value,end=" ")
            c = c.prev
        print()

    def clear_list(self):
        self.head = None
        self.tail = None
        self._size = 0

    def swap_nodes(self, i1, i2):
        if i1 == i2:
            return
        n1 = self.get_node_at(i1)
        n2 = self.get_node_at(i2)
        if n1 == None or n2 == None:
            return
        # print(self.__str__())
        self.insert_at(i1,n2.value)
        # print(self.__str__())
        a = self.remove_at(i1+1)
        # print(self.__str__())
        self.insert_at(i2,n1.value)
        # print(self.__str__())
        b = self.remove_at(i2+1)
        # print(self.__str__())
        # if i1 == i2:
        #     return
        # node1 = self.get_node_at(i1)
        # node2 = self.get_node_at(i2)
        
        # if not node1 or not node2:
        #     return
        
        # if node1.prev:
        #     node1.prev.next = node2
        # if node1.next:
        #     node1.next.prev = node2

        # if node2.prev:
        #     node2.prev.next = node1
        # if node2.next:
        #     node2.next.prev = node1
        
        # node1.prev, node2.prev = node2.prev, node1.prev
        # node1.next, node2.next = node2.next, node1.next

        # if self.head == node1:
        #     self.head = node2
        # elif self.head == node2:
        #     self.head = node1

        # if self.tail == node1:
        #     self.tail = node2
        # elif self.tail == node2:
        #     self.tail = node1

    def detect_cycle(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False
    
    def print_list(self):
        if self._size == 0:
            return 
        c = self.head
        while c:
            print(c.value,end=" ")
            c = c.next
        print()

    def __str__(self):
        if self._size == 0:
            return "DoublyLinkedList is empty"

        c = self.head
        e = []

        while c:
            e.append(f"[{c.value}]")
            c = c.next
        return "<->".join(e)
