"""
todo:In this program, our objective is to generate a fibonacci series upto n terms as input by user.
! Fibonacci Series is basically a series which starts from 0 followed by 1 and the rest of the upcoming elements are the summation of the previous two elements.
? Example of Fibonacci Series: 0 1 1 2 3 5 8 13 21 34 55 .....
"""
while True:
    limit = int(
        input('Enter upto how many terms(>1) you want to generate Fibonacci Series-->:'))
    if limit <= 1:
        print('Please Enter Valid Input\n')
    else:
        break
print(
    f'Your desired Fibonacci Series upto {limit} will be generated in an array:--->>>')
first_num = 0
second_num = 1
array = []
while limit != 0:
    array.append('-')
    limit -= 1
array[0] = 0
array[1] = 1
for i, j in enumerate(array):
    if i >= 2:
        array[i] = array[i-1]+array[i-2]
print(array)
print('\nHit Enter to End.......')
input()
