class DigitalWallet:
    def __init__(self):
        self.balance = 0.0
        self.transaction_history = []

    def initialize_wallet(self):
        self.balance = 0.0
        self.transaction_hispyttory = []
        print("Wallet initialized with balance 0 and empty transaction history.")

    def display_balance(self):
        print(f"Current balance: {self.balance:.1f}")

    def add_funds(self, input_line):
        try:
            amount = float(input_line.split('=')[1].strip())
            if amount > 0:
                self.balance += amount
                self.transaction_history.append("+" + str(round(amount, 1)))
                print(f"Balance updated to {self.balance:.1f}, transaction history logged.")
            else:
                print("Invalid amount. Transaction not recorded.")
            
        except Exception as e:
            print(f"Error in add_funds: {e}")

    def make_payment(self, input_line):
        try:
            amount = float(input_line.split('=')[1].strip())
            if amount > 0 and self.balance >= amount:
                self.balance -= amount
                # Round the amount to 1 decimal place if second digit is zero, else to 2 decimal places
                formatted_amount = f"{round(amount, 2):.2f}" if amount % 1 != 0 else f"{round(amount, 1):.1f}"
                self.transaction_history.append(f"-{formatted_amount}")
                print(f"Balance updated to {self.balance:.1f}, transaction history logged.")
            elif amount <= 0:
                print("Invalid amount. Transaction not recorded.")
            else:
                print("Insufficient balance. Transaction not recorded.")
        except Exception as e:
            print(f"Error in make_payment: {e}")

    def view_transaction_history(self):
        if self.transaction_history:
            print(f"[{', '.join(self.transaction_history)}]")
        else:
            print([])

    def run_wallet_operations(self):
        while True:
            try:
                line = input().strip()  # Read the first input
                if line == "STOP":
                    break

                if line.startswith("Method:"):
                    method_name = line.split(":")[1].strip()
                    inputs_line = input().strip()  # Read the second input

                    if method_name == "initialize_wallet":
                        self.initialize_wallet()
                    elif method_name == "add_funds":
                        self.add_funds(inputs_line)
                    elif method_name == "make_payment":
                        self.make_payment(inputs_line)
                    elif method_name == "view_transaction_history":
                        self.view_transaction_history()
                    elif method_name == "display_balance":
                        self.display_balance()
                    else:
                        print("Invalid method name.")
                else:
                    print("Invalid input format. Please start with 'Method:'.")
            except EOFError:
                
                break
            except Exception as e:
                print(f"Error: {e}")


# Main Execution
if __name__ == "__main__":
    wallet = DigitalWallet()
    wallet.run_wallet_operations()
