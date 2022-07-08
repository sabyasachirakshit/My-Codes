"""
todo: In this program, our objective is to develop a python code that enables users to convert Celsuis Temperature to Farenheit Temperature and vice versa.
! Note: C=5/9 X (F-32)
"""
print('1.Convert Celsius To Farenheit')
print('2.Convert Farenheit To Celsius')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    C = int(input('Enter Temperature(Celsius):'))
    F = ((9*C)+160)/5
    print(f'Equivalent Temperature of {C} C is {F} F')
elif choice == 2:
    F = int(input('Enter Temperature(Farenheit):'))
    C = (5*(F-32))/9
    print(f'Equivalent Temperature of {F} F is {C} C')
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
