"""
In this program, our objective is to generate the following pattern using loops in Python...

                                               *****
                                                ****
                                                 ***
                                                  **
                                                   *
"""

lines = int(input('How many lines:'))
space = ' '
i = 0
while(lines > 0):
    print(space*i, end='')
    print('*'*lines, end='')
    print('\n')
    lines -= 1
    i += 1
