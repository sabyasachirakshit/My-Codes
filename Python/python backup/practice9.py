import random
print("Numbers of friends name do you want to take")
var1=int(input())
print(f"enter {var1} name" )
firstn=[]
lastn=[]
for i in range(var1):
    intput1=input()
    var2=intput1.split()
    a=(var2[len(var2)-2])
    firstn.append(a)
    b=(var2[len(var2)-1])
    lastn.append(b)
for item in firstn:
    fun1=random.choice(lastn)
    print(f"{item} {fun1}")





