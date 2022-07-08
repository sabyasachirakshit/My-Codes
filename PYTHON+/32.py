# Find sum of three given integers. However, if two values are equal sum will be zero.

# Program-

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
sum_of_three = 0
if a == b or b == c or a == c:
    print(sum_of_three)
else:
    print(a+b+c)
