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
    
class Bank:
    def __init__(self):
        self.bank_accounts = []

    def addAccount(self,acc):
        self.bank_accounts.append(acc)
    
    def findAccount(self,acc):
        for i in self.bank_accounts:
            if i.account_number == acc:
                return i
        return None
    
    def transfer(self, fromacc, toacc, amount):
        from_account = self.findAccount(fromacc)
        to_account = self.findAccount(toacc)
        
        if not from_account:
            return "from_account doesnot exist."
        elif not to_account:
            return "to_account doesnot exist."
        else:
            if from_account.balance >= amount and amount > 0:
                from_account.balance -= amount
                to_account.balance += amount
                return True
        return False