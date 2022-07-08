def sevenBoom(lst):
    for i in lst:
        if i >= 0 and i <= 9:
            if i == 7:
                return "Boom!"
        else:
            temp = i
            while(temp > 0):
                dig = temp % 10
                if dig == 7:
                    return "Boom!"
                temp //= 10

    else:
        return "There is no 7 in the array"


print(sevenBoom([1, 2, 3, 4, 5, 6, 7]))
print(sevenBoom([8, 6, 33, 100]))
print(sevenBoom([2, 55, 60, 97, 861]))
