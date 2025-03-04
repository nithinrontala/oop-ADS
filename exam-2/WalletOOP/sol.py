class ArrayListADT:
    def __init__(self):
        self.data = []
        self.size = 0

    def add(self, num):
        self.data.append(num)
        self.size = len(self.data)
        return True

    def add_at(self, index, c):
        index = int(index)
        self.data.append(c)
        self.size = len(self.data)
        for i in range(len(self.data) - 2, index - 1, -1):
            self.data[i + 1] = self.data[i]
        self.data[index] = c
        self.size = len(self.data)
        return True

    def add_all_at(self, index, col):
        for i in range(len(col)):
            self.add_at(index + i, col[i])
        return True

    def add_all(self, c):
        for i in c:
            self.data.append(i)
        self.size = len(self.data)
        return self.data

    def contains(self, o):
        return o in self.data

    def index_of(self, o):
        for i in range(len(self.data)):
            if self.data[i] == o:
                return i
        return -1

    def get(self, index):
        return self.data[index]

    def last_index_of(self, o):
        l = []
        for i in range(len(self.data)):
            if self.data[i] == o:
                l.append(i)
        return l[-1] if l else -1

    def is_empty(self):
        return len(self.data) == 0

    def size_(self):
        return len(self.data)

    def remove_at(self, index):
        value = self.data.pop(index)
        self.size = len(self.data)
        return value

    def remove(self, o):
        if o in self.data:
            self.remove_at(self.data.index(o))
            self.size = len(self.data)
            return True
        return False

    def set(self, index, e):
        a = self.data[index]
        self.data[index] = e
        return a

    def trim_to_size(self):
        return self.data

    def clear(self):
        self.data = []
        self.size = 0

    def ensure_capacity(self, cap):
        self.add_all_at(len(self.data), [None] * cap)

    def __str__(self):
        return f"{self.data}"

