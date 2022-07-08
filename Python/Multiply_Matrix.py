lst1 = []
lst2 = []
lst = []
count = 1
m1 = 'Enter dimension of your Matrix 1:'
m2 = 'Enter dimension of your Matrix 2:'
m11 = "Matrix 1:"
m22 = "Matrix 2:"
size1 = int(input(m1))
i = 1
lst3 = []
l3 = []
while i <= size1:
    j = 1
    lst = []
    l3 = []
    while(j <= size1):
        element = int(input(f'Enter element {count}:'))
        lst.append(element)
        l3.append(element)
        j += 1
        count += 1
    lst1.append(lst)
    lst3.append(l3)
    i += 1
print(m11, lst1)
count = 1
size2 = int(input(m2))
i = 1
while i <= size2:
    j = 1
    lst = []
    while(j <= size2):
        element = int(input(f'Enter element {count}:'))
        lst.append(element)
        j += 1
        count += 1
    lst2.append(lst)
    i += 1
print(m22, lst2)
i = 0
j = 0
k = 0
while i < size1:
    j = 0
    while(j < size1):
        k = 0
        lst3[i][j] = 0
        while (k < size1):
            lst3[i][j] += lst1[i][k]*lst2[k][j]
            k += 1
        j += 1
    i += 1
print('Multiplication of Matrix 1 and Matrix 2 is:', lst3)