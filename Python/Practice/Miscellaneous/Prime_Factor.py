number=int(input("Enter number:"))
i=2
def prime(n):
    i=2
    f=0
    while i<n:
        if(n%i==0):
            f=1
            break
        i+=1
    if f==0:
        print(f"Prime Factors->{n} ")
while i<number:
    if number%i==0:
        prime(i)
    i+=1