def list_of_multiples(n1, n2):
    lst = []
    i = 1
    while(i <= n2):
        lst.append(n1*i)
        i += 1
    return lst


print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))
