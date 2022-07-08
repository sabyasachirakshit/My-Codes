"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is Disarium or not.
todo: User can also generate all Disarium number within a desired range if he wants to..
! Note: A number is Disarium if the sum of its digits raised to the power of respective position is equal to that number.
? Example of Disarium Number is : 175 [1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175]
"""
import math  # * To Calculate Power
print('1.Check if a number is Disarium or not')
print('2.Generate Disarium numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    number = int(input('Enter any number:'))
    temp = number
    lst_num = []
    sumx = 0
    while(temp > 0):
        digit = temp % 10
        lst_num.append(digit)
        temp //= 10
    fin_num = lst_num[::-1]
    for i in range(len(fin_num)):
        fin_num[i] = math.pow(fin_num[i], i+1)
    for i in range(len(fin_num)):
        sumx += fin_num[i]
    if(sumx == number):
        print("It's an Disarium Number!")
    else:
        print("It's not an Disarium Number")
elif choice == 2:
    print('All Disarium numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Disarium numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        temp = minx
        lst_num = []
        sumx = 0
        while(temp > 0):
            digit = temp % 10
            lst_num.append(digit)
            temp //= 10
        fin_num = lst_num[::-1]
        for i in range(len(fin_num)):
            fin_num[i] = math.pow(fin_num[i], i+1)
        for i in range(len(fin_num)):
            sumx += fin_num[i]
        if(sumx == minx):
            print(minx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
