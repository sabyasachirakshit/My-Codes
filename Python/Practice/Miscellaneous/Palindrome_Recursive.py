n=int(input("Enter number:"))

def reverse(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(reverse(n//10)))

def ispalindrome(n):
    if(n==reverse(n)):
        print(f"{n} is Palindrome!")
    else:
        print(f"{n} is not Palindrome!")

ispalindrome(n)