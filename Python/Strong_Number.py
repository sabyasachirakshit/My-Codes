"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is strong or not.
todo: User can also generate all strong numbers within a desired range if he wants to..
! Note: A number is strong if the sum of factorial of every digit of a number is equal to that number.
? Example of Strong Number is : 145 [1!+4!+5!=145]
"""
print('1.Check if a number is strong or not')
print('2.Generate strong numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    number = int(input('Enter any number:'))
    temp = number
    sumx = 0
    factz = 1
    while(number > 0):
        digit = number % 10
        while digit != 0:
            factz *= digit
            digit -= 1
        number //= 10
        sumx += factz
        factz = 1
    if(sumx == temp):
        print("It's a strong Number!")
    else:
        print("It's not a strong Number")
elif choice == 2:
    print('All strong number shall be generated within a given input range..')
    min = int(input('Enter the starting number of the range:'))
    max = int(input('Enter the ending number of the range:'))
    print(f'All strong numbers between {min} and {max} are:')
    while(min <= max):
        temp = min
        sumx = 0
        factz = 1
        while(temp > 0):
            digit = temp % 10
            while digit != 0:
                factz *= digit
                digit -= 1
            sumx += factz
            factz = 1
            temp //= 10
        if(sumx == min):
            print(sumx)
        min += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
