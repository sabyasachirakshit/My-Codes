"""
In this program, our objective is to generate the following pattern using loops in Python...

                                               *****
                                               ****
                                               ***
                                               **
                                               *
"""

lines = int(input('How many lines:'))
while(lines > 0):
    print('*'*lines, end='')
    print('\n')
    lines -= 1
