def is_curzon(num):
    n1 = (2**num)+1
    n2 = (2*num)+1
    if n1 % n2 == 0:
        return True
    else:
        return False


print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))
