"""
todo: In this program, our objective is to develop a python code that applies buuble sort on a unsorted list.
? Bubble sort is a basic algorithm for arranging a string of numbers or other elements in the correct order. 
? The method works by examining each set of adjacent elements in the string, from left to right, switching their positions if they are out of 
? order.The algorithm then repeats this process until it can run through the entire string and find no two elements that need to be swapped.
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
temp = 1
while(no_of_pass != 0):
    for i in range(0, len(lst)):
        for j in range(1, len(lst)):
            if lst[i-1] <= lst[j-1]:
                temp = lst[i-1]
                lst[i-1] = lst[j-1]
                lst[j-1] = temp
    no_of_pass -= 1
print('Sorted List[Using Bubble Sort]:', lst)
print('\nHit Enter to End.......')
input()
