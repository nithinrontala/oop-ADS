class Transaction:
    def __init__(self,tid,accno,amount,transactiontype):
        self.tid  = tid
        self.accno = accno
        self.amount = amount
        self.ttype = transactiontype
    
    def getTransactionDetails(self):
        return f"transactionID: {self.tid}, accountNumber: {self.accno}, amount: {self.amount}, transactionType: {self.ttype}"
    
class BankAccount:
    def __init__(self, accno, balance, accountType):
        self.accno = accno
        self.balance = balance
        self.accountType = accountType
        self.transactions = []

    def performTransaction(self, t):
        if t.ttype == "deposit":
            self.balance += t.amount
            self.transactions.append(t)
            return True
        elif t.ttype == "withdrawal":
            if t.amount <= self.balance:
                self.balance -= t.amount
                self.transactions.append(t)
                return True
            else:
                return False
        return False

    def getBalance(self):
        return self.balance

    def listTransactions(self):
        return self.transactions



def main():
# Create a bank account
    account = BankAccount("ACC001", 1000.0, "checking")
    # Create transactions
    deposit = Transaction(1, "ACC001", 250.0, "deposit")
    withdrawal = Transaction(2, "ACC001", 100.0, "withdrawal")
    invalid_withdrawal = Transaction(3, "ACC001", 2000.0, "withdrawal")
    # Process deposit
    processed_deposit = account.performTransaction(deposit)
    print("Deposit processed:", processed_deposit)
    print("Balance after deposit:", account.getBalance())
    # Process valid withdrawal
    processed_withdrawal = account.performTransaction(withdrawal)
    print("Withdrawal processed:", processed_withdrawal)
    print("Balance after withdrawal:", account.getBalance())
    # Process invalid withdrawal (should fail)
    processed_invalid = account.performTransaction(invalid_withdrawal)
    print("Invalid withdrawal processed (should be False):", processed_invalid)
    # List transactions
    print("Transaction log:")
    for t in account.listTransactions():
        print(t.getTransactionDetails())
if __name__ == '__main__':
    main()



# 1 2 3 4 5 
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25