while(True):
    print("WELCOME TO SNAKE-WATER-GUN GAME ------> DEVELOPED BY - SK MD AFRIDI")
    i = 10
    str1 = int(input("How many rounds you want to play?\n"))
    t = str1
    while (str1 != 0):
        import random
        lst1 = ["SNAKE", "WATER", "GUN"]
        var = random.choice(lst1)
        var1 = input("Enter snake/water/gun:\n ")
        if var1.upper() == "SNAKE" and var == "WATER":
            print("You=", var1.upper(), " System=", var)
            print("You are winner")
            print("Your total score is", i)
            i += 10
        elif var1.upper() == "SNAKE" and var == "GUN":
            print("You=", var1.upper(), " System=", var)
            print("System is winner")
        elif var1.upper() == "SNAKE" and var == "SNAKE":
            print("You=", var1.upper(), " System=", var)
            print("Tie")
        elif var1.upper() == "WATER" and var == "SNAKE":
            print("You=", var1.upper(), " System=", var)
            print("System is winner")
        elif var1.upper() == "WATER" and var == "GUN":
            print("You=", var1.upper(), " System=", var)
            print("You are winner")
            print("Your total score is", i)
            i += 10
        elif var1.upper() == "WATER" and var == "WATER":
            print("You=", var1.upper(), " System=", var)
            print("Tie")
        elif var1.upper() == "GUN" and var == "SNAKE":
            print("You=", var1.upper(), " System=", var)
            print("You are winner")
            print("Your total score is", i)
            i += 10
        elif var1.upper() == "GUN" and var == "WATER":
            print("You=", var1.upper(), " System=", var)
            print("System IS winner")
        elif var1.upper() == "GUN" and var == "GUN":
            print("You=", var1.upper(), " System=", var)
            print("Tie")
        else:
            print("Wrong Input")
        str1 = str1 - 1
        t -= 1
        if t != 0:
            print(t, "Rounds are left")
        if str1 == 0:
            print("Game Over")
    print("Do you want to play again?\n Press y for yes and press n for no")
    play = input()
    if play != "y":
        print("We will meet soon")
        break
    else:
        continue
