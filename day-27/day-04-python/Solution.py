class Account:
    def __init__(self,accno,name,bal):
        self.accountNumber = accno
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
            if i.accountNumber == acc:
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
                from_account.withrdaw(amount)
                to_account.deposit(amount)
                return True
        return False

class LoanAccount(Account):
    # def __init__(self, accno, name, bal,interest):
    #     super().__init__(accno, name, bal)
    def __init__(self, loan_no, name, loan_amount, interest):
        self.loan_number = loan_no
        self.name = name
        self.loan_amount = loan_amount
        self.interest = interest
    
    def repay(self,amount):
        self.loan_amount -= amount
    
    def calculateInterest(self):
        i = self.loan_amount * self.interest
        return i
    
    def getOutstandingLoan(self):
        return self.loan_amount

class Transaction:
    def __init__(self,tid,accno,type,amount,time):
        self.transaction_id = tid
        self.accountNumber = accno
        self.type = type
        self.transaction_amount = amount
        self.time = time

    def __str__(self):
        return f"{self.transaction_amount}, {self.accountNumber}, {self.type}, {self.transaction_amount}, {self.time}"

class Person:
    def __init__(self,pno,pname):
        self.person_number = pno
        self.person_name = pname
        self.account_list = []

    def addAccount(self,accno):
        self.account_list.append(accno)

    def getAccounts(self):
        return self.account_list