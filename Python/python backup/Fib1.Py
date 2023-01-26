def fibo1(n):
    if n<0:
        print("incorect")
    elif n ==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)
num=int(input("enter no"))
f=1
while(f<=num):
 print(fibo1(f))
 f=f+1


