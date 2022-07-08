"""
todo:In this program, our objective is to develop a python code that enables users to check if a number is kaprekar or not.
todo: User can also generate all kaprekar number within a desired range if he wants to..
! Note: A number is kaprekar if the sum of the two divided parts of the square. is equal to the number.
? Example of kaprekar Number is : 45 [45^2=2025 and 20+25=45]
"""
print('1.Check if a number is kaprekar or not')
print('2.Generate kaprekar numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    number = int(input('Enter any number:'))
    sq = number**2
    temp = sq
    c = 0
    while temp > 0:
        c += 1
        temp //= 10
    if c % 2 == 0:
        temp = sq
        lst = []
        while temp > 0:
            dig = temp % 10
            lst.append(dig)
            temp //= 10
        mid1 = []
        mid2 = []
        for i in range(0, len(lst)//2):
            mid1.append(lst[i])
        for i in range(len(lst)//2, len(lst)):
            mid2.append(lst[i])
        mid1 = mid1[::-1]
        mid2 = mid2[::-1]
        concat1 = ''
        concat2 = ''
        for i in range(len(mid1)):
            mid1[i] = str(mid1[i])
            concat1 += mid1[i]
        for i in range(len(mid2)):
            mid2[i] = str(mid2[i])
            concat2 += mid2[i]
        if int(concat1)+int(concat2) == number:
            print('Kaprekar Number!')
        else:
            print('Non Kaprekar Number!')
elif choice == 2:
    print('All kaprekar numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All kaprekar numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        sq = minx**2
        temp = sq
        c = 0
        while temp > 0:
            c += 1
            temp //= 10
        if c % 2 == 0:
            temp = sq
            lst = []
            while temp > 0:
                dig = temp % 10
                lst.append(dig)
                temp //= 10
            mid1 = []
            mid2 = []
            for i in range(0, len(lst)//2):
                mid1.append(lst[i])
            for i in range(len(lst)//2, len(lst)):
                mid2.append(lst[i])
            mid1 = mid1[::-1]
            mid2 = mid2[::-1]
            concat1 = ''
            concat2 = ''
            for i in range(len(mid1)):
                mid1[i] = str(mid1[i])
                concat1 += mid1[i]
            for i in range(len(mid2)):
                mid2[i] = str(mid2[i])
                concat2 += mid2[i]
            if int(concat1)+int(concat2) == minx:
                print(minx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
