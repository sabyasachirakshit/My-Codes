"""
? In this program, we have implemented Hybrid inheritance of class!
! Hybrid Inheritance means mixture of multiple and multilevel inheritance!
"""


class A:
    a1 = 10
    b = 20


class B(A):
    c = 10
    d = 40


class C(A):
    f = 30
    g = 60


class D(B, C):
    h = 70
    k = 100

    def sum_all(self):
        return self.a1+self.b+self.c+self.d+self.f+self.g+self.h+self.k


d = D()
print(d.sum_all())
print('\nHit Enter to End.......')
input()
