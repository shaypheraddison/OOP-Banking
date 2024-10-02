#simple banking app for cli
#! /usr/bin/python
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

    
class Checking(BankAccount):
    def __init__(self, balance, has_overdraft_protection):
        super().__init__(balance)
        self.has_overdraft_protection = has_overdraft_protection

    def remove_from_balance(self):
        withdraw = int(input("How much would you like to take out of your balance? $"))
        if withdraw > self.balance and self.has_overdraft_protection == False or self.has_overdraft_protection == True:
            print("There is not enough money to withdraw, please deposit more first. Don't forget to sign up for Overdraft Protection too!")
        else:
            self.balance -= withdraw
            print(f"${withdraw} has been removed from your balance.")
            print(f"New balance is ${self.balance}")

        return self.balance



class Saving(BankAccount):
    interest_rate = 1.04

    def apply_interest(self):
        years_open = int(input("How many years has this account been open? "))
        if years_open == 0:
            print("No interest has been accrued just yet, come back later")
            return self.balance
        else:
            new_balance = (years_open * Saving.interest_rate) * self.balance
            self.balance = new_balance
            print(f"Interest applied to account! New Savings balance is: {new_balance:.2f}")

        return self.balance
    
    
while True: 
    print("1. Checking Account \n2. Savings Account \n3. Exit")
    account_type = int(input("Please select an account type: "))

    if account_type == 1:
        starting_balance = int(input("How much will your starting balance be? $"))
        checking = Checking(starting_balance, True)

        while True: 
            print("1. Check Balance \n2. Deposit \n3. Withdraw \n4. Exit")
            choice_1 = int(input("Please select an option: "))
            if choice_1 == 1:
                checking.view_balance()
            elif choice_1 == 2:
                checking.add_to_balance()
            elif choice_1 == 3:
                checking.remove_from_balance()
            elif choice_1 == 4:
                print("Closing out of app now. Thank you!")
                break
            else:
                print("Please select a correct option.")
    
    if account_type == 2:
        starting_balance = int(input("How much will your starting balance be? $"))
        saving = Saving(starting_balance)

        while True:
            print("1. Check Balance \n2. Deposit \n3. Exit")
            choice_2 = int(input("Please select an option: "))
            if choice_2 == 1:
                saving.view_balance()
            elif choice_2 == 2:
                saving.add_to_balance()
                saving.apply_interest()
            elif choice_2 == 3:
                print("Closing out of app. Thank you!")
                break
            else:
                print("Please select a correct option.")

    if account_type == 3:
        print("Thank you for visiting the bank today!")
        break

