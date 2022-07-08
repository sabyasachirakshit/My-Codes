number=int(input("Enter number:"))
reversed_number=0
actual_number=number
while(number!=0):
    reversed_number=reversed_number*10+number%10
    number//=10
if(actual_number==reversed_number):
    print(f"The number {actual_number} is Palindrome!")
else:
    print(f"The number {actual_number} is not Palindrome!")