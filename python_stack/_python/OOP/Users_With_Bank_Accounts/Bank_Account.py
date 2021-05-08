class BankAccount:
    def __init__(self ,interest_rate = 0.01 , balance = 0):
        self.account_balance = balance
        self.intrest = interest_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if (self.account_balance - amount) > 0:
            self.account_balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5

    def display_account_info(self, account_num , name):   
        print(f"{name}: Account balance - Accnum = {account_num} - {self.account_balance}")

    def yield_interest(self):
        if (self.account_balance) > 0:
            self.account_balance = (self.account_balance * self.intrest) + self.account_balance
            return self
