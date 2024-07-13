class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_balance(self):
        """Return the current balance."""
        return self.balance

    def cash_withdrawal(self, amount):
        """Withdraw cash if sufficient balance is available."""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal: ${amount}')
            return True
        else:
            return False

    def cash_deposit(self, amount):
        """Deposit cash into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit: ${amount}')
            return True
        else:
            return False

    def change_pin(self, new_pin):
        """Change the PIN."""
        self.pin = new_pin
        self.transaction_history.append('PIN changed')

    def show_transaction_history(self):
        """Display transaction history."""
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

# Example usage:
if __name__ == "__main__":
    # Create an instance of ATM
    atm = ATM(balance=1000, pin='1234')

    # Example operations
    print(f"Current balance: ${atm.check_balance()}")

    # Withdraw cash
    withdraw_amount = 200
    if atm.cash_withdrawal(withdraw_amount):
        print(f"Withdrew ${withdraw_amount}. New balance: ${atm.check_balance()}")
    else:
        print(f"Insufficient funds to withdraw ${withdraw_amount}. Balance: ${atm.check_balance()}")

    # Deposit cash
    deposit_amount = 500
    if atm.cash_deposit(deposit_amount):
        print(f"Deposited ${deposit_amount}. New balance: ${atm.check_balance()}")

    # Change PIN
    new_pin = '4321'
    atm.change_pin(new_pin)
    print("PIN changed successfully.")

    # Display transaction history
    print("Transaction history:")
    atm.show_transaction_history()
