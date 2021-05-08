from Bank_Account import BankAccount
class User:		# here's what we have so far
    def __init__(self, name, email):  #this is the constructor "each class have one constructor"
        self.name = name
        self.email = email
        self.account = [BankAccount(interest_rate = 0.02, balance = 0)] #make a banks list for multiple accounts

    def make_deposit(self, amount , account_num):
        self.account[account_num].deposit(amount) #for multiple accounts for same user []list

    def new_account(self):
        self.account.append(BankAccount(interest_rate = 0.02, balance = 0))
    
    def make_withdrawal(self, amount , account_num):
        self.account[account_num].withdraw(amount)
    
    def display_user_balance(self , account_num):
        self.account[account_num].display_account_info(account_num ,self.name)
    
    # def transfer_money_method(self , other_user , amount):
    #     if self.account[account_num].account_balance > amount:
    #         self.make_withdrawal(amount)
    #         other_user.make_deposit(amount)
    #     else:
    #         print("No sufficient money")

Mahmoud = User("Mahmoud" , "anbousi@gmail.com")
Amro = User("Amro" , "sadadas@asdsa.asd")
Mahmoud.make_deposit(500,0)
Mahmoud.display_user_balance(0)

# Amro.display_user_balance(0)
# Mahmoud.display_user_balance(0)

Mahmoud.new_account()
Mahmoud.make_deposit(1000,1)
Mahmoud.display_user_balance(1)
    
