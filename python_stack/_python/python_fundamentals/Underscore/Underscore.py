class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable

    def find(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable

    def filter(self, iterable, callback):
        arr = []
        for i in iterable:
            if callback(i):
                arr.append(i)
        return arr

    def reject(self, iterable, callback):
        arr = []
        for i in iterable:
            if callback(i):
                arr.append(i)
        return arr
        
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
filter = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print("filter: ",filter)

squares = _.map([1,2,3,4,5,6], lambda x: x**2)
print("squares: ",squares)

find = _.find([1,2,3,4,5,6], lambda x: x>4)
print("find x>4: ",find)

reject = _.reject([1,2,3,4,5,6], lambda x: x%2==1)
print("reject: ",reject)
