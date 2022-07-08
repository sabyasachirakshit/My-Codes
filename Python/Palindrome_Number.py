""" 
todo: In this program, our objective is to develop a python code that enables users to check if a number is palindrome or not.
todo: User can also generate all palindrome number within a desired range if he wants to..
! Note: A number is palindrome if the reverse of a number is equal to that number.
? Example of palindrome Number is : 111
"""
print('1.Check if a number is palindrome or not')
print('2.Generate palindrome numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    num = int(input('Enter a number:'))
    numx = str(num)
    numy = numx[::-1]
    if(numx == numy):
        print('Palindrome')
    else:
        print('Not Palindrome')
elif choice == 2:
    print('All Palindrome number shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Palindrome numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        numx = str(minx)
        numy = numx[::-1]
        if(numx == numy):
            print(minx)
        minx += 1
else:
    print('Wrong Choice')
print('\nHit Enter to End.......')
input()
