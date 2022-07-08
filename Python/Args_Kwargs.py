"""
? In this program, we have implemented args and kwargs.
! *args stands for variable length argument and **kwargs stands for variable length keyworded argument
"""


def func1(name, *args, **kwargs):
    print(name)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(f'{key} is from {value}')


n = 'Sabyasachi'
a = ['Python', 'C', 'Java']
k = {'A': '1', 'B': '2', 'C': '3'}
func1(n, *a, **k)
print('\nHit Enter to End.......')
input()
