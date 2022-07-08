"""
todo: In this program, our objective is to develop a python code that enables users to find out the super digit of a number.
! Note: A super digit is the summation of all digits until it becomes one.
? Example: Finding super digit of 1355: 1+3+5+5=14 , 1+4=5 , SUPER DIGIT=5                                                                      
"""
num = int(input('Enter a number whose super digit is required:'))


def sum_of_digits(number):
    temp = number
    s = 0
    while temp > 0:
        dig = temp % 10
        s += dig
        temp //= 10
    return s


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
print(f'The super digit of {num} is {sumx}')
print('\nHit Enter to End.......')
input()
