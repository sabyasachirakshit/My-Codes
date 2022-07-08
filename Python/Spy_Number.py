"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is spy or not.
todo: User can also generate all spy number within a desired range if he wants to..
! Note: A number is spy if the sum of every digit is equal to the product of each digit.
? Example of Spy Number is : 132 [1 + 3 + 2 = 6 ; 1 * 3 * 2 = 6]
"""
print('1.Check if a number is spy or not')
print('2.Generate spy numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    num = int(input('Enter spy number:'))
    prd = 1
    sumx = 0
    temp = num
    temp2 = num
    while(temp > 0):
        dig = temp % 10
        sumx += dig
        temp //= 10
    while(temp2 > 0):
        dig = temp2 % 10
        prd *= dig
        temp2 //= 10
    if(sumx == prd):
        print('Spy Number')
    else:
        print('Not a Spy Number')
elif choice == 2:
    print('All Spy numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Spy numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        prd = 1
        sumx = 0
        temp = minx
        temp2 = minx
        while(temp > 0):
            dig = temp % 10
            sumx += dig
            temp //= 10
        while(temp2 > 0):
            dig = temp2 % 10
            prd *= dig
            temp2 //= 10
        if(sumx == prd):
            print(minx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
