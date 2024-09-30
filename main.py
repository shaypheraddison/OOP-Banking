#simple banking app for cli
#! /usr/bin/python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def view_balance(self):
        print(f"Your current balance is: ${self.balance}")

    
class Checking(BankAccount):

    def add_to_balance(self):
        deposit = int(input("How much money would you like to deposit? $"))
        self.balance += deposit
        print(f"${deposit} has been added to your balance.")
        return self.balance

    def remove_from_balance(self):
        withdraw = int(input("How much would you like to take out of your balance? $"))
        if withdraw > self.balance:
            print("There is not enough money to withdraw, please deposit more first.")
        else:
            self.balance -= withdraw
            print(f"${withdraw} has been removed from your balance.")

        return self.balance

class Saving(BankAccount):
    
    pass
    

starting_bal = int(input("Please set your starting balance: $"))
c1 = Checking(starting_bal)
c1.add_to_balance()
c1.view_balance()
c1.remove_from_balance()
c1.view_balance()