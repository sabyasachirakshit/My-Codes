"""
? In this program, we will implement Exception Handling in Python which includes--
Try except
Handling multiple exceptions
Else clause
Finally
Raise an Exception
"""


try:
    print('boo')
except TypeError:
    print('Exception Occured!')
ch = int(input(
    '1 for NameError, 2 for Type Error, 3 for ZeroDivisonError  input choice(1-3):'))
try:
    if ch == 1:
        print('r')
    elif ch == 2:
        r = "???"+10
    else:
        x = 10/0
except NameError:
    print('Name Error Occured!')
except TypeError:
    print('Type Errror Occured!')
except ZeroDivisionError:
    print('Zero Division Error Occured!')
print('1.To generate Error Exception\n2.To process successfully!')
c = int(input('Enter choice(1-2):'))
try:
    if c == 1:
        x = 10/0
except ZeroDivisionError:
    print('Zero Division Exception Occured')
else:
    print('Compiled Successfully!')
print('1.To generate Error Exception\n2.To process successfully!')
c = int(input('Enter choice(1-2):'))
try:
    if c == 1:
        x = 10/0
except ZeroDivisionError:
    print('Zero Division Exception Occured')
finally:
    print('Finally Excecutes!')
num = -1
if num < 0:
    raise Exception('Wrong configuration')
print('\nHit Enter to End.......')
input()
