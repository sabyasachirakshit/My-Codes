def extendList(val,list_x=[]):
    list_x.append(val)
    print(list_x)
    return list_x
lst1=extendList(10)
print("l1=",lst1)
lst2=extendList(123,[])
print("l2=",lst2)
lst3=extendList("a")
print("l3=",lst3)
print("lst1=",lst1)
print("lst2=",lst2)
print("lst3=",lst3)
extendList(9)
