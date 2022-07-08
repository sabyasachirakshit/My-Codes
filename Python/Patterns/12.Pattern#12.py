"""
In this program, our objective is to generate the following pattern using loops in Python...

                                               *
                                              *  *
                                             *    *
                                            *      *
                                           **********
"""

lines = int(input('Enter how many lines:'))
ls = lines-1
ms = 2
start = 1
xc = 0
t = lines
while(start <= lines):
    if start == 1:
        print(' '*(lines+1), end='')
        print('*')
        print('\n')
        ls -= 1
        start += 1
        continue
    print(' '*ls, '*', ' '*ms, '*', end='')
    print('\n')
    ms += 2
    ls -= 1
    start += 1
    if start == lines:
        if(t == 5):
            xc = 1
            print('*'*((lines*3)-xc), end='')
        else:
            while(t != 5):
                xc += 1
                t -= 1
            print('*'*((lines*3)-(xc+1)), end='')
        print('\n')
        start += 1
