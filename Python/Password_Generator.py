"""
todo: In this program, our objective is to develop a python code that is able to generate passwords for users.
"""
import random
print('~~~~~~~~~PASSWORD GENERATOR~~~~~~~~~~~')
print('What kind of password you would like to generate?')
print('1.Numeric')
print('2.Alphabetic')
print('3.Alphanumeric')
ch = int(input('Enter choice(1-3):'))
gn = 'Generate another one? Press y to continue else any other key to exit---\n'
if ch == 1:
    print('We will generate a 10 digit strong numerical password for you.')
    while True:
        print('\n')
        n = 10
        lst = []
        while(n != 0):
            lst.append(random.randint(0, 9))
            n -= 1
        password = ''
        for i in range(0, 10):
            lst[i] = str(lst[i])
            password += lst[i]
        print(password)
        c = input(gn)
        if c == 'Y' or c == 'y':
            continue
        else:
            break
elif ch == 2:
    print('We will generate a 10 digit strong alphabetic password for you.')
    while True:
        print('\n')
        n = 10
        lst = []
        passw = ['Q', 'x', 'T', 'R', 'f', 'J',
                 'k', 'O', 'W', 'd', 'z', 'p', 'M']
        while(n != 0):
            lst.append(random.choice(passw))
            n -= 1
        password = ''
        for i in range(0, 10):
            lst[i] = str(lst[i])
            password += lst[i]
        print(password)
        c = input(gn)
        if c == 'Y' or c == 'y':
            continue
        else:
            break
elif ch == 3:
    print('We will generate a 10 digit strong alphanumerical password for you.')
    while True:
        print('\n')
        n = 10
        lst = []
        passw = ['Q', 'x', 'T', 'R', 'f', 'J',
                 'k', 'O', 'W', 'd', 'z', 'p', 'M']
        while(n != 0):
            lst.append(random.choice(passw))
            lst.append(random.randint(0, 9))
            n -= 1
        password = ''
        for i in range(0, 10):
            lst[i] = str(lst[i])
            password += lst[i]
        print(password)
        c = input(gn)
        if c == 'Y' or c == 'y':
            continue
        else:
            break
else:
    print('Wrong Choice')
print('\nHit Enter to End.......')
input()
