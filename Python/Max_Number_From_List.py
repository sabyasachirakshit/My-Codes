L = int(input('Please enter the size of list:'))
lst = []
i = 1
while L != 0:
    element = int(input(f'Enter Element {i} = '))
    lst.append(element)
    i += 1
    L -= 1
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
print(f'Max number from {lst} is {lst[len(lst)-1]}')
print('\nHit Enter to End.......')
input()
