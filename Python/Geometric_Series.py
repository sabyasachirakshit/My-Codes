"""
todo: In this program, our objective is to generate an Geometric progression series upto n terms...
!Geometric Progression is basically a series having common ratio.
"""
limit = int(input('Geometric Progression Series upto how many terms?: '))
cr = int(input('Enter Common Ratio:'))
start = int(input('Enter first number(except 1):'))
lst = [start]
print(
    f'Geometric Progression will be generated in a list having common difference {cr}-->')
for i in range(1, limit):
    res = lst[i-1]*cr
    lst.append(res)
print(lst)
print('\nHit Enter to End.......')
input()
