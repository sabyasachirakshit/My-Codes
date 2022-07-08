"""
todo: In this program, our objective is to generate an arithmetic progression series upto n terms...
!Arithmetic Progression is basically a series having common difference.
"""
limit = int(input('Arithmetic Progression Series upto how many terms?: '))
cd = int(input('Enter Common Difference:'))
lst = [1]
print(
    f'Arithmetic Progression will be generated in a list having common difference {cd}-->')
for i in range(1, limit):
    res = lst[i-1]+cd
    lst.append(res)
print(lst)
print('\nHit Enter to End.......')
input()
