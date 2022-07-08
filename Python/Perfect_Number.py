"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is perfect or not.
todo: User can also generate all perfect number within a desired range if he wants to..
! Note: A number is perfect if the sum of every factors except the number itself is equal to that number.
? Example of Perfect Number is : 6 [1 + 2 + 3 = 6]
"""
print('1.Check if a number is perfect or not')
print('2.Generate perfect number within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    num = int(input('Enter perfect number:'))
    lst = []
    for i in range(1, num):
        if(num % i == 0):
            lst.append(i)
        else:
            continue
    sumx = 0
    for i, j in enumerate(lst):
        sumx += lst[i]
    if(sumx == num):
        print('Perfect Number')
    else:
        print('Not a Perfect Number!')
elif choice == 2:
    print('All Perfect numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Perfect numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        lst = []
        for i in range(1, minx):
            if(minx % i == 0):
                lst.append(i)
            else:
                continue
        sumx = 0
        for i, j in enumerate(lst):
            sumx += lst[i]
        if(sumx == minx):
            print(minx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
