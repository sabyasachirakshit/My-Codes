"""
? In this program, we have implemented hierarchial inheritance of class!
! Hierarchial Inheritance means when multiple child class inherits from single parent class..
"""


class Base:
    a = 10
    b = 20


class Derived1(Base):  # ! Hierarchial Inheritance
    def sum(self):
        add = self.a+self.b
        print('Addition:', add)


class Derived2(Base):  # ! Hierarchial Inheritance
    def mul(self):
        mul = self.a*self.b
        print('Multiplication:', mul)


da = Derived1()
db = Derived2()
da.sum()
db.mul()
print('\nHit Enter to End.......')
input()
