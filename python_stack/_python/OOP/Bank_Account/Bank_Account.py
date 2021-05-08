class BankAccount:
    def __init__(self ,interest_rate = 0.01 , amount = 0):
        self.account_balance = amount
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

    def display_account_info(self):   
        print(f"Account balance = {self.account_balance}")

    def yield_interest(self):
        if (self.account_balance) > 0:
            self.account_balance = (self.account_balance * self.intrest) + self.account_balance
            return self

Account1 = BankAccount(amount = 1000)
Account2 = BankAccount(amount = 1500)
Account3 = BankAccount(amount = 1300) 
Account1.deposit(200).deposit(500).deposit(800).withdraw(1300).display_account_info()
Account2.deposit(600).deposit(400).withdraw(1000).withdraw(500).withdraw(200).withdraw(500).display_account_info()