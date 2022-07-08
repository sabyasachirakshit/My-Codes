str=input("Enter String:")
vowel=['a','e','i','o','u']
vc=0
cc=0
lst=[]
for i in str:
    lst.append(i)
    if i in vowel:
        vc+=1
    else:
        cc+=1
f_str=""
if vc>cc:
    lst.sort()
    for i in lst:
        f_str+=i
else:
    lst.sort()
    for i in lst[::-1]:
        f_str+=i
print(f_str)