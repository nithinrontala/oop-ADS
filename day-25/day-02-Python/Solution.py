class Account:
    def __init__(self,accno,name,bal):
        self.account_number = accno
        self.name = name
        self.balance = bal

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount

    def getBalance(self):
        return self.balance

    def withdraw(self,amount):
        if self.balance > amount and amount > 0:
            self.balance -= amount
            return True
        return False

class SavingsAccount(Account):
    def __init__(self, accno, name, bal, interst):
        super().__init__(accno, name, bal)
        self.interst = interst
    
    def calculateInterest(self):
        i = self.balance*(self.interst)
        self.balance -=i
        return i

class CurrentAccount(Account):
    def __init__(self, accno, name, bal, over_bal):
        super().__init__(accno, name, bal)
        self.over = over_bal

    def withdraw(self, amount):
        if self.balance + self.over >= amount and amount > 0:
            self.balance -= amount
            return True
        return False