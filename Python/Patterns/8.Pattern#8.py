"""
In this program, our objective is to generate the following pattern using loops in Python...

                                           *********    
                                            *******
                                             *****
                                              ***
                                               *
"""

lines = int(input('How many lines:'))
space = ' '
i = 0
rep = lines+4
while(lines > 0):
    print(space*i, end='')
    if rep == 0:
        print('*')
    print('*'*rep, end='')
    print('\n')
    rep -= 2
    i += 1
    lines -= 1
