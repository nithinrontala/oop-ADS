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


class Transaction:
    def __init__(self):
        self.type = ""
        self.amount = 0.0
        self.fee = 0

    def TransactionFee(self):
        self.f = self.amount * self.fee
        self.remaining = self.amount - self.f


class Wallet:
    # p=Transaction()
    def __init__(self):
        self.t = Transaction()
        self.a = self.t.amount
        self.fee = 0.0
        self.totalAmount = 0.0
        self.TransactionHis = ArrayListADT()  
        
    def iniWallet(self, a, b):
        self.limit = float(a)
        self.fee = float(b) / 100
        print(f"Wallet initialized with withdrawalLimit: {int(a):.1f}, withdrawalFeePercentage: {float(b)}%")

    def deposit(self, amount):
        fee = 0.0
        d = "DEPOSIT"
        if amount < 0:
            return f"Deposit of {float(amount)} failed. Balance remains: {self.totalAmount}"
        else:
            self.totalAmount += amount
            self.getTransactions((d, amount, fee))
            return f"Deposit of {float(amount)} successful. Current balance: {self.totalAmount}"

    def withdraw(self, amount):
        if self.limit < amount or self.totalAmount < amount:
            return f"Withdrawal of {float(amount)} failed. Balance remains: {self.totalAmount}"
        else:
            w = "WITHDRAW"
            self.withdrawalFee(amount)
            self.getTransactions((w, amount, self.f))
            return f"Withdrawal of {float(amount)} successful with a fee of {self.f}. Current balance: {self.totalAmount}"

    def getBalance(self):
        return f"Current Balance: {self.totalAmount}"

    def getTransactions(self, a):
        self.TransactionHis.add(a)  

    def Transtaction(self):
        trans = "Transaction History:\n"
        if self.TransactionHis.is_empty():
            return trans
        for i in range(self.TransactionHis.size_()):
            t = self.TransactionHis.get(i)
            # print(t)  
            trans += f"{i+1}. {t[0]} {t[1]:.1f} (Fee: {t[2]})\n"
        return trans

    def withdrawalFee(self, amount):
        self.f = amount * self.fee
        self.totalAmount -= amount
        self.totalAmount -= self.f
        return [self.totalAmount, self.f]

    def runWallet(self):
        while True:
            try:
                s = input().split()
                if s[0] == "deposit":
                    print(self.deposit(float(s[1])))
                elif s[0] == "withdraw":
                    print(self.withdraw(float(s[1])))
                elif s[0] == "getBalance":
                    print(self.getBalance())
                elif s[0] == "getTransactions":
                    print(self.Transtaction())
                else:
                    self.iniWallet(s[0], s[1])
            except:
                break


if __name__ == "__main__":
    r = Wallet()
    r.runWallet()
