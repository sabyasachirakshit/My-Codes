"""
? A Lambda Function is a samll anonymous function. A lambda function can take any number of arguments, but can have only one expression.
! There are available three functions for lambda: map,filter
Additional  Function Reduce
"""
from functools import reduce
def addx(a, b): return a+b


print(addx(5, 7))
def mult(a, b, c, d, e): return a*b*c*d*e


print(mult(1, 2, 3, 4, 5))
fruit = ["Apple", "Banana", "Pear", "Apricot"]
map_object = map(lambda s: s[0] == "A", fruit)
print(list(map_object))
fruit = ["Apple", "Banana", "Pear", "Apricot"]
map_object = filter(lambda s: s[0] == "A", fruit)
print(list(map_object))


def add(x, y):
    return x+y


lst = [2, 4, 7, 3]
print(reduce(add, lst))
# ! Using Reduce in lambda function
lst = [2, 4, 7, 3]
print(reduce(lambda x, y: x+y, lst))
print("With an initial value:"+str(reduce(lambda x, y: x+y, lst, 10)))
print('\nHit Enter to End.......')
input()
