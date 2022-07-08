"""
? This program conatins all operations that can be done in a list and a multi dimensional list!
"""
lu = "List Updated:"
l = 'List:'
slr = 'Sorted List[Reverse=False]:'
slrt = 'Sorted List[Reverse=True]:'
#! Defining List
lst = [1, 2, 3, 4, 5]
print(lst)
#! Traverse List using loops
print('The items in the list are given below')
for i in lst:
    print(i)
#! Accessing items using index
print(lst[2])  # ? Prints the 3rd element of the list
#! Accessing items using negative index
print(lst[-2])  # ? Prints the 2nd element from the last of list
#! Accessing tuple elements using index range
print(lst[1:3])
#! Accessing tuple elements using  negativeindex range
print(lst[-5:-1])
#! Modifying item
lst[2] = 0
print(lu, lst)
#! Finding length of list
print('Length of List:', len(lst))
#! Add items inside list using append
lst.append(6)  # ? Adds element at the last
print(lu, lst)
#! Add items inside list using insert
lst.insert(1, 7)  # ? Adds element '7' at the second position
print(lu, lst)
#! Remove items inside list using remove
lst.remove(6)  # ? Removes the element '6'
print(lu, lst)
#! Remove items inside list using pop
lst.pop(1)  # ? Removes the element from index 1
lst.pop()  # * Removes the last element of the list
print(lu, lst)
#! Remove items inside list using del
del lst[2]  # ? Removes the element from index 2
print(lu, lst)
#! Remove all items inside list using clear()
lst = [1, 2, 3, 4, 5]
print('Before clear():', lst)
lst.clear()  # ? Removes all elements
print('After clear():', lst)
#! Deleting List using del
del lst  # ? Deletes the list
print("List Deleted!")
#! Search item in list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(l, lst)
search = 7
for i, j in enumerate(lst):
    if search == lst[j]:
        print(f'{search} found at index {i+1} and at position {i+2}')
        break
    else:
        continue
else:
    print(f'{search} not in list!')
#! Copying List using copy()
listA = ['C', 'C++', 'Java', 'Python']
listB = listA.copy()  # ? Copies the list
print(listB)
#! Concatenate two lists
list1 = ['A', 'B', 'C', 'D', 'E']
list2 = [1, 2, 3, 4, 5]
list3 = list1+list2  # ? Concatenates two lists
print(list3)
#! Reverse List
lst1 = [1, 2, 3, 4, 5]
print('List before Reverse:', lst1)
print('List after Reverse:', lst1[::-1])  # ? Lsit Slicing Done
#! Sort List using sort()
lstx = [1, 5, 7, 3, 9, 4, 5, 0]
print(l, lstx)
lstx.sort()  # ? Sorting List
print(slr, lstx)
lstx.sort(reverse=True)
print(slrt, lstx)
#! ---------------------MULTI DIMENSIONAL LIST--------------------
mList = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [2, 4, 6, 8, 10]]
print(mList)
#! Accessing list elements
for i in range(len(mList)):
    for j in range(len(mList[i])):
        print(mList[i][j], end=" ")
    print()
#! Create list with zero filled
r = 4
c = 3
mlst = [[0 for x in range(r)] for x in range(c)]
print('Mutli dimensional list:', mlst)
#! Add sublist using append()
mlist1 = [[1, 2, 3], [4, 5, 6]]
print(mlist1)
mlist1.append([7, 8, 9])
print(mlist1)
#! Adding more items using sublist extend()
mlist2 = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
print(mlist2)
mlist2[2].extend([4, 5, 6])  # ? Adds at the extension of last element
print(mlist2)
#! Reverse List
mlist2 = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
print('List before Reverse:', mlist2)
print('List after Reverse:', mlist2[::-1])  # ? Lsit Slicing Done
#! Sort List using sort()
mlist2 = [[11, 2, 23], [2, 14, 9], [1, 8, 7]]
print(l, mlist2)
mlist2.sort()  # ? Sorting List
print(slr, mlist2)
mlist2.sort(reverse=True)
print(slrt, mlist2)
#! Sort sublist using sort()
mlist2 = [[11, 2, 23], [2, 14, 9], [1, 8, 7]]
print(l, mlist2)
mlist2[1].sort()  # ? Sorting sub list
print(slr, mlist2)
mlist2[1].sort(reverse=True)
print(slrt, mlist2)
print('\nHit Enter to End.......')
input()
