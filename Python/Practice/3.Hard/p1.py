import math
print('Enter Coordinate 1:')
lst1, lst2, lst3 = [], [], []
i = 1
while(i <= 2):
    lst1.append(int(input()))
    i += 1
print('Enter Coordinate 2:')
i = 1
while(i <= 2):
    lst2.append(int(input()))
    i += 1
print('Enter Coordinate 3:')
i = 1
while(i <= 2):
    lst3.append(int(input()))
    i += 1
side1 = ((lst2[0]-lst1[0])**2)+((lst2[1]-lst1[1])**2)
side2 = ((lst3[0]-lst2[0])**2)+((lst3[1]-lst2[1])**2)
side3 = ((lst2[0]-lst1[0])**2)+((lst2[1]-lst1[1])**2)
s1 = math.sqrt(side1)
s2 = math.sqrt(side2)
s3 = math.sqrt(side3)
print('Perimeter:', round((s1+s2+s3), 2))
