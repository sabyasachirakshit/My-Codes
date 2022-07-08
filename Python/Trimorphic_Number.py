"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is Trimorphic or not.
todo: User can also generate all Trimorphic number within a desired range if he wants to..
! Note: A number is Trimorphic if the last digit of cube of the number is equal to the number.
? Example of Trimorphic Number is : 5 [5^3=125]
"""
print('1.Check if a number is Trimorphic or not')
print('2.Generate trimorphic numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    num = int(input('Enter any number:'))
    black_flag = 0
    temp = num
    c = 0
    while(temp > 0):
        dig = temp % 10
        c += 1
        temp //= 10
    cb_num = num*num*num
    temp = cb_num
    lst = []
    while(temp > 0):
        dig = temp % 10
        lst.append(dig)
        temp //= 10
    m_list = lst[::-1]
    if c == 1:
        if(m_list[-c] == num):
            print('Trimorphic Number')
        else:
            print('Not an Trimorphic Number')
    else:
        lst = []
        temp = num
        while(temp > 0):
            dig = temp % 10
            lst.append(dig)
            temp //= 10
        mm_list = lst[::-1]
        while(c != 0):
            if(m_list[-c] != mm_list[-c]):
                black_flag = 1
                break
            else:
                c -= 1
        if(black_flag == 0):
            print('Trimorphic Number')
        else:
            print('Not an Trimorphic Number')
elif choice == 2:
    print('All Trimorphicnumbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(f'All Trimorphic numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        black_flag = 0
        temp = minx
        c = 0
        while(temp > 0):
            dig = temp % 10
            c += 1
            temp //= 10
        cb_num = minx*minx*minx
        temp = cb_num
        lst = []
        while(temp > 0):
            dig = temp % 10
            lst.append(dig)
            temp //= 10
        m_list = lst[::-1]
        if c == 1:
            if(m_list[-c] == minx):
                print(minx)
        else:
            lst = []
            temp = minx
            while(temp > 0):
                dig = temp % 10
                lst.append(dig)
                temp //= 10
            mm_list = lst[::-1]
            while(c != 0):
                if(m_list[-c] != mm_list[-c]):
                    black_flag = 1
                    break
                else:
                    c -= 1
            if(black_flag == 0):
                print(minx)
        minx += 1
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
