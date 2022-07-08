"""
In this program, our objective is to generate the following pattern using loops in Python...

                                               1
                                               2 3                                        
                                               4 5 6
                                               7 8 9 10
                                               11 12 13 14
                                               15 16 17 18 19 
"""

lines = int(input('How many lines:'))
i = 0
n = 1
s = 1
while(lines != 0):
    if i >= 4:
        x = i
    else:
        x = i+1
    num = n
    while x != 0:
        print(f'{num} ', end='')
        x -= 1
        num += 1
        n += 1
    print('\n')
    i += 1
    s += 1
    lines -= 1
