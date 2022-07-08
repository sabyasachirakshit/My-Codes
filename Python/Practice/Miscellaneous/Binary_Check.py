number=input("Enter number:")
bin_verify=["0","1"]
for i in str(number):
    if i not in bin_verify:
        print(f"{number} is not binary")
        break
else:
    print(f"{number} is binary")