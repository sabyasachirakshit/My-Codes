def number_length(num):
    if num >= 0 and num <= 9:
        return 1
    else:
        c = 0
        while(num > 0):
            c += 1
            num //= 10
        return c


print(number_length(10))

print(number_length(5000))

print(number_length(0))
