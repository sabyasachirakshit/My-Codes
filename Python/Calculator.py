"""
todo: In this program, our objective is to develop python code that works as a scientific calculator!
"""
import math
print('~~~~~~~~~~~CALCULATOR~~~~~~~~~~~')
print('1. + ')
print('2. - ')
print('3. * ')
print('4. / ')
print('5. % ')
print('6. sin ')
print('7. cos ')
print('8. tan ')
print('9. cot ')
print('10. sec ')
print('11. cosec ')
print('12. Sqrt')
print('13. Power')
print('14. Log Base 10')
print('15. HCF/GCD')
print('16. LCM')
print('17.Area of Circle')
print('18.Area of Rectangle')
print('19.Area of Sqaure')
print('20.Area of Triangle')
print('21.Area of Trapezoid')
print('22.Area of Rhombus')
print('23.Area of Parallelogram')
ch = int(input('Enter your choice(1-23):'))
fn = 'Enter First Number:'
sn = 'Enter Second Number:'
rs = 'Result:'
en = 'Enter Number:'
eb = 'Enter Base:'
eh = 'Enter Height:'
aor = 'Area of Rhombus:'
if ch == 1:
    num1 = int(input(fn))
    num2 = int(input(sn))
    print(rs, num1+num2)
elif ch == 2:
    num1 = int(input(fn))
    num2 = int(input(sn))
    print(rs, num1-num2)
elif ch == 3:
    num1 = int(input(fn))
    num2 = int(input(sn))
    print(rs, num1*num2)
elif ch == 4:
    num1 = int(input(fn))
    num2 = int(input(sn))
    print(rs, num1//num2)
    print(rs, '[Decimals Included]:', num1/num2)
elif ch == 5:
    num1 = int(input(fn))
    num2 = int(input(sn))
    print(rs, num1 % num2)
elif ch == 6:
    num = int(input(en))
    print(f'sin {num}:', math.sin(num))
elif ch == 7:
    num = int(input(en))
    print(f'cos {num}:', math.cos(num))
elif ch == 8:
    num = int(input(en))
    print(f'tan {num}:', math.tan(num))
elif ch == 9:
    num = int(input(en))
    print(f'cot {num}:', 1/math.tan(num))
elif ch == 10:
    num = int(input(en))
    print(f'sec {num}:', 1/math.cos(num))
elif ch == 11:
    num = int(input(en))
    print(f'cosec {num}:', math.sin(num))
elif ch == 12:
    num = int(input(en))
    print(f'Square Root of {num}:', math.sqrt(num))
elif ch == 13:
    num = int(input(en))
    por = int(input('Enter power:'))
    print(f'{num} raised to power {por}:', math.pow(num, por))
elif ch == 14:
    num = int(input(en))
    print(f'log {num} base 10:', math.log10(num))
elif ch == 15:
    num1 = int(input(fn))
    num2 = int(input(sn))
    print('GCD/HCF:', math.gcd(num1, num2))
elif ch == 16:
    num1 = int(input(fn))
    num2 = int(input(sn))
    i = 2
    lst = []
    t1 = num1
    t2 = num2
    while True:
        if num1 % i == 0 and num2 % i == 0:
            num1 //= i
            num2 //= i
            lst.append(i)
            i = 2
        elif num1 % i == 0 and num2 % i != 0:
            num1 //= i
            lst.append(i)
            i = 2
        elif num1 % i != 0 and num2 % i == 0:
            num2 //= i
            lst.append(i)
            i = 2
        else:
            if num1 == 1 and num2 == 1:
                break
            else:
                i += 1
    lcm = 1
    print(lst)
    for i in lst:
        lcm *= i
    print(f'LCM of {t1} and {t2} is:', lcm)
elif ch == 17:
    rad = int(input('Enter Radius:'))
    print('Area of circle:', math.pi*(rad**2))
elif ch == 18:
    lent = int(input('Enter length:'))
    bret = int(input('Enter breadth:'))
    print('Area of Rectangle:', lent*bret)
elif ch == 19:
    side = int(input('Enter Side:'))
    print('Area of Square:', side**2)
elif ch == 20:
    base = int(input(eb))
    height = int(input(eh))
    print('Area of Traiangle:', 0.5*base*height)
elif ch == 21:
    base1 = int(input('Enter base1:'))
    base2 = int(input('Enter base2:'))
    height = int(input(eh))
    print('Area of Trapezoid:', (height/2)*(base1+base2))
elif ch == 22:
    print('1. Using Diagonals')
    print('2.Using Base & Height')
    print('3.Using Trigonometry')
    c = int(input('Select choice(1-3):'))
    if c == 1:
        d1 = int(input('Enter Diagonal 1:'))
        d2 = int(input('Enter Diagonal 2:'))
        print(aor, 0.5*d1*d2)
    elif c == 2:
        base = int(input(eb))
        height = int(input(eh))
        print(aor, base*height)
    elif c == 3:
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        print(aor, (b**2)*(math.sin(a)**2))
    else:
        print('Wrong Choice!')
elif ch == 23:
    base = int(input(eb))
    height = int(input(eh))
    print('Area of Parallelogram:', base*height)
else:
    print('Wrong Choice!')
print('\nHit Enter to End.......')
input()
