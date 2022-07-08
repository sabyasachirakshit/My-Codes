"""
todo: In this program, our objective is to develop a python code that enables users to find out if a number is magic or not!
! Note:A magic number is a number whose super digit is 1. A super digit is the summation of all digits until it becomes one.
? Example: Finding super digit of 226: 2+2+6=10 , 1+0=1 SUPER DIGIT=1 Therefore, 226 is a magic number!                     
"""


def sum_of_digits(number):
    temp = number
    s = 0
    while temp > 0:
        dig = temp % 10
        s += dig
        temp //= 10
    return s


print('1.Check if a number is magic or not')
print('2.Generate magic numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    num = int(input('Enter any number:'))
    sumx = sum_of_digits(num)
    c = 0
    while True:
        temp = sumx
        temp2 = temp
        while temp > 0:
            c += 1
            temp //= 10
        if c == 1:
            break
        else:
            sumx = sum_of_digits(temp2)
            c = 0
    if sumx == 1:
        print('Magic Number')
    else:
        print('Not a Magic Number')
elif choice == 2:
    print('All magic numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All magic numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        sumx = sum_of_digits(minx)
        c = 0
        while True:
            temp = sumx
            temp2 = temp
            while temp > 0:
                c += 1
                temp //= 10
            if c == 1:
                break
            else:
                sumx = sum_of_digits(temp2)
                c = 0
        if sumx == 1:
            print(minx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
