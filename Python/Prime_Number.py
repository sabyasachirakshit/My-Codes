"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is Prime or not.
todo: User can also generate all Prime number within a desired range if he wants to..
! Note: A number is Prime if no number can divide that number except the number itself and 1.
? Example of Prime Number is : 19
"""
print('1.Check if a number is Prime or not')
print('2.Generate Prime numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    number = int(input('Enter any number:'))
    temp = 2
    flag = 0
    while temp < number:
        if number % temp == 0:
            flag = 1
            break
        else:
            temp += 1
    if(flag == 0):
        print("It's an Prime Number!")
    else:
        print("It's not a Prime Number")
elif choice == 2:
    print('All Prime numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Prime numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        if minx == 1:
            minx += 1
            continue
        temp = 2
        flag = 0
        while(temp < minx):
            if minx % temp == 0:
                flag = 1
                break
            else:
                temp += 1
        if(flag == 0):
            print(minx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
