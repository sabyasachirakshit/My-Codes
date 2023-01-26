def fac1(n):

    fac=1
    for i in range(n):
       fac=fac*(i+1)
    return fac
def fact2(n):
    if n==1:
        return 1
    else:
        return n*fact2(n-1)
num1=int(input("Enter A no"))
print(fac1(num1))
print(fact2(num1))
