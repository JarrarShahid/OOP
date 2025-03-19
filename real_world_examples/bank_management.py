# bank_management.py

import uuid

class BankAccount:
    """Represents a bank account with basic operations."""

    def __init__(self, owner_name, initial_balance=0.0):
        self.account_number = str(uuid.uuid4())[:8]  # Unique 8-character account number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []  # Stores transaction history
        print(f"🏦 Account created for {owner_name} | Account No: {self.account_number}")

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount:.2f}")
            print(f"✅ Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("❌ Invalid deposit amount!")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount:.2f}")
            print(f"✅ Withdrawn ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        else:
            print("❌ Insufficient funds or invalid amount!")

    def check_balance(self):
        """Returns the current balance."""
        print(f"💰 Account Balance for {self.owner_name}: ${self.balance:.2f}")
        return self.balance

    def show_transaction_history(self):
        """Displays all transactions."""
        print(f"\n📜 Transaction History for {self.owner_name} ({self.account_number}):")
        for transaction in self.transactions:
            print(f"🔹 {transaction}")
        if not self.transactions:
            print("📂 No transactions yet!")


class Bank:
    """Manages multiple bank accounts."""

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self, owner_name, initial_balance=0.0):
        """Creates a new bank account and stores it."""
        new_account = BankAccount(owner_name, initial_balance)
        self.accounts[new_account.account_number] = new_account
        return new_account

    def get_account(self, account_number):
        """Retrieves an account by account number."""
        return self.accounts.get(account_number, None)


# 🎯 Demonstration
if __name__ == "__main__":
    my_bank = Bank("OOP Bank")

    # Creating accounts
    alice = my_bank.create_account("Alice", 500)
    bob = my_bank.create_account("Bob", 1000)

    # Transactions
    alice.deposit(300)
    alice.withdraw(200)
    alice.check_balance()
    alice.show_transaction_history()

    bob.withdraw(500)
    bob.deposit(700)
    bob.show_transaction_history()

    # Fetch an account using account number
    account_num = alice.account_number
    fetched_account = my_bank.get_account(account_num)
    if fetched_account:
        print(f"\n🔍 Found account: {fetched_account.owner_name} | Balance: ${fetched_account.balance:.2f}")
