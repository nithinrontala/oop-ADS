
from Solution import InsufficientFundsException, NegativeAmountException, BankAccount

def main():
    account = BankAccount(500)
    print("Initial balance:", account.get_balance())
    
    # Test 1: Valid deposit
    try:
        account.deposit(200)
        print("Deposited 200, new balance:", account.get_balance())
    except Exception as e:
        if isinstance(e, NegativeAmountException):
            print("Deposit error (NegativeAmountException):", e)
    
    # Test 2: Deposit with a negative amount
    try:
        account.deposit(-50)
    except Exception as e:
        if isinstance(e, NegativeAmountException):
            print("Deposit error (NegativeAmountException):", e)
        else:
            print("Deposit error (Other Exception):", e)
    
    # Test 3: Valid withdrawal
    try:
        account.withdraw(100)
        print("Withdrew 100, new balance:", account.get_balance())
    except Exception as e:
        if isinstance(e, NegativeAmountException):
            print("Withdrawal error (NegativeAmountException):", e)
        elif isinstance(e, InsufficientFundsException):
            print("Withdrawal error (InsufficientFundsException):", e)
        else:
            print("Withdrawal error (Other Exception):", e)
    
    # Test 4: Withdrawal with a negative amount
    try:
        account.withdraw(-20)
    except Exception as e:
        if isinstance(e, NegativeAmountException):
            print("Withdrawal error (NegativeAmountException):", e)
        else:
            print("Withdrawal error (Other Exception):", e)
    
    # Test 5: Withdrawal exceeding balance to trigger InsufficientFundsException
    try:
        account.withdraw(1000)
    except Exception as e:
        if isinstance(e, InsufficientFundsException):
            print("Withdrawal error (InsufficientFundsException):", e)
        elif isinstance(e, NegativeAmountException):
            print("Withdrawal error (NegativeAmountException):", e)
        else:
            print("Withdrawal error (Other Exception):", e)

main()

