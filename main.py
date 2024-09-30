#simple banking app for cli

class BankAccount:
    def __init__(self, balance, allow_both_transactions):
        self.balance = balance
        self.allow_both_transactions = allow_both_transactions

    
class Checking(BankAccount):
    def add_to_balance(self):
        deposit = int(input("How much money would you like to deposit? \n$"))
        self.balance += deposit
        return self.balance

    def remove_from_balance(self):
        withdraw = int(input("How much would you like to take out of your balance? \n$"))
        self.balance -= withdraw
        return self.balance
        
    def view_balance(self):
        print(self.balance)
    

c1 = Checking(0, True)
c1.add_to_balance()
c1.view_balance()
c1.remove_from_balance()
c1.view_balance()