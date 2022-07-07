while(True):
    print("WELCOME TO MY FAULTY CALCULATOR")
    n1 = int(input("Enter first number "))
    op = input("Enter operator(+,*,-,/) ")
    n2 = int(input("Enter second number "))

    if n1 * n2 == 45 * 3:
        print("555")
    elif n1 + n2 == 56 + 9:
        print("77")
    elif n1 / n2 == 56 / 6:
        print("4")
    elif op == '*':
        print(n1 * n2)
    elif op == '+':
        print(n1 + n2)
    elif op == '/':
        print(n1 / n2)
    elif op == '-':
        print(n1 - n2)
    else:
        exit()
    print("Do you want to calculate again??? ")
    print("If YES Type Y , If NO Type N")
    res = input()
    if res != "Y":
        print("We will meet soon")
        break
    else:
        continue

