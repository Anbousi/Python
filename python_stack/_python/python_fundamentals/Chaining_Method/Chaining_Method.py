class User:		# here's what we have so far
    def __init__(self, name, email):  #this is the constructor "each class have one constructor"
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit  #this is the method 1
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    # adding the widthrow method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("name:",self.name,"balance:", self.account_balance )
        return self
    
    def transfer_money_method(self , other_user , amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print("name:",self.name,"Transfer", amount ,"To","name:",other_user.name,"balance:", other_user.account_balance )
        return self
        
        
    


Mahmoud = User(email = "anb@gmail.com" , name ="Mahmoud")
Tamara = User(email = "Tamara@gmail.com" , name ="Tamara")
Lana = User(email = "Lana@gmail.com" , name ="Lana")


Mahmoud.make_deposit(500).make_deposit(300).make_deposit(500).make_withdrawal(300).transfer_money_method(Tamara, 300).display_user_balance()

Tamara.make_deposit(200).make_deposit(600).make_withdrawal(300).make_withdrawal(100).display_user_balance()

Lana.make_deposit(400).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()




# vv = vars(Mahmoud) #to print all vlues at one time
# for i in vv:       # convert to variable "Dictionary" >>> vars
#     print(i, vv[i])

