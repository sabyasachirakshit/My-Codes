# Check wether a file exists.

# Program-
import os
filename = input("Enter filename: ")
print(f"{filename} exists: ", os.path.isfile(filename))
