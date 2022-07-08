"""
todo: In this program, our objective is to develop a python code that generates all possible permutations of a number!
"""
import itertools as IT  # ! to Generate Permutations
num = int(input('Enter a number whose permutations are required:'))
print('The possible permutations will be generated inside a list..(please wait for a moment if number of digits are more than 5)..')
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
print('Generated Permutations Count:', len(perm1))
print(perm1)
print('\nHit Enter to End.......')
input()
