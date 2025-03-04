class DigitalWallet:
    def __int__(self):
        self.balance = 0.0
        self.trasaction_history = []
    def initialize_wallet(self):
        # print("hi")
        self.balance = 0.0
        self.trasaction_history = []
        print("Wallet initialized with balance 0 and empty transaction history.")
    def add_funds(self, amount):
        amount = amount.split("=")
        amount = amount[-1]
        self.balance+=int(amount)
        print(f"Balance updated to {self.balance}, transaction history logged.")

    def run_wallet_transactions(self):
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
                        self.initialize_wallet()
                    elif start == "add_funds":
                        self.add_funds(inputs_line)
                    elif start == "make_payment":
                        self.makePayment(inputs_line)
                    elif start == "view_transaction_history":
                        self.viewTransactionHistory()
                    elif start == "display_balance":
                        self.displayBalance()
            except:
                break

if __name__ == "__main__":
    c = DigitalWallet()
    c.run_wallet_transactions()