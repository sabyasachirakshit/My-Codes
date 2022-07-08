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
up_sp = mid-1
up_rep = 1
while(start <= mid):
    print(' '*up_sp, end='')
    print('*'*up_rep, end='')
    print('\n')
    up_rep += 1
    up_sp -= 1
    start += 1
start = mid
dn_sp = 1
dn_rep = mid-1
while(start <= lines):
    print(' '*dn_sp, end='')
    print('*'*dn_rep, end='')
    print('\n')
    dn_sp += 1
    dn_rep -= 1
    start += 1
