size=int(input("Enter size of list:"))
index=1
lst=[]
while(size!=0):
    el=int(input(f"Enter element {index}: "))
    lst.append(el)
    index+=1
    size-=1
loop_starter=1
while(loop_starter!=len(lst)):
    if loop_starter%2!=0:
        print(lst[loop_starter-1],end="")
    loop_starter+=1

