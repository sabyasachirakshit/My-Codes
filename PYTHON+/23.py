# Get the n(non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

# Program-

integer = int(input("Enter an integer(non-negative): "))
str = input("Enter String:")
if len(str) < 2:
    print(str*integer)
else:
    ft = str[0:2]
    print(integer*ft)
