lst=[1,5,0,0,0,0,4,9,0]
number=[1,2,3,4,5,6,7,8,9]
num=[]
import random
for i in lst:
    if i!=0:
        num.append(i)
print(num)
x=0

def fill_list(lst,num,number):
    for pos,value in enumerate(lst):
        if value==0:
            x=random.choice(number)
            while x in num:
                x=random.choice(number)
            if x not in num:
                lst.remove(value)
                lst.insert(pos,x)
                num.append(value)
    print(lst)
    return lst

def count(lst, value):
    c = 0
    for i in lst:
        if i == value:
            c += 1
    return c

while True:
    for pos,value in enumerate(lst):
        while count(lst,value)!=1:
            lst=fill_list(lst,num,number)
            break
        if pos==len(lst)-1 and count(lst,value)==1:
            break
        else:
            continue
    break


print(lst)

