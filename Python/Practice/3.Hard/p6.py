def fact(num):
    f = 1
    while(num > 0):
        f *= num
        num -= 1
    return f


def factFact(num):
    factorial = 1
    while(num > 0):
        factorial *= fact(num)
        num -= 1
    return factorial


print(factFact(4))
print(factFact(5))
print(factFact(6))
