class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable


    def find(self, iterable, callback):
        pass
    
    def filter(self, iterable, callback):
        arr = []
        for i in iterable:
            if callback(i):
                arr.append(i)
        return arr
    def reject(self, iterable, callback):
        pass
        
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print(evens)


squares = _.map([1,2,3,4,5,6], lambda x: x**2)
print(squares)