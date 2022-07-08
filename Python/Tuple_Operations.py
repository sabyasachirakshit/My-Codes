"""
? This program conatins all operations that can be done in a tuple!
"""
#! Defining a tuple
tup = (1, 2, 3, 4, 5)
print(tup)
#! Traverse Tuple using loops
print('Elements inside tuple:')
for item in tup:
    print(item)
#! Accessing tuple elements using index
print(tup[3])  # ? Accessing the element at index 3
#! Accessing tuple elements using index range
print(tup[2:5])
#! Accessing tuple elements using  negativeindex range
print(tup[-5:-1])
#! Finding Length of tuple
print('Length of tuple:', len(tup))
#! Searching element inside tuple
search = 3
if search in tup:
    print('Present!')
else:
    print('Not Present!')
#! Concatenate two tuples
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1+tup2  # ? Concatenating two tuples
print(tup3)
#! Delete Tuple
tuple = (1, 2, 3, 4, 5)
print(tuple)
del tuple  # ? Deleting tuple
print('Previous Tuple Deleted!')
print('\nHit Enter to End.......')
input()
