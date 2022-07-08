"""
todo: In this program, our objective is to develop a python code that enables users to check if two numbers are Anagram or not.
! Note:Two numbers are anagram if they contain same set of charcaters but in different order
? Example of Anagram numbers are : 175 and 157 
"""
import itertools as IT  # ? For Generating Permutations
num = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
temp = num
lst1 = []
while temp > 0:
    digit = temp % 10
    lst1.append(digit)
    temp //= 10
s1 = list(IT.permutations(lst1))
x1 = []
for i in s1:
    x1.append(list(i))
    new1 = []
    for i in x1:
        for j in i:
            new1.append(j)
    for i, j in enumerate(new1):
        new1[i] = str(new1[i])
    concat = ''
    i = 1
    perm1 = []
    c1 = 0
    while i <= len(new1):
        if i % len(lst1) != 0:
            concat += new1[i-1]
        else:
            concat += new1[i-1]
            perm1.append(concat)
            concat = ''
        i += 1
    for i, j in enumerate(perm1):
        perm1[i] = int(perm1[i])
for i in perm1:
    if i == num2:
        print(f'{num} and {num2} are both anagram numbers!')
        break
else:
    print(f'{num} and {num2} are not anagram numbers')
print('\nHit Enter to End.......')
input()
