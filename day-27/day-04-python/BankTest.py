from datetime import datetime
from Solution import Account, SavingsAccount, LoanAccount, Transaction, Person

def main():
    # Test LoanAccount: Create a Person and a LoanAccount.
    person_david = Person("P1", "David")
    loan_acc = LoanAccount("L1", person_david, 5000.0, 0.10)
    loan_acc.repay(1000.0)  # Outstanding loan should now be 4000.
    interest = loan_acc.calculateInterest()  # Expected interest = 400.0
    if loan_acc.getOutstandingLoan() == 4000.0 and interest == 400.0:
        print("Test 1: Loan repayment and interest calculation successful.")
    else:
        print("Test 1: Error - Loan repayment or interest calculation incorrect.")
    
    # Test linking a Person with an Account.
    savings_acc = SavingsAccount("S2", person_david, 2000.0, 0.03)
    person_david.addAccount(savings_acc)
    if savings_acc in person_david.getAccounts():
        print("Test 2: Account successfully linked to person.")
    else:
        print("Test 2: Error - Account not linked to person.")
    
    # Test Transaction Logging.
    transaction = Transaction("T1", savings_acc.accountNumber, "DEPOSIT", 500.0, datetime.now())
    trans_str = str(transaction)
    if "DEPOSIT" in trans_str and "500.0" in trans_str and savings_acc.accountNumber in trans_str:
        print("Test 3: Transaction logged correctly.")
    else:
        print("Test 3: Error - Transaction log details are incorrect.")

main()
