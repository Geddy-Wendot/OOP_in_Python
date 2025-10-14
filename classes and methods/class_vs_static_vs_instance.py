'''OOP Challenge: Build a BankAccount System

Goal:
Create a BankAccount class that models a simple banking system.
You must demonstrate the use of instance methods, class methods, and static methods.

🧱 Requirements
Attributes
Every account should have:
owner (the account holder’s name)
balance (default: 0)
The class should track:
The bank_name (same for all accounts)
The interest_rate (e.g. 0.03)
The total_accounts (how many accounts have been created)

Methods
Instance methods
deposit(amount) → adds to balance (only if amount is valid)
withdraw(amount) → subtracts from balance (only if sufficient funds)
apply_interest() → applies interest to the balance

Class methods
set_interest_rate(new_rate) → updates the interest rate for all accounts
get_total_accounts() → returns how many accounts exist

Static method
is_valid_amount(amount) → returns True if amount is a positive number, otherwise False

Extra (optional but good practice)
Override __str__ so printing an account shows its details neatly.
Handle edge cases (like trying to withdraw too much or deposit invalid data).

🎯 Example Run (for testing your work)
acc1 = BankAccount("Geddy", 1000)
acc2 = BankAccount("Wendot", 500)

print(acc1.deposit(200))
print(acc2.withdraw(100))
print(acc1.apply_interest())

print(BankAccount.set_interest_rate(0.05))
print(acc2.apply_interest())

print(BankAccount.get_total_accounts())


Expected output (roughly):

Geddy deposited 200. New balance: 1200
Wendot withdrew 100. New balance: 400
Interest applied: 36.00. New balance: 1236.00
New interest rate set to 5.0%
Interest applied: 20.00. New balance: 420.00
Total accounts: 2'''

class BankAccount:
    # class attributes
    bank_name = "Co-operative bank"
    interest_rate = 0.03
    total_accounts = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance if balance else 0
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if not BankAccount.is_valid_amount(amount):
            raise ValueError("Invalid deposit amount")
        self.balance += amount
        return f"{self.owner} deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if not BankAccount.is_valid_amount(amount):
            raise ValueError("Invalid withdrawal amount")
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return f"{self.owner} withdrew {amount}. New balance: {self.balance}"

    def apply_interest(self):
        interest = BankAccount.interest_rate * self.balance
        self.balance += interest
        return f"Interest applied: {interest:.2f}. New balance: {self.balance:.2f}"

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        return f"New interest rate set to {new_rate*100}%"

    @classmethod
    def get_total_accounts(cls):
        return f"Total accounts: {cls.total_accounts}"

    @staticmethod
    def is_valid_amount(amount):
        return isinstance(amount, (float, int)) and amount > 0

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}, Bank: {BankAccount.bank_name}"

# Create two accounts
acc1 = BankAccount("Geddy", 1000)
acc2 = BankAccount("Wendot", 500)

print(acc1.deposit(200))
print(acc2.withdraw(100))
print(acc1.apply_interest()) 

# Change interest rate for everyone
print(BankAccount.set_interest_rate(0.05))
print(acc2.apply_interest())

# Check total accounts
print(BankAccount.get_total_accounts())



