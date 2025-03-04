class NegativeAmountException(Exception):
    def __init__(self, message):
        self.message = message


class InsufficientFundsException(Exception):
    def __init__(self, message):
        self.message = message

class BankAccount:
    def __init__(self, bal):
        self.balance = bal

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountException("Deposit amount cannot be negative.")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountException("Withdrawal amount cannot be negative.")
        if self.balance < amount:
            raise InsufficientFundsException("Insufficient funds for withdrawal.")
        self.balance -= amount
