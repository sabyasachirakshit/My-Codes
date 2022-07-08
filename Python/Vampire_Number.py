"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is Vampire or not.
todo: User can also generate all Vampire number within a desired range if he wants to..
! Note: A number is Vampire if the product of both fangs is equal to that number! The number should have even number of digits so that it can have a pair of digits!
? Example of Vampire Number is : 1260 [21*60=1260] 
"""
import itertools  # ? To Generate Permutations
print('1.Check if a number is Vampire or not')
print('2.Generate Vampire numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    num = int(input('Enter any number:'))
    temp = num
    c = 0
    while(temp > 0):
        c += 1
        temp //= 10
    if c % 2 == 0:
        num_lst = []
        temp = num
        while temp > 0:
            digit = temp % 10
            num_lst.append(digit)
            temp //= 10
        num_lst = num_lst[::-1]
        lst1 = []
        lst2 = []
        mid = len(num_lst)//2
        for i in range(0, mid):
            lst1.append(str(num_lst[i]))
        for i in range(mid, len(num_lst)):
            lst2.append(str(num_lst[i]))
        for i, j in enumerate(lst1):
            lst1[i] = int(lst1[i])
        for i, j in enumerate(lst2):
            lst2[i] = int(lst2[i])
        s1 = list(itertools.permutations(lst1))
        x1 = []
        for i in s1:
            x1.append(list(i))
        new1 = []
        for i in x1:
            for j in i:
                new1.append(j)
        for i, j in enumerate(new1):
            new1[i] = str(new1[i])
        concat = ''
        i = 1
        perm1 = []
        c1 = 0
        while i <= len(new1):
            if i % len(lst1) != 0:
                concat += new1[i-1]
            else:
                concat += new1[i-1]
                perm1.append(concat)
                concat = ''
            i += 1
        for i, j in enumerate(perm1):
            perm1[i] = int(perm1[i])
        s2 = list(itertools.permutations(lst2))
        x1 = []
        for i in s2:
            x1.append(list(i))
        new1 = []
        for i in x1:
            for j in i:
                new1.append(j)
        for i, j in enumerate(new1):
            new1[i] = str(new1[i])
        concat = ''
        i = 1
        perm2 = []
        c1 = 0
        while i <= len(new1):
            if i % len(lst2) != 0:
                concat += new1[i-1]
            else:
                concat += new1[i-1]
                perm2.append(concat)
                concat = ''
            i += 1
        for i, j in enumerate(perm2):
            perm2[i] = int(perm2[i])
        mult = []
        for i in perm1:
            for j in perm2:
                mult.append(i*j)
        for i in mult:
            if i == num:
                print('VAMPIRE NUMBER!!')
                break
        else:
            print('Not a Vampire Number!')
elif choice == 2:
    print('All Vampire numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print('Vampire Number must contain even number of digits!!!')
    print(f'All Vampire numbers between {minx} and {maxx} are:')
    while(minx <= maxx):
        temp = minx
        c = 0
        while(temp > 0):
            c += 1
            temp //= 10
        if c % 2 == 0:
            num_lst = []
            temp = minx
            while temp > 0:
                digit = temp % 10
                num_lst.append(digit)
                temp //= 10
            num_lst = num_lst[::-1]
            lst1 = []
            lst2 = []
            mid = len(num_lst)//2
            for i in range(0, mid):
                lst1.append(str(num_lst[i]))
            for i in range(mid, len(num_lst)):
                lst2.append(str(num_lst[i]))
            for i, j in enumerate(lst1):
                lst1[i] = int(lst1[i])
            for i, j in enumerate(lst2):
                lst2[i] = int(lst2[i])
            s1 = list(itertools.permutations(lst1))
            x1 = []
            for i in s1:
                x1.append(list(i))
            new1 = []
            for i in x1:
                for j in i:
                    new1.append(j)
            for i, j in enumerate(new1):
                new1[i] = str(new1[i])
            concat = ''
            i = 1
            perm1 = []
            c1 = 0
            while i <= len(new1):
                if i % len(lst1) != 0:
                    concat += new1[i-1]
                else:
                    concat += new1[i-1]
                    perm1.append(concat)
                    concat = ''
                i += 1
            for i, j in enumerate(perm1):
                perm1[i] = int(perm1[i])
            s2 = list(itertools.permutations(lst2))
            x1 = []
            for i in s2:
                x1.append(list(i))
            new1 = []
            for i in x1:
                for j in i:
                    new1.append(j)
            for i, j in enumerate(new1):
                new1[i] = str(new1[i])
            concat = ''
            i = 1
            perm2 = []
            c1 = 0
            while i <= len(new1):
                if i % len(lst2) != 0:
                    concat += new1[i-1]
                else:
                    concat += new1[i-1]
                    perm2.append(concat)
                    concat = ''
                i += 1
            for i, j in enumerate(perm2):
                perm2[i] = int(perm2[i])
            mult = []
            for i in perm1:
                for j in perm2:
                    mult.append(i*j)
            for i in mult:
                if i == minx:
                    print(minx)
                    break
        minx += 1
print('\nHit Enter to End.......')
input()
