print("How many numbers do you want to take")
var1=int(input())
print(f"enter {var1} numbers" )
list1=[]
for i in range(var1):
    intput1=int(input())
    for item in range(intput1,intput1*10):
        n1=item
        rev=0
        while(n1>0):
            a=n1%10
            rev=rev*10+a
            n1=n1//10
        if item==rev:
           list1.append(f"The next palindrome of {intput1} is {item}")
           break
for j in list1:
    print(j)

