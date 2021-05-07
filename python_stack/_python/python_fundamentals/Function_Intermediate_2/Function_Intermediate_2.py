# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1-1- Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# 1-2- Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)

# 1-3- In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

# 1-4- Change the value 20 in z to 30
z[0]["y"] = 30
print(z)

#==========================================================

#2-Iterate Through a List of Dictionaries
def iterateDictionary(a):

    # for i  in a :
    #     for key , value in i.items():
    #         print (f"first_name - {key}, last_name - {value}")

    for i in a:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")
    
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
x = iterateDictionary(students)
print(x)


#==========================================================

#3-Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    if key_name == "first_name":
        for i in some_list:
            print(f"{i['first_name']}")
    elif key_name == "last_name":
        for i in some_list:
            print(f"{i['last_name']}")
    else:
        return "please specify first or last name"

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
x = iterateDictionary2( 'first_name' , students)
print(x)
y = iterateDictionary2( 'last_name' , students)
print(y)

#==========================================================

#4-Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    for key , value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for i in value:
            print(i)
        print("\n")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

x= printInfo(dojo)
print (x)
