"""
todo:In this program, our objective is to develop a python code that applies insertion sort on a unsorted list.
? Insertion Sort is a simple sorting algorithm that builds the final sorted arrat one item at a time.
"""
L = int(input('Please enter the size of list:'))
lst = []
i = 1
while L != 0:
    element = int(input(f'Enter Element {i} = '))
    lst.append(element)
    i += 1
    L -= 1
print('Your Unsorted List is:', lst)
no_of_pass = len(lst)
i = 1
while no_of_pass != 1:
    key = lst[i]
    j = i-1
    while j >= 0 and lst[j] > key:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = key
    i += 1
    no_of_pass -= 1
print('Sorted List[Using Insertion Sort]:', lst)
print('\nHit Enter to End.......')
input()
