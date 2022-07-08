"""
todo: In this program, our objective is to develop a python code that applies selection sort on a unsorted list.
!Selection Sort sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.
"""
L = int(input('Please enter the size of list:'))
lst = []
i = 0
while L != 0:
    element = int(input(f'Enter Element {i} = '))
    lst.append(element)
    i += 1
    L -= 1
print('Your Unsorted List is:', lst)
no_of_pass = len(lst)
j = 1
min_idx = 1
iterator = 0
temp = 0
while iterator < no_of_pass-1:
    min_idx = iterator
    j = iterator+1
    while j < no_of_pass:
        if lst[j] < lst[min_idx]:
            min_idx = j
        j += 1
    temp = lst[min_idx]
    lst[min_idx] = lst[iterator]
    lst[iterator] = temp
    iterator += 1
print('Sorted List[Using Selection Sort]:', lst)
print('\nHit Enter to End.......')
input()
