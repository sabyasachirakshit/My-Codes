"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is Fascinating or not.
todo: User can also generate Fascinating numbers within a desired range if he wants to..
! Note: A number is Fascinating if is multilpied by 2 and 3, and both these products are concatenated with the original number, then the 
! new number contains all the digits from 0-9 exactly once. There could be any number of zeroes and are ignored. 
? Example Fascinating Number is : 192 [192*2=384,192*3=576,conc=192384576 which contains number from 0-9 exactly once.]
"""
print('1.Check if a number Fascinating or not')
print('2.Generate Fascinating numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    num = int(input('Enter a 3 digit number:'))
    temp = num
    c = 0
    while(temp > 0):
        c += 1
        temp //= 10
    if c == 3:
        num2 = num*2
        num3 = num*3
        temp, temp2, temp3 = num, num2, num3
        num_lst = []
        while(temp > 0):
            dig = temp % 10
            num_lst.append(dig)
            temp //= 10
        while(temp2 > 0):
            dig = temp2 % 10
            num_lst.append(dig)
            temp2 //= 10
        while(temp3 > 0):
            dig = temp3 % 10
            num_lst.append(dig)
            temp3 //= 10
        i = 0
        flag = 0
        j = 1
        n = len(num_lst)
        for i in range(0, n):
            for j in range(1, n-1):
                if i == j:
                    continue
                else:
                    if num_lst[i] == num_lst[j]:
                        flag = 1
                        break
                    else:
                        continue
            if flag == 1:
                break
            else:
                continue
        if flag == 1:
            print('Not a Fascinating Number')
        else:
            print('Fascinating Number')
    else:
        print('Please enter 3 digit number!')
        quit()
elif choice == 2:
    print('All Fascinating numbers shall be generated within a given input range..')
    print('Range shall be within 100-999!')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    if minx >= 100 and maxx <= 999:
        print(f'All Fascinating numbers between {minx} and {maxx} are:')
        while(minx <= maxx):
            num2 = minx*2
            num3 = minx*3
            flag = 0
            temp, temp2, temp3 = minx, num2, num3
            num_lst = []
            while(temp > 0):
                dig = temp % 10
                num_lst.append(dig)
                temp //= 10
            while(temp2 > 0):
                dig = temp2 % 10
                num_lst.append(dig)
                temp2 //= 10
            while(temp3 > 0):
                dig = temp3 % 10
                num_lst.append(dig)
                temp3 //= 10
            i = 0
            flag = 0
            j = 1
            n = len(num_lst)
            i = 0
            flag = 0
            j = 1
            n = len(num_lst)
            for i in range(0, n):
                for j in range(1, n-1):
                    if i == j:
                        continue
                    else:
                        if num_lst[i] == num_lst[j]:
                            flag = 1
                            break
                        else:
                            continue
                if flag == 1:
                    break
                else:
                    continue
            if flag == 0:
                print(minx)
            minx += 1
print('\nHit Enter to End.......')
input()
