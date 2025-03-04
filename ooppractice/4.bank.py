class BankAccount:
    def __init__(self,accno:str,bal:float,acctyp:str):
        self.accountNumber = accno
        self.balance = bal
        self.accountType = acctyp

    def deposit(self,a:float)->None:
        self.balance+=a

    def withdraw(self,a:float)->bool:
        if self.balance < a:
            return False
        else:
            self.balance-=a
            return True
        
    def getBalance(self):
        return self.balance

class Customer:
    def __init__(self,cid:int,name:str,a:list[BankAccount]):
        self.customerID = cid
        self.name = name
        self.accounts = a

    def addAccount(self,a:str) -> None:
        self.accounts.append(a)

    def getAccount(self,accno:str):
        for i in self.accounts:
            if i.accountNumber == accno:
                return i
        return False

def main():
# Create a BankAccount and test deposit/withdrawal
    account = BankAccount("ACC001", 1000.0, "savings")
    account.deposit(500.0)
    if account.getBalance() != 1500.0:
        print("Error: Incorrect balance after deposit.")
    # Test valid withdrawal
    success_withdraw = account.withdraw(300.0)
    print("Withdrawal of 300 successful:", success_withdraw)
    # Test invalid withdrawal (exceeding balance)
    fail_withdraw = account.withdraw(2000.0)
    print("Withdrawal of 2000 (should fail):", fail_withdraw)
    # Create a Customer and add the account
    customer = Customer(1, "John Doe", [])
    customer.addAccount(account)
    retrieved = customer.getAccount("ACC001")
    print("Retrieved account balance:", retrieved.getBalance())
    # Test retrieval of a non-existing account
    non_exist = customer.getAccount("ACC999")
    print("Non-existent account retrieval:", non_exist is None)
if __name__ == '__main__':
    main()   
