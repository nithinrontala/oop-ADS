class DigitalWallet:
    def __init__(self):
        self.walletBalance = 0.0
        self.transactionHistory = []

    def intializeWallet(self):
        self.walletBalance = 0.0
        self.transactionHistory = []
        print("Wallet initialized with balance 0 and empty transaction history.")

    def displayBalance(self):
        print(f"Current balance: {self.walletBalance}")
    
    def addFunds(self, amount):
        amount = amount.split("=")
        amount = amount[-1]
        if (int(amount)>0):
            self.walletBalance +=int(amount)
            self.transactionHistory.append(f"+{float(amount)}")
            print(f"Balance updated to {self.walletBalance}, transaction history logged.")
        else:
            print("Invalid amount. Transaction not recorded.")
        
    def makePayment(self, amount):
        amount = amount.split("=")
        amount = amount[-1]             
        if self.walletBalance >= int(amount) and int(amount)>0:
            self.walletBalance-=int(amount)
            self.transactionHistory.append(f"-{float(amount)}")
            print(f"Balance updated to {self.walletBalance}, transaction history logged.")
        else:
            print("Insufficient balance. Transaction not recorded.")

    def viewTransactionHistory(self):
        print(f"[{', '.join(self.transactionHistory)}]")

    def run_wallet_operations(self):
        while True:
            try:
                line = input().strip()  

                if line[0:7]=="Method:":
                    start = line.split(":")
                    start = start[-1].strip()
                    # print(start)
                    inputs_line = input().strip()  
                    # print(inputs_line)
                    if start == "initialize_wallet":
                        self.intializeWallet()
                    elif start == "add_funds":
                        self.addFunds(inputs_line)
                    elif start == "make_payment":
                        self.makePayment(inputs_line)
                    elif start == "view_transaction_history":
                        self.viewTransactionHistory()
                    elif start == "display_balance":
                        self.displayBalance()
            except:
                break

if __name__ == "__main__":
    w = DigitalWallet()
    w.run_wallet_operations()
