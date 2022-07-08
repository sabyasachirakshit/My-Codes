# Return true if the two given integer values are equal or their sum or difference is 5

# Program-

def c(a, b):
    if a == b or a+b == 5 or a-b == 5:
        return True


print(c(12, 12))
print(c(10, 5))
print(c(1, 4))
print(c(12, 13))
