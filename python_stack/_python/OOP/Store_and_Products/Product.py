class Product:
    def __init__(self, name , price , category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change , is_increased):
        if is_increased == True:
            self.price += self.price*percent_change
        elif is_increased == False:
            self.price -= self.price*percent_change
    
    def print_info(self):
        print("Product name: ",self.name)
        print("Product category: ",self.category)
        print("Product price: ",self.price)

laptop = Product("Laptop" , 3000 ,"Electronics")
# laptop.print_info()
