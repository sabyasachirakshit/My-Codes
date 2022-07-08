def sorting(lst):
    no_of_pass = len(lst)
    temp = 1
    while(no_of_pass != 0):
        for i in range(0, len(lst)):
            for j in range(1, len(lst)):
                if lst[i-1] <= lst[j-1]:
                    temp = lst[i-1]
                    lst[i-1] = lst[j-1]
                    lst[j-1] = temp
        no_of_pass -= 1
    return lst


def sum_missing_numbers(lst):
    fin_lst = sorting(lst)
    min_num = fin_lst[0]
    max_num = fin_lst[len(fin_lst)-1]
    all_num = []
    temp = min_num
    while(temp < max_num):
        all_num.append(temp)
        temp += 1
    sumx = 0
    for i, j in enumerate(all_num):
        if j not in fin_lst:
            sumx += j
    return sumx


print(sum_missing_numbers([4, 3, 8, 1, 2]))
print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))
print(sum_missing_numbers([1, 2, 3, 4, 5]))
