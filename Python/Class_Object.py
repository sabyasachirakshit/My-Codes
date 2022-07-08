"""
? In this program, we will implement OOP class and objects!
"""


class Person:
    def __init__(self, name, age):  # ! Constructor
        self.name = name
        self.age = age

    def __del__(self):
        print('Destructor called! Person Deleted')

    def myfunc(self):  # ?Creating a Function
        print('Hello! My name is '+self.name+'!')


pl = Person("SABYASACHI RAKSHIT", 20)  # ?Creating Objects
print(pl.name)
print(pl.age)  # *Printing them using objects
pl.myfunc()
del pl
print('\nHit Enter to End.......')
input()
