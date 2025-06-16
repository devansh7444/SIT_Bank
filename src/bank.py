class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_acc_num = 1001

    def create_account(self, name, initial):
        acc_num = str(self.next_acc_num)
        self.accounts[acc_num] = {"name": name, "balance": float(initial)}
        self.next_acc_num += 1
        return acc_num

    def deposit(self, acc_num, amount):
        if acc_num not in self.accounts:
            raise Exception("Account not found.")
        self.accounts[acc_num]["balance"] += float(amount)

    def withdraw(self, acc_num, amount):
        if acc_num not in self.accounts:
            raise Exception("Account not found.")
        if self.accounts[acc_num]["balance"] < float(amount):
            raise Exception("Insufficient funds.")
        self.accounts[acc_num]["balance"] -= float(amount)

    def get_balance(self, acc_num):
        if acc_num not in self.accounts:
            raise Exception("Account not found.")
        return self.accounts[acc_num]["balance"]