"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is Pronic or not.
todo: User can also generate all Pronic number within a desired range if he wants to..
! Note: A number is Pronic if the product of two consecutive integers is equal to that number!
? Example of Pronic Number is : 6 [ Product of 2 and 3 which are consecutive integer numbers]
"""
print('1.Check if a number is Pronic or not')
print('2.Generate Pronic numbers within a desired range')
flag = 1
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    number = int(input('Enter any number:'))
    factors = []
    i = 1
    while(i <= number):
        if number % i == 0:
            factors.append(i)
        i += 1
    for i in factors:
        for j in factors:
            if(i*j == number) and i == j-1:
                print('Pronic Number')
                flag = 0
                break
    if flag == 1:
        print('Non-Pronic Number')
elif choice == 2:
    print('All Pronic numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Pronic numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        factors = []
        i = 1
        while(i <= minx):
            if minx % i == 0:
                factors.append(i)
            i += 1
        for i in factors:
            for j in factors:
                if(i*j == minx) and i == j-1:
                    print(minx)
                    flag = 0
                    break
        minx += 1
else:
    print('Wrong Choice!!')
print('\nHit Enter to End.......')
input()
