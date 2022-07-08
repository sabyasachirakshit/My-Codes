"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is Neon or not.
todo: User can also generate all Neon number within a desired range if he wants to..
! Note: A number is Neon if the sum of the digits of its sqaure is equal to that number.
? Example of Neon Number is : 9 [9^2=81=8+1=9]
"""
print('1.Check if a number is Neon or not')
print('2.Generate Neon numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    number = int(input('Enter any number:'))
    sq = number**2
    temp = sq
    s = 0
    while temp > 0:
        dig = temp % 10
        s += dig
        temp //= 10
    if s == number:
        print('Neon Number')
    else:
        print('Not a Neon Number')
elif choice == 2:
    print('All Neon numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Neon numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        sq = minx**2
        temp = sq
        s = 0
        while temp > 0:
            dig = temp % 10
            s += dig
            temp //= 10
        if s == minx:
            print(minx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
