from bank_account import BankAccount

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