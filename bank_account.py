class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def add_to_balance(self):
        deposit = int(input("How much money would you like to deposit? $"))
        self.balance += deposit
        print(f"${deposit} has been added to your balance. New balance is ${self.balance}")
        return self.balance

    def view_balance(self):
        print(f"Your current balance is: ${self.balance} \n")