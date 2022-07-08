str=input("Enter String:")
rev_str=str[::-1]
if(str==rev_str):
    print(f"String {str} is palindrome!")
else:
    print(f"String {str} is not palindrome!")