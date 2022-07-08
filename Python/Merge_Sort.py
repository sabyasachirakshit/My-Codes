"""
todo: In this program, our objective is to develop a python code that applies Merge sort on a unsorted list.
! Merge Sort is a Divide and Conquer Algorithm. It picks an element as pivot and partiitions the given list around the picked pivot.
"""
L = int(input('Please enter the size of list:'))
lst = []
i = 0


def merge(lst, l, m, r):
    n1 = m-l+1
    n2 = r-m
    L = []
    R = []
    x = 1
    y = 1
    while x <= n1:
        L.append(0)
        x += 1
    while y <= n2:
        R.append(0)
        y += 1
    i = 0
    while i < n1:
        L[i] = lst[l+i]
        i += 1
    j = 0
    while j < n2:
        R[j] = lst[m+1+j]
        j += 1
    i = 0
    j = 0
    k = l
    while (i < n1 and j < n2):
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1


def merge_sort(lst, l, r):
    if l >= r:
        return
    m = (l+r-1)//2
    merge_sort(lst, l, m)
    merge_sort(lst, m+1, r)
    merge(lst, l, m, r)


while L != 0:
    element = int(input(f'Enter Element {i} = '))
    lst.append(element)
    i += 1
    L -= 1
print('Your Unsorted List is:', lst)
no_of_pass = len(lst)
merge_sort(lst, 0, no_of_pass-1)
print('Your Sorted List[Using Merge Sort]:', lst)
print('\nHit Enter to End.......')
input()
