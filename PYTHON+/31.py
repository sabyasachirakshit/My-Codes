# Compute the lowest common multiply (lCM) of two positive integers.

# Program-

import math
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
print(f"LCM of {n1} and {n2} is {(n1*n2)//math.gcd(n1,n2)}")
