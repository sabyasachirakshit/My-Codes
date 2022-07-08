"""
todo: In this program, our objective is to implement linear search on a list.
!Linear search is searching element on by one in the whole list.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
flag = 0
print(lst)
search = int(input('\nEnter search element:'))
for i in lst:
    if search == i:
        print(f'{search} found in list!')
        flag = 1
        break
if(flag == 0):
    print(f'{search} not found in list!')
print('\nHit Enter to End.......')
input()
