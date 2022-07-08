"""
todo: In this program, our objective is to make a faulty calculator that gives fake results only on the following sums->
! 45+87=?
! 52-23=?
! 98*43=?
! 56/12=?
! 785.322*433.44=?
! 987/3.67=?
? And the rest of the operations shall produce the correct answer!
"""
print('CALCULATOR-->')
res = 1
while True:
    num1 = int(input('Enter 1st operand:'))
    num2 = int(input('Enter 2nd operand:'))
    op = input('Enter operator(+,-,*,/):')
    if(num1 == 45 and num2 == 87 and op == '+'):
        print('Result=142')
    elif(num1 == 52 and num2 == 23 and op == '-'):
        print('Result=28')
    elif(num1 == 98 and num2 == 43 and op == '*'):
        print('Result=4114')
    elif(num1 == 56 and num2 == 12 and op == '/'):
        print('Result=3.1116666666666666')
    elif(num1 == 785.322 and num2 == 433.44 and op == '*'):
        print('Result=340587.296768')
    elif(num1 == 987 and num2 == 3.67 and op == '/'):
        print('Result=266.324545653456677')
    else:
        if op == '+':
            res = num1+num2
        elif op == '-':
            res = num1-num2
        elif op == '*':
            res = num1*num2
        elif op == '/':
            res = num1/num2
        elif op == '%':
            res = num1 % num2
        print('Result=', res)
    c = input('Press E to exit or any other key to continue--->')
    if(c == 'e' or c == 'E'):
        print('Thanks for using Faulty Calculator! :)')
        break
print('\nHit Enter to End.......')
input()
