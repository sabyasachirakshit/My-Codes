"""
todo: In this program, our objective is to implement Binary search on a list.
!Binary search is searching a sorted array by repeatedly dividing the search interval in half.
"""


def bin_search(lst, search):
    length = len(lst)
    if length == 1:
        if lst[0] == search:
            print('Element Present!!')
            quit()
        else:
            print('Element Not Present!!')
            quit()
    if length % 2 != 0:
        mid = (length+1)//2
    else:
        mid = length//2
    if lst[mid-1] == search:
        print('Element Present!!')
        quit()
    elif lst[mid-1] < search:
        lst1 = []
        for i in range(mid, len(lst)):
            lst1.append(lst[i])
        bin_search(lst1, search)
    elif lst[mid-1] > search:
        lst1 = []
        for i in range(0, mid):
            lst1.append(lst[i])
        bin_search(lst1, search)


def sort_array(lst, s):
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
    bin_search(lst, s)


print('BINARY SEARCH..')
size = int(input('how many elements:'))
lst = []
while(size > 0):
    lst.append(int(input('Enter element:')))
    size -= 1
s = int(input('Enter Searching Element:'))
sort_array(lst, s)
print('\nHit Enter to End.......')
input()
