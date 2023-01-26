print("How many apples do you want to share?")
n=int(input())
print("enter the minimum number apple per people ")
mn=int(input())
print("enter the maximum number apple per people ")
mx=int(input())
for i in range(mn,mx+1):
    if n%i==0:
        print(i,"apples per people are divisible")
    else:
        print(i,"apples per people are not divisible")
