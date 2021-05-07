class User:		# here's what we have so far
    def __init__(self, name, email):  #this is the constructor "each class have one constructor"
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit  #this is the method 1
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    # adding the widthrow method
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("name:",self.name,"balance:", self.account_balance )
        print("\n")
    
    def transfer_money_method(self , other_user , amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print("name:",self.name,"balance:", self.account_balance )
        print("name:",other_user.name,"balance:", other_user.account_balance )

Mahmoud = User(email = "anb@gmail.com" , name ="Mahmoud")
Tamara = User(name ="Tamara",email = "Tamara@gmail.com")
Lana = User("Lana","Lana@gmail.com") #when not specify the parameter name the order is important


Mahmoud.make_deposit(500)
Mahmoud.make_deposit(200)
Mahmoud.make_deposit(300)
Mahmoud.display_user_balance()
Mahmoud.make_withdrawal(300)
Mahmoud.display_user_balance()
Tamara.make_deposit(200)
Tamara.make_deposit(600)
Tamara.make_withdrawal(300)
Tamara.make_withdrawal(100)
Tamara.display_user_balance()
Lana.make_deposit(400)
Lana.make_withdrawal(100)
Lana.make_withdrawal(100)
Lana.make_withdrawal(100)

Mahmoud.transfer_money_method(Tamara, 300)


# vv = vars(Mahmoud) #to print all vlues at one time
# for i in vv:       # convert to variable "Dictionary" >>> vars
#     print(i, vv[i])










# class User:
#     def __init__(self,balance=0): #this is the constructor
#         self.balance = balance

#     def make_withdrawal(self,amount): #this is the method 1
#         self.amount = amount
#         self.balance = self.balance-amount   


    
#     def display_user_balance(self): 
#         #this is the method 2
#        ## print("Wirtdraw amount" , self.amount)
#         print("Remaining balance" , self.balance)


# if __name__ == "__main__":
