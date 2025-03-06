# Subject interface
class BankAccount:
    def withdraw(self, amount):
        pass

# Real subject
class ConcreteBankAccount(BankAccount):
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self._balance}")
        else:
            print("Insufficient funds.")

# Proxy
class BankAccountProxy(BankAccount):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def withdraw(self, amount):
        if amount <= 1000:  # Check if withdrawal amount is within limit
            self._real_subject.withdraw(amount)
        else:
            print("Withdrawal amount exceeds limit.")

# Client code
real_account = ConcreteBankAccount(1500)
proxy = BankAccountProxy(real_account)

proxy.withdraw(800)   # Allowed
proxy.withdraw(900)  # Not Allowed
proxy.withdraw(3000)  # Not allowed
