# Get a new string from a given string where Is has been added to the front. If the given string already begins with Is then return the string unchanged.

# Program-

str = input("Enter String:")
lst = []
for i in str:
    lst.append(i)
if lst[0] == 'I' and lst[1] == 's':
    print(str)
else:
    print("Is"+str)
