"""
todo: In this program, our objective is to develop a python code that applies Quick sort on a unsorted list.
? Quick Sort is a Divide and Conquer Algorithm. It picks an element as pivot and partiitions the given list around the picked pivot.
"""
L = int(input('Please enter the size of list:'))
lst = []
i = 0


def partition(lst, low, high):
    pivot = lst[high]
    i = low-1
    j = low
    while(j <= high-1):
        if lst[j] < pivot:
            i += 1
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
        j += 1
    temp = lst[i+1]
    lst[i+1] = lst[high]
    lst[high] = temp
    return i+1


def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi-1)
        quick_sort(lst, pi+1, high)


while L != 0:
    element = int(input(f'Enter Element {i} = '))
    lst.append(element)
    i += 1
    L -= 1
print('Your Unsorted List is:', lst)
no_of_pass = len(lst)
quick_sort(lst, 0, no_of_pass-1)
print('Your Sorted List[Using Quick Sort]:', lst)
print('\nHit Enter to End.......')
input()
