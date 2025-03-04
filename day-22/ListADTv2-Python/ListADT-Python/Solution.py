class ArrayListADT:
    def __init__(self):
        self.data = []
        self.size = 0
                
    def add(self, num):
        # for i in self.data:
            self.data.append(num)
            self.size = self.size_()
            # self.size+=1
            return True
        
    def add_at(self, index, c):  
        index = int(index)  
        self.data.append(c)  
        self.size = self.size_()
        for i in range(len(self.data) - 2, index - 1, -1):
            self.data[i + 1] = self.data[i]
        
        self.data[index] = c
        self.size = self.size_()
        return True
    
    def add_all_at(self,index,col):
        for i in range(len(col)):
            self.add_at(index + i, col[i])
        return True
    
    def add_all(self,c):
        for i in c:
            self.data.append(i)
        self.size = self.size_()
        return self.data

    def contains(self,o):
        for i in self.data:
            if i == o:
                return True
        return False 

    def index_of(self,o):
        for i in range(len(self.data)):
            if self.data[i] == o:
                return i
        return -1

    def get(self,index):
        # print(self.data)
        l = []
        for i in self.data:
            if i != None:
                l.append(i)
        # print(l,index)
        self.size = len(l)
        self.data = l
        return l[index]
    
    def last_index_of(self,o):
        # print(63636,self.size- 1)
        l = []
        for i in range(len(self.data)):
            if self.data[i] == o:
                l.append(i)
        return l[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size_(self):
        return len(self.data)
    
    def remove_at(self, index):
        l = []
        a = self.data[index]
        for i in range(len(self.data)):
            if i != index:
                l.append(self.data[i])
        self.data = l
        self.size = self.size_()
        return a            
    
    def remove(self,o):
        a = self.data.index(o)
        self.remove_at(a)
        self.size = self.size_()
        return True

            
    def set(self,index,e):
        a = self.data[index]
        self.data[index] = e
        return a
                
    def trim_to_size(self):
        return self.data


    def clear(self):
        self.data = []
        self.size = 0
    
    def ensure_capacity(self, cap):
        self.add_all_at(len(self.data),[None]*cap)


    def __str__(self):
        return f"{self.data}"
