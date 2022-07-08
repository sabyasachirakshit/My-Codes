lst = []
size = int(input('Enter how many elements:'))
i = 1
while(size != 0):
    lst.append(int(input(f'Enter element {i}:')))
    i += 1
    size -= 1
print('Here is your list:', lst)
for key, value in enumerate(lst):
    prime_flag = 1
    if (value % 2) != 0:
        j = 2
        while(j < value):
            if value % j == 0:
                prime_flag = 0
                break
            j += 1
    if prime_flag == 0:
        start = value
        end = value+100
        while(start <= end):
            k = 2
            while(k < start):
                if start % k == 0:
                    start += 1
                    break
                k += 1
            else:
                lst[key] = start
                break
            start += 1
print('Updated List:', lst)
