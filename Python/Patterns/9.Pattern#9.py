"""
In this program, our objective is to generate the following pattern using loops in Python...

                                           *********    
                                            *******
                                             *****
                                              ***
                                               *
                                              ***
                                             *****
                                            *******
                                           *********   
"""

lines = int(input('How many lines:'))
i = 1
up_space = 0
up_rep = lines+4
while(i <= lines-1):
    print(' '*up_space, end='')
    print('*'*up_rep, end='')
    print('\n')
    up_space += 1
    up_rep -= 2
    i += 1
i = ' '
j = '*'
inc = 1
while lines != 0:
    print(i*(lines-1), end='')
    print((j*inc), end='')
    inc += 2
    lines -= 1
    print('\n')
