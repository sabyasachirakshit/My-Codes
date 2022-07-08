"""
todo:In this program, our objective is to develop a python code that applies Heap sort on a unsorted list.
? Heap Sort is similar to selection sort wehre we first find the maximum element and place the maximum element at the end.
! We repeat process for the remaining elements.
"""


def heapify(lst, size, i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < size and lst[left] > lst[largest]:
        largest = left
    if right < size and lst[right] > lst[largest]:
        largest = right
    temp = 0
    if largest != i:
        temp = lst[i]
        lst[i] = lst[largest]
        lst[largest] = temp
        heapify(lst, size, largest)


def heap_sort(lst, size):
    i = (size//2)-1
    while i >= 0:
        heapify(lst, size, i)
        i -= 1
    i = size-1
    temp = 0
    while i >= 0:
        temp = lst[0]
        lst[0] = lst[i]
        lst[i] = temp
        heapify(lst, i, 0)
        i -= 1


lst = []
size = int(input('How many elements:'))
i = 1
while(size != 0):
    element = int(input(f'Enter Element {i}:'))
    lst.append(element)
    i += 1
    size -= 1
print('Your Unsorted List:', lst)
heap_sort(lst, len(lst))
print('Your Sorted List[Using Heap Sort]:', lst)
print('\nHit Enter to End.......')
input()
