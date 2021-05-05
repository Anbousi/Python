print("Hello World!")
f_name = "Mahmoud"
num = 5
print("My name is ", f_name , "--with comma")
print("My name is "+ f_name , "--with +")

print("My fav num is", num , "--with comma")
#print("My fav num is" + num , "--with +") #not recognized , not working
print("My fav num is" + str(num) , "--with +") #str will convert the num to string and solve the problem

y = "Rice"
z = "Potato"
print("I love eat {} and {}".format(y , z))
print(f"I love eat {y} and {z}")