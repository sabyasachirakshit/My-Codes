"""
In this program, our objective is to generate the following pattern using loops in Python...

                                               *
                                              ***
                                             *****
                                            *******
                                           *********
"""

lines = int(input('How many lines:'))
i = ' '
j = '*'
inc = 1
while lines != 0:
    print(i*(lines-1), end='')
    print((j*inc), end='')
    inc += 2
    lines -= 1
    print('\n')
