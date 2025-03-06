class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyCircularLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
        self._size+=1

    def add_first(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = new_node
        self._size += 1

    def contains(self,value):
        c = self.head
        count = 0

        while count < self._size:
            if c.value == value:
                return True
            c = c.next
            count+=1
        return False
    
    def get_first(self):
        return self.head.value
    
    def get_last(self):
        return self.tail.value
    
    def size(self):
        return self._size
    
    def remove(self):
        if not self.head:
            return None
        
        removable = self.head.value
        self.head = self.head.next
        self._size -= 1
        # print(self.tail.data)
        return removable
    
    def remove_last(self):
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
    
    def get(self, i):
        if i < 0 or i >= self._size:
            return
        c = self.head
        for i in range(i):
            c = c.next
        return c.value
    
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_circular(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False

    def __str__(self):
        if self._size == 0:
            return "CircularLinkedList is empty"

        c = self.head
        e = []
        count = 0

        while count < self._size:
            e.append(f"[{c.value}]")
            c = c.next
            count+=1
        return "<->".join(e)

class Josephus:
    def josephusDCLL(self, size, rotation):
        self.size = size
        self.rotation = rotation
    
        
