from bank_account import BankAccount

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