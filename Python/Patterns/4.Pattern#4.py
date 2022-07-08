"""
In this program, our objective is to generate the following pattern using loops in Python...

                                               1
                                               22                                         
                                               333
                                               4444
                                               55555 
"""

lines = int(input('How many lines:'))
num = '1'
rep = 1
while lines != 0:
    print(str(num)*rep, end='')
    num = int(num)+1
    rep += 1
    lines -= 1
    print('\n')
