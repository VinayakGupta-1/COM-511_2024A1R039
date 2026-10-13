# Q4. Create a BankAccount class that stores an account holder's name and balance.
# Add instance methods to deposit money, withdraw money, and display the balance.
# Do not allow a withdrawal greater than the available balance.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


b1 = BankAccount("Rahul", 5000)

b1.deposit(1000)
b1.withdraw(2000)
b1.display()