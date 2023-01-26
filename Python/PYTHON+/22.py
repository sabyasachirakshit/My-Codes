# Count the number 4 in a given list.

# Program-

lst = list(map(int, input("Enter numbers in list: ").split(',')))
c = 0
for i in lst:
    if i == 4:
        c += 1
print(f"The number 4 appears {c} time(s) in the given list {lst}")
