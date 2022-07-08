"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is armstrong or not.
todo: User can also generate all armstrong number within a desired range if he wants to..
! Note: A number is armstrong if the cube of the sum of every digit of a number is equal to that number.
? Example of Armstrong Number is : 153 [1^3+5^3+3^3=1+125+27=153]
"""
print('1.Check if a number is armstrong or not')
print('2.Generate armstrong numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    number = int(input('Enter any number:'))
    temp = number
    sumx = 0
    while(number > 0):
        digit = number % 10
        sumx += digit**3
        number //= 10
    if(sumx == temp):
        print("It's an Armstrong Number!")
    else:
        print("It's not an Armstrong Number")
elif choice == 2:
    print('All Armstrong numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Armstrong numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        temp = minx
        sumx = 0
        while(temp > 0):
            digit = temp % 10
            sumx += digit**3
            temp //= 10
        if(sumx == minx):
            print(sumx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
