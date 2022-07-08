"""
? In this program, our objective is to perform basic arithmetic operation except division on two matrices.
"""
print('1.Add two matrices')
print('2.Substract two matrices')
print('3.Multiply two matrices')
print('4.Transpose a matrix')
choice = int(input('Enter choice(1-4):'))
lst1 = []
lst2 = []
lst = []
count = 1
m1 = 'Enter dimension of your Matrix 1:'
m2 = 'Enter dimension of your Matrix 2:'
m11 = "Matrix 1:"
m22 = "Matrix 2:"
if choice == 1:
    size1 = int(input(m1))
    i = 1
    while i <= size1:
        j = 1
        lst = []
        while(j <= size1):
            element = int(input(f'Enter element {count}:'))
            lst.append(element)
            j += 1
            count += 1
        lst1.append(lst)
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
    sum_of_lst = []
    lst = []
    i = 1
    while i <= size1:
        j = 1
        lst = []
        while(j <= size1):
            lst.append(lst1[i-1][j-1]+lst2[i-1][j-1])
            j += 1
            count += 1
        sum_of_lst.append(lst)
        i += 1
    print('Sum of Matrix 1 and Matrix 2 is:', sum_of_lst)
elif choice == 2:
    size1 = int(input(m1))
    i = 1
    while i <= size1:
        j = 1
        lst = []
        while(j <= size1):
            element = int(input(f'Enter element {count}:'))
            lst.append(element)
            j += 1
            count += 1
        lst1.append(lst)
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
    sub_of_lst = []
    lst = []
    i = 1
    while i <= size1:
        j = 1
        lst = []
        while(j <= size1):
            lst.append(lst1[i-1][j-1]-lst2[i-1][j-1])
            j += 1
            count += 1
        sub_of_lst.append(lst)
        i += 1
    print('Substracrtion of Matrix 1 and Matrix 2 is:', sub_of_lst)
elif choice == 3:
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
elif choice == 4:
    matrix = []
    size = int(input('Enter dimension of your Matrix :'))
    i = 1
    j = 1
    matrix2 = []
    lst2 = []
    while i <= size:
        j = 1
        lst = []
        lst2 = []
        while(j <= size):
            element = int(input(f'Enter element {count}:'))
            lst.append(element)
            lst2.append(element)
            j += 1
            count += 1
        matrix.append(lst)
        matrix2.append(lst2)
        i += 1
    print("Matrix:", matrix)
    i = 0
    j = 0
    while i < size:
        j = 0
        while j < size:
            matrix2[i][j] = matrix[j][i]
            j += 1
        i += 1
    print('Transposed Matrix:', matrix2)
print('\nHit Enter to End.......')
input()
