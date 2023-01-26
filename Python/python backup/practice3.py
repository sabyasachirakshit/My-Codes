cal=[12,75,4,63,50]
list2=cal[::-1]
lenth=len(cal)
list1=[]
for i in range(lenth):
   list1.append(cal[lenth-i-1])
cal.reverse()
if list1==list2 and list1==cal:
    print("Three ways return same list")