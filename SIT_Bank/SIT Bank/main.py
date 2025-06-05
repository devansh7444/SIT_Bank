from Banking.account import BankAccount, SavingsAccount, CurrentAccount
from Banking.transaction import deposit, withdraw

accounts = {}  # Global dictionary to store accounts

def create_account():
    name = input("Enter your name: ").strip()
    acc_type = input("Enter account type (savings/current): ").strip().lower()
    initial_deposit = float(input("Enter initial deposit amount: "))
    
    if acc_type == "savings":
        acc = SavingsAccount(name, initial_deposit)
    elif acc_type == "current":
        acc = CurrentAccount(name, initial_deposit)
    else:
        print("Invalid account type. Defaulting to Savings Account.")
        acc = SavingsAccount(name, initial_deposit)

    accounts[acc.account_number] = acc
    print(f"Account created successfully. Account Number: {acc.account_number}")

def login():
    acc_number = int(input("Enter your account number: "))
    if acc_number in accounts:
        user_acc = accounts[acc_number]
        print(f"Welcome {user_acc.name}!")
        
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")        
            print("3. Check Balance")
            if isinstance(user_acc, SavingsAccount):
                print("4. Calculate Interest")
                print("5. Logout")
            else:
                print("4. Logout")

            choice = input("Choose an option: ")
            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                deposit(user_acc, amount)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                withdraw(user_acc, amount)
            elif choice == "3":
                print(f"Current Balance: {user_acc.get_balance()}")
            elif choice == "4" and isinstance(user_acc, SavingsAccount):
                user_acc.calculate_interest()
            elif (choice == "4" and not isinstance(user_acc, SavingsAccount)) or (choice == "5" and isinstance(user_acc, SavingsAccount)):
                print("Logging out...")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Account not found. Please try again.")

def main():
    print("Welcome to SBI Bank!".center(50))
    print("Nagpur SIT Branch".center(50))

    while True:
        print("\n1. Create Account")
        print("2. Login")   
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using SBI Bank. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":   
    main()
