def prime_factorization(number):
    i = 2
    lst = []
    lst2 = []
    while(i < number):
        if number % i == 0:
            lst.append(i)
        i += 1
    for i in lst:
        temp = 2
        flag = 0
        while temp < i:
            if i % temp == 0:
                flag = 1
                break
            else:
                temp += 1
        if(flag == 0):
            lst2.append(i)
    print(lst2)


prime_factorization(1048)
prime_factorization(782016)
prime_factorization(12)
