# create a program that simulates a basic ATM machine. The user should be able to check their balance, deposit and withdraw money. Use functions to handle each operation

class ATM():
    def __init__(self, balance):
        self._balance = balance

    def deposit(self):
        try:
            amount_deposit = float(input("Type the amount you would like to deposit? "))
            if amount_deposit > 0:
                self._balance += amount_deposit
                return f"\n{amount_deposit}e was deposit into your account. \n"
            elif amount_deposit <= 0: 
                return f"Error, invalid operation. \n"
        except:
            print("Invalid input, please enter a valid number.")

    def withdraw(self):
        transaction = False
        while not transaction:
            withdraw_money = float(input("Type the amount you would you like to withdraw? "))
            if withdraw_money > self._balance:
                print(f"Operation failed, Your credential are not sufficient for this transaction. Please select a lower amount.")
            else:
                self._balance -= withdraw_money
                transaction = True
                return f"'{withdraw_money} euros' was withdrawned from your account. \n"

    def check_balance(self):
        return f"You have a balance of '{self._balance} euros' in your account. \n"
        

Marc = ATM(100)

while True:
    operation = input("Enter your operation (deposit, withdraw, balance, quit): ")
    if operation.lower() == "deposit":
        print(Marc.deposit())
    elif operation.lower() == "withdraw":
        print(Marc.withdraw())
    elif operation.lower() == "balance":
        print(Marc.check_balance())
    elif operation.lower() == "quit":
        print("Thank you, goodbye!")
        break
    else:
        print("Invalid operation. Please try again.")
