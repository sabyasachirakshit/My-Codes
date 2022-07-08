"""
In this program, our objective is to generate the following pattern using loops in Python...

                                               *
                                               **
                                               ***
                                               ****
                                               ***
                                               **
                                               *
"""

lines = int(input('How many lines:'))
mid = (lines+1)//2
start = 1
while(start <= mid):
    print('*'*start, end='')
    print('\n')
    start += 1
start = mid
rep = start-1
while(start <= lines):
    print('*'*rep, end='')
    print('\n')
    rep -= 1
    start += 1
