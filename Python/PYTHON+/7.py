# Accept a filename and print the extension of that.

# Program-

filename = input("Enter Filename:")
lst = filename.split(".")
lst = lst[::-1]
print(f"Extension of the file {filename} is: .{lst[0]}")
