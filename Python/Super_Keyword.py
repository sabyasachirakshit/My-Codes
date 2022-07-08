"""
? In this program, we will implement super keyword
! super keyword is used to call the parent class function in case both parent and child class has same functions..
"""


class parent:
    def func1(self):
        print('This is Parent CLass Function')


class child(parent):
    def func1(self):
        print('This is child class function')

    def func2(self):
        super().func1()
        self.func1()
        print('This is child class function no.2')


c = child()
c.func2()
print('\nHit Enter to End.......')
input()
