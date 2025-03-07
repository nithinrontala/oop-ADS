class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def add(self,s):
        new_node = Node(s)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size+=1
    
    def add_first(self, s):
        new_node = Node(s)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
        
    def contains(self,s):
        c = self.head
        while c:
            if c.data == s:
                return True
            c = c.next
        return False
    
    def get_first(self):
        return self.head.data
    
    def get_last(self):
        return self.tail.data
    
    def size(self):
        return self._size
    
    def remove(self):
        if not self.head:
            return None

        removable = self.head.data
        self.head = self.head.next
        self._size -= 1
        # print(self.tail.data)
        return removable
    
    def remove_last(self):
        if not self.head:  
            return None
        
        removable = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            # print(self.tail.)

        self._size -= 1
        # print(removable)
        return removable

    
    def get(self,ind):
        c = self.head
        for i in range(ind):
            c = c.next
        return c.data
    
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        if self._size == 0:
            return "DoublyLinkedList is empty"

        c = self.head
        e = []

        while c:
            e.append(f"[{c.data}]")
            c = c.next
        # print("<->".join(e))
        return "<->".join(e)
