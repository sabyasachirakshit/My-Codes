# Find wether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

# Program-

number = int(input("Enter number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
