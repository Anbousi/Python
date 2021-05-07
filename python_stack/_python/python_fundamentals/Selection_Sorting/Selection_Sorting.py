def selection_sorting(arr):
    k = None
    for j in range (len(arr)):
        # print("Iteration num: ", j)
        min = arr[j]
        for i in range (j,len(arr)):
            #print ("i = ", i ,"---","j = ", j)
            if arr[i]<min:
                min = arr[i]
                k = i
        # print("min value =", min , "index of :", k ,"\n")
        arr[j] , arr[k] = arr [k] , arr[j]
    return arr

arr = [8,5,2,6,9,3,1,4,7]
x = selection_sorting(arr)
print (x)


