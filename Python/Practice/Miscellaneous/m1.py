import numpy
n,k=input().split()
n=int(n)
k=int(k)
lst=[int(i) for i in input().split()]
new_lst=numpy.roll(lst,k)
for i in new_lst:
    print(f"{i} ",end="")
    