    # If no arguments are provided, the function should return a random integer between 0 and 100.
    # If only a max number is provided, the function should return a random integer between 0 and the max number.
    # If only a min number is provided, the function should return a random integer between the min number and 100
    # If both a min and max number are provided, the function should return a random integer between those 2 values.

    #print(randInt()) 		    # should print a random integer between 0 to 100
    #print(randInt(max=50)) 	    # should print a random integer between 0 to 50
    #print(randInt(min=50)) 	    # should print a random integer between 50 to 100
    #print(randInt(min=50, max=500))    # should print a random integer between 50 and 500


import random
def randInt(min=0 , max=100):
    if max<0:
        print("max is less than zero")
        return False
    if min > max:
        temp = min
        min = max
        max = temp
        print("min and max are switched")

    num = random.random()*(max-min) + min
    num = round(num)
    return num

x = randInt()
print ("x =",x)
y = randInt(max=10)
print ("y =",y)
z = randInt(min=90)
print("z =",z)
k = randInt(min = 50 , max = 60)
print("k =",k)
f = randInt(min = 80 , max = 60)
print("f =",f)
g = randInt(min = 80 , max = -60)
print("g =",g)




