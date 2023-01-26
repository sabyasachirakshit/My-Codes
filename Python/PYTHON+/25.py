# Check wether a specified value is contained in a group of values.

# Program-

lst = list(
    map(str, input("Enter a group of values (sepeerated by commas): ").split(',')))
val = input("Enter specified value: ")
if val in lst:
    print(True)
else:
    print(False)
