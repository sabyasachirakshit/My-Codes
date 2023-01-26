# Create a histogram from a given list of integers.

# Program-

lst = list(
    map(int, input("Enter list of integers (sepeerated by commas): ").split(',')))
for i in lst:
    print('*'*i)
