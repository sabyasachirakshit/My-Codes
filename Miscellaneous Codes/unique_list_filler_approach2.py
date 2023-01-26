import random
ununique_lst=[1,0,0,0,2,3,9,7,0]
unique_lst=[]
number=[1,2,3,4,5,6,7,8,9]

for value in ununique_lst:
    if value!=0:
        unique_lst.append(value)


for pos,value in enumerate(ununique_lst):
    if value==0:
        ununique_lst.remove(value)
        value=random.choice(number)
        while value in unique_lst:
            value=random.choice(number)
        ununique_lst.insert(pos,value)
        unique_lst.append(value)

print(ununique_lst)



    
