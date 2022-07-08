# Get the difference between a given number and 17, if the numbe is greater than 17 return double the absolute difference.

# Program-

def diff(num):
    if num > 17:
        return (num-17)*2
    else:
        return (17-num)


number = int(input("Enter Number: "))
print(diff(number))
