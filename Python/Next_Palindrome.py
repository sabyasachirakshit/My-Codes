list1 = [1, 25, 6, 89, 458, 9, 45]
list2 = []
for item in list1:
    if item >= 10:
        for item1 in range(item, item*10):
            n1 = item1
            rev = 0
            while(n1 > 0):
                a = n1 % 10
                rev = rev*10+a
                n1 = n1//10
            if item1 == rev:
                list2.append(f"The next palindrom of {item} is {item1}")
                break
    else:
        list2.append(f"{item} is less than 10")
for i in list2:
    print(i)
print('\nHit Enter to End.......')
input()
