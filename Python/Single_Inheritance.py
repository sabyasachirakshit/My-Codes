"""
? In this program, we have implemented single inheritance of class!
! Single Inheritance means when single child class inherits from single parent class..
"""


class Base:
    def cal_sum(self, a, b):
        return a+b


class Derived(Base):  # ! Single Inheritance
    def cal_mul(self, a, b):
        return a*b


n1 = int(input('Enter 1st number:'))
n2 = int(input('Enter 2nd number:'))
d = Derived()
print('(From Base Class) Addition:', d.cal_sum(n1, n2))
print('(From Derived Class) Multiplication:', d.cal_mul(n1, n2))
print('\nHit Enter to End.......')
input()
