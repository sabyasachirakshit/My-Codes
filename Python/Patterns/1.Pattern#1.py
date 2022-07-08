"""
In this program, our objective is to generate the following pattern using loops in Python...

                                               *
                                               **
                                               ***
                                               ****
                                               *****
"""

lines = int(input('How many lines:'))
i = 0
while(lines != 0):
    print('*'*(i+1), end='')
    print('\n')
    i += 1
    lines -= 1
