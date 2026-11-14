"""
05 - Bank Account: Objects Protect Their Data
Methods can ENFORCE RULES (no negative deposits, no overdrafts), which is
safer than letting any code change the data directly.
"""


class BankAccount:
    interest_rate = 0.02          # a CLASS attribute: shared by every account

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []         # a list of (type, amount) tuples

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return False
        self.balance += amount
        self.history.append(("deposit", amount))
        return True

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds: balance is ${self.balance:.2f}")
            return False
        self.balance -= amount
        self.history.append(("withdraw", amount))
        return True

    def transfer(self, other, amount):
        """Move money from this account to another account object."""
        if self.withdraw(amount):
            other.deposit(amount)
            return True
        return False

    def add_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.deposit(interest)

    def statement(self):
        print(f"--- {self.owner}'s statement ---")
        for kind, amount in self.history:
            print(f"  {kind:<9} ${amount:>8.2f}")
        print(f"  Balance:  ${self.balance:>8.2f}")

    def __str__(self):
        return f"{self.owner}: ${self.balance:.2f}"


alice = BankAccount("Alice", 100)
bob = BankAccount("Bob")

alice.deposit(50)
alice.deposit(-10)           # rejected
alice.withdraw(500)          # rejected
alice.transfer(bob, 30)
alice.add_interest()

print(alice)
print(bob)
alice.statement()

# Every account shares the class attribute:
print(alice.interest_rate, bob.interest_rate, BankAccount.interest_rate)
