class BankAccount:
    account_number_counter = 1000  # Class-level counter for unique account numbers

    def __init__(self, name, balance=0):
        self.account_number = BankAccount.account_number_counter
        BankAccount.account_number_counter += 1
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.02):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        months = int(input("Enter the number of months to apply interest: "))
        interest = self.balance * self.interest_rate * months
        self.deposit(interest)
        print(f"Interest of {interest:.2f} applied for {months} months. New balance is {self.balance:.2f}.")


class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=100000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")
            else:
                print("Exceeded overdraft limit.")
        else:
            print("Withdrawal amount must be positive.")
