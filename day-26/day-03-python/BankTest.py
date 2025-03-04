
from Solution import Bank, Account

def main():
    bank = Bank()
    # Create two accounts: Account A ("A1") with balance 1000, Account B ("B1") with balance 500.
    accountA = Account("A1", "Alice", 1000.0)
    accountB = Account("B1", "Bob", 500.0)
    bank.addAccount(accountA)
    bank.addAccount(accountB)
    
    # Test findAccount
    if bank.findAccount("A1") is not None:
        print("Test 1: Account A found successfully.")
    else:
        print("Test 1: Error - Account A not found.")
    
    # Test successful transfer: Transfer 300 from A1 to B1.
    success = bank.transfer("A1", "B1", 300.0)
    if success and accountA.getBalance() == 700.0 and accountB.getBalance() == 800.0:
        print("Test 2: Transfer successful.")
    else:
        print("Test 2: Error - Transfer failed.")
    
    # Test failed transfer: Transfer 1200 from A1 (balance 700) to B1.
    success = bank.transfer("A1", "B1", 1200.0)
    if not success and accountA.getBalance() == 700.0:
        print("Test 3: Transfer correctly rejected due to insufficient funds.")
    else:
        print("Test 3: Error - Transfer should have failed but succeeded.")

main()
