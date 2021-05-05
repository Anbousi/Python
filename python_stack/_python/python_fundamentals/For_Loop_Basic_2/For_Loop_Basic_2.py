#1- Biggie Size - Given a list, 
# write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
# but whose values are now [-1, "big", "big", -5]
def biggie_size(lista):
    for i in range (len(lista)):
        if lista[i] > 0 :
            lista[i] = "big"
    return lista
x = biggie_size([-1, 3, 5, -5])
print(x)

#2-Count Positives - Given a list of numbers, 
# create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(lista):
    sum = 0
    for i in range (len(lista)):
        if lista[i]>0:
            sum += 1
    lista[-1] = sum  # same as lista[len(lista)-1] = sum
    return lista
x = count_positives([1,6,-4,-2,-7,-2])
print(x)

#3-Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(lista):
    count = 0
    for i in range(len(lista)):
        count = count + lista[i]
    return count
lista = [1,2,3,4]
x = sum_total(lista)
print("summation =",x)

#4-Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5
def average(lista):
    count = 0
    for i in range(len(lista)): #we can use --- for i in lesta   - ---- count = count + i
        count = count + lista[i]
    return count/len(lista)
lista = [1,2,3,4]
x = average(lista)
print("average =",x)

#OR OR OR OR
def average(lista):
    count = 0
    for i in lista: #we can use --- for i in lesta   - ---- count = count + i
        count = count + i
    return count/len(lista)
lista = [1,2,3,4]
x = average(lista)
print("average =",x)

#5-Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(lista):
    return len(lista)
lista = [37,2,1,-9]
x = length(lista)
print("The lenght of the list is",x)

#6-Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(lista):
    min = lista[0]
    if len(lista) == 0:
        return False
    for i in lista: #same as for i in range (len(lista))
        if i < min:
            min = i
    return min
lista = [37,2,1,-9]
x = minimum(lista)
print(x)

#7-Maximum - Create a function that takes a list and returns the maximum value in the list. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(lista):
    max = lista[0]
    if len(lista) == 0:
        return False
    for i in lista: #same as for i in range (len(lista))
        if i > max:
            max = i
    return max
lista = [37,2,1,-9]
x = maximum(lista)
print(x)

#8-Ultimate Analysis - Create a function that takes a list and returns a dictionary that 
# has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(lista):
    diction={}
    count = 0
    max = lista[0]
    min = lista[0]
    for i in lista:
        if i > max:
            max = i
        if i < min:
            min = i
        count = count + i

        dict = {
        'sumTotal' : count,
        'average' : count/len(lista),
        'minimum' : min,
        'maximum' : max,
        'length' : len(lista)
        }
    return dict
lista = [37,2,1,-9]
x = ultimate_analysis(lista)
print(x)

#9-Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(lista):
    lista = lista[::-1]
    return lista
lista = [37,2,1,-9]
x = reverse_list(lista)
print(x)






