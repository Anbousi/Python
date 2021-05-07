def insertion_sort(list):
    for i in range(1,len(list)):
        print(list)
        print(list[i])
        k = i # to represent the index value "i" and decrease it later without changing the value of "i" itself
        #to keep checking values to the left of the "i" until reach zero index
        for j in range(i-1 , -1 , -1): 
            if list[j] > list[k]:
                list[j] , list[k] = list[k] , list[j]
                print("swap" ,list[j], list[k])
                k -= 1
        print(list , "\n")

arr = [6, 5, 4, 3, 7, 1, 9, 8, 2]

x = insertion_sort(arr)
print(x)