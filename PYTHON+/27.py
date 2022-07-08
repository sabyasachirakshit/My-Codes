# Concatenate all elements in a list into a string and return it.

# Program-

lst = list(
    map(str, input("Enter elements of list (seperated by commas): ").split(',')))
str = ""
for i in lst:
    str += i
print("Concatenated elements of list into string: ", str)
