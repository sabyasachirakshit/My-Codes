
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

number=int(input("Enter number:"))
print(fact(number))
