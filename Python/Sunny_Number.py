"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is sunny or not.
todo: User can also generate all sunny number within a desired range if he wants to..
! Note: A number is sunny if the square root of N+1 is an integer.
? Example of sunny Number is : 24 [24+1=root(25)=5 which is an integer]
"""
import math  # ! To find square root
print('1.Check if a number is sunny or not')
print('2.Generate sunny numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    number = int(input('Enter any number(<1000000):'))
    if(number > 1000000):
        print('Error!')
        quit()
    else:
        next_number = number+1
        sq_root = math.sqrt(next_number)
        for i in range(1, 1000000):
            if float(i) == sq_root:
                print('Sunny Number')
                break
        else:
            print('Not Sunny')
elif choice == 2:
    print('All sunny numbers shall be generated within a given input range..')
    print('Range shall be under 1-1000000')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    if minx >= 1 and maxx <= 1000000:
        print(f'All sunny numbers between {minx} and {maxx} are:')
        while(minx <= maxx):
            next_number = minx+1
            sq_root = math.sqrt(next_number)
            x = int(sq_root)
            for i in range(1, 100000):
                if float(i) == sq_root:
                    print(minx)
                    break
            minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
