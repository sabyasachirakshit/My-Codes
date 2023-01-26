# Accept a sequence of comma seperated numbers from user and generate a list and a tuple with those numbers.

# Program-

lst = list(map(int, input("Input numbers seperated by commas- ").split(",")))
print(f"List-{lst}, Tuple-{tuple(lst)}")
