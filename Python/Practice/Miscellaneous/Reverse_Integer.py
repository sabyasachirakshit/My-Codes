number=int(input("Enter Number:"))
reverse=0
temp=number
while number!=0:
    reverse=reverse*10+number%10
    number//=10
print(f"After reversing the number {temp}, it becomes {reverse}")