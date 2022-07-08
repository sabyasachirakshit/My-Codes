# Calculate sum of three given numbers, if the values are equal then return thrice of their sum

# Program-

def sum_of_three(a, b, c):
    if a == b == c:
        return ((a+b+c)*3)
    else:
        return (a+b+c)


n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
n3 = int(input("Enter 3rd number:"))
print(sum_of_three(n1, n2, n3))
