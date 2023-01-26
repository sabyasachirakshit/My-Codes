# Find sum of two given integers. However, if the sum is between 15 and 20 it will return 20.

# Program-

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
if (a+b) >= 15 and (a+b) <= 20:
    print("20")
else:
    print(a+b)
