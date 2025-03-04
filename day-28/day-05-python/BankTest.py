from datetime import datetime
from Solution import Account, SavingsAccount, CurrentAccount, LoanAccount, Transaction, Person, Bank

def main():
    bank = Bank()
    
    # Create Persons
    alice = Person("P1", "Alice")
    bob = Person("P2", "Bob")
    
    # Create Accounts
    alice_savings = SavingsAccount("S1", alice, 1000.0, 0.04)
    bob_current = CurrentAccount("C1", bob, 500.0, 300.0)
    alice_loan = LoanAccount("L1", alice, 3000.0, 0.08)
    
    # Link accounts to persons and add them to the bank.
    alice.addAccount(alice_savings)
    alice.addAccount(alice_loan)
    bob.addAccount(bob_current)
    bank.addAccount(alice_savings)
    bank.addAccount(bob_current)
    bank.addAccount(alice_loan)
    
    # Test Deposit: Deposit 200 to Alice's Savings; expected balance: 1200.
    alice_savings.deposit(200.0)
    if alice_savings.getBalance() == 1200.0:
        print("Test 1: Deposit successful in Alice's Savings Account.")
    else:
        print("Test 1: Error - Deposit failed in Alice's Savings Account.")
    
    # Test Withdrawal: Bob's CurrentAccount withdraws 600 (allowed via overdraft).
    success = bob_current.withdraw(600.0)
    if success and bob_current.getBalance() == (500.0 - 600.0):
        print("Test 2: Withdrawal successful in Bob's Current Account.")
    else:
        print("Test 2: Error - Withdrawal failed in Bob's Current Account.")
    
    # Test Transfer: Transfer 300 from Alice's Savings to Bob's Current.
    success = bank.transfer("S1", "C1", 300.0)
    if success and alice_savings.getBalance() == 900.0 and bob_current.getBalance() == (500.0 - 600.0 + 300.0):
        print("Test 3: Transfer operation successful.")
    else:
        print("Test 3: Error - Transfer operation failed.")
    
    # Test Loan Repayment: Alice repays 500 on her LoanAccount; expected outstanding loan: 2500.
    alice_loan.repay(500.0)
    if alice_loan.getOutstandingLoan() == 2500.0:
        print("Test 4: Loan repayment successful.")
    else:
        print("Test 4: Error - Loan repayment failed.")
    
    # Test Input Validation: Negative deposit should not change balance.
    balance_before = bob_current.getBalance()
    bob_current.deposit(-100.0)
    if bob_current.getBalance() == balance_before:
        print("Test 5: Input validation for deposit works correctly.")
    else:
        print("Test 5: Error - Negative deposit affected the balance.")
    
    # Test Transaction Logging: Create a transaction and check its string.
    trans = Transaction("T100", alice_savings.accountNumber, "DEPOSIT", 200.0, datetime.now())
    trans_str = str(trans)
    if "DEPOSIT" in trans_str and "200.0" in trans_str and alice_savings.accountNumber in trans_str:
        print("Test 6: Transaction logged correctly.")
    else:
        print("Test 6: Error - Transaction logging failed.")


main()
