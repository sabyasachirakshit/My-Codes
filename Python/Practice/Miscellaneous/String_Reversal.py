# Method 1
same_sent="Enter String:"
string = input(same_sent)
string = string[::-1]
print(string)

# Method 2

string2 = input(same_sent)
for i in reversed(string2):
    print(i, end="")

# Method 3

print("\n")
string3 = input(same_sent)
lst=list(string3)
i=len(lst)-1
while(i!=-1):
    print(lst[i],end="")
    i-=1