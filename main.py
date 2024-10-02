#simple banking app for cli
#! /usr/bin/python
from bank_account import BankAccount
from checking import Checking
from saving import Saving
    

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

