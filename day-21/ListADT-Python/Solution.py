class ArrayListADT:
    def __init__(self):
        self.data = []
                
    def add(self, num):
        self.data.append(num)
        return True
    
    def add_at(self, index, c):  
        index = int(index)  
        self.size = len(self.data)+1   
        self.data.append(c)
        for i in range(len(self.data) - 2, index - 1, -1):
            self.data[i + 1] = self.data[i]
        
        self.data[index] = c
        return True
    
    def addAll(self,index,col):
        for i in range(len(col)):
            self.add_at(index + i, col[i])
        return True

    def contains(self,o):
        for i in self.data:
            if i == o:
                return True
        return False 

    def get(self,index):
        return self.data[index]              
    
    def clear(self):
        self.data = []
        self.size = 0
    
    def ensureCapacity(self, cap):
        self.addAll(len(self.data),[None]*cap)


    def __str__(self):
        return f"{self.data}"
