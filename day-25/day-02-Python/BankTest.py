
from Solution import Account, SavingsAccount, CurrentAccount

def testpart1():
    # Create an Account with accountNumber "A1", accountHolder "Alice", initial balance 1000.0
    acc = Account("A1", "Alice", 1000.0)
    
    # Test Deposit: deposit 500; expected balance: 1500.0
    acc.deposit(500.0)
    if acc.getBalance() == 1500.0:
        print("Test 1: Deposit successful.")
    else:
        print("Test 1: Error - Deposit did not update balance correctly.")
    
    # Test Withdrawal: withdraw 300; expected balance: 1200.0; withdrawal returns True.
    success_withdraw = acc.withdraw(300.0)
    if success_withdraw and acc.getBalance() == 1200.0:
        print("Test 2: Withdrawal successful.")
    else:
        print("Test 2: Error - Withdrawal failed or balance incorrect.")
    
    # Test Withdrawal Exceeding Balance: attempt to withdraw 2000 (should fail)
    fail_withdraw = acc.withdraw(2000.0)
    if not fail_withdraw and acc.getBalance() == 1200.0:
        print("Test 3: Properly handled insufficient funds.")
    else:
        print("Test 3: Error - Withdrawal allowed without sufficient funds.")
    
    # Test Deposit Negative Amount: deposit -100; balance should remain unchanged.
    balance_before = acc.getBalance()
    acc.deposit(-100.0)
    if acc.getBalance() == balance_before:
        print("Test 4: Negative deposit rejected.")
    else:
        print("Test 4: Error - Negative deposit affected the balance.")


def testpart2():
    # Test SavingsAccount
    sa = SavingsAccount("S1", "Bob", 1000.0, 0.05)
    interest = sa.calculateInterest()
    if interest == 50.0:
        print("Test 1: SavingsAccount interest calculated correctly.")
    else:
        print("Test 1: Error - Incorrect interest calculation. Expected 50.0, got", interest)
    
    # Test CurrentAccount: Create with balance 1000 and overdraft limit 500.
    ca = CurrentAccount("C1", "Carol", 1000.0, 500.0)
    success = ca.withdraw(1300.0)  # expected new balance = 1000 - 1300 = -300
    if success and ca.getBalance() == -300.0:
        print("Test 2: CurrentAccount overdraft withdrawal successful.")
    else:
        print("Test 2: Error - Overdraft withdrawal failed or balance incorrect.")
    
    # Test CurrentAccount: Attempt to withdraw an excessive amount (250, when available is 200)
    success = ca.withdraw(250.0)
    if not success and ca.getBalance() == -300.0:
        print("Test 3: Properly rejected excessive withdrawal in CurrentAccount.")
    else:
        print("Test 3: Error - Excessive withdrawal was allowed.")


testpart1()
testpart2()
