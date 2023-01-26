
list1=[]
list2=[]
c=1
def rohanmul(input1):
    for i in range(1,11):
       global var1
       var1=i*input1
       if var1==24:
          list1.append(var1+2)
       else:
           list1.append(var1)
    return list1
def iscorrect(input1):
    for i in range(1,11):
       global var2
       var2=i*input1
       list2.append(var2)
    for item in list1:
        if item not in list2:
         print(f"{item} is not correct ")
    return f"There correct table is {list2}"
print("enter a number")
input1=int(input())
print(rohanmul(input1))
print(iscorrect(input1))

