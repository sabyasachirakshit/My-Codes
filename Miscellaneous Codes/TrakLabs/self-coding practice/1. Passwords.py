n=input("Number of users registered: ")
array=input("enter strings: ").split(",")
new_array=[]
for i in array:
    if i[0]=='{':
        new_array.append(i.replace('{',''))
    if i[len(i)-1]=='}':
        new_array.append(i.replace('}',''))
temp=0
newest_array=[]
for i,j in enumerate(new_array):
    if i!=0:
        newest_array.append(j)
distinct_password=1
condition=True
for element in newest_array:
    for i in range(0,len(element)):
        for j in range(0,len(element)):
            if((i+j)%2==0):
                element=list(element)
                element[i],element[j]=element[j],element[i]
                element=''.join(element)
                if element==new_array[0]:
                    condition=False
if condition==True:
    distinct_password+=1
print(distinct_password)