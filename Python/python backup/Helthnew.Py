print("You want to lock or retrieve?\nPress l for lock and press r for retrieve.")
var1 = input(" ")
if var1=="l":
    print("You want to lock for :\n Afridi  --  press 5\n Ronit  --  press 21\n Sabyasachi  --  press 19")
    var2 = int(input())
    if var2 == 5 :
        print("You want to lock:\n Diet  --  press d\n Exercise -- press e")
        var4 = input()
        if var4=="d":
            print("Enter your data")
            afridi=input()
            f1=open("AfridiDiet.txt","a")
            f1.write(afridi)
            f1.close()
            while(True):
                print("do you want a new line,press Y or N")
                var10 = input()
                if var10=="Y":
                    print("Enter your data")
                    afridi = input()
                    f1 = open("AfridiDiet.txt", "a")
                    f1.write(afridi)
                    f1.close()
                    continue
                else:
                    break
            print("You file is saved")
        elif var4=="e":
            print("Enter your data")
            afridi1 = input()
            f2 = open("AfridiExer.txt", "a")
            f2.write(afridi1)
        else:
            print("You entered wrong input")
    elif var2 == 21 :
        print("You want to lock:\n Diet  --  press d\n Exercise -- press e")
        var5 = input()
        if var5=="d":
            print("Enter your data")
            ronit=input()
            f3=open("RonitDiet.txt","a")
            f3.write(ronit)
        elif var5=="e":
            print("Enter your data")
            ronit1 = input()
            f4 = open("RonitExer.txt", "a")
            f4.write(ronit1)
        else:
            print("You entered wrong input")
    elif var2 == 19 :
        print("You want to lock:\n Diet  --  press d\n Exercise -- press e")
        var6 = input()
        if var6=="d":
            print("Enter your data")
            sabya=input()
            f5=open("SabyaDiet.txt","a")
            f5.write(sabya)
        elif var6=="e":
            print("Enter your data")
            sabya1 = input()
            f6 = open("SabyaExer.txt", "a")
            f6.write(sabya1)
        else:
            print("You entered wrong input")
elif var1=="r":
    print("You want to retrieve for :\n Afridi  --  press 5\n Ronit  --  press 21\n Sabyasachi  --  press 19")
    var3 = int(input())
    if var3 == 5 :
        print("You want to retrieve:\n Diet  --  press d\n Exercise -- press e")
        var7 = input()
        if var7=="d":
            f1=open("AfridiDiet.txt")
            cont1=f1.read()
            print(cont1)
        elif var7=="e":
            f2 = open("AfridiExer.txt")
            cont2 = f2.read()
            print(cont2)
        else:
            print("You entered wrong input")
    elif var3 == 21 :
        print("You want to retrieve:\n Diet  --  press d\n Exercise -- press e")
        var8 = input()
        if var8=="d":
            f3=open("RonitDiet.txt")
            cont3=f3.read()
            print(cont3)
        elif var8=="e":
            f4 = open("RonitExer.txt", "a")
            cont4 = f4.read()
            print(cont4)
        else:
            print("You entered wrong input")
    elif var3 == 19 :
        print("You want to lock:\n Diet  --  press d\n Exercise -- press e")
        var9 = input()
        if var9=="d":
            f5=open("SabyaDiet.txt")
            cont5 = f5.read()
            print(cont5)
        elif var9=="e":
            f6 = open("SabyaExer.txt")
            cont6 = f6.read()
            print(cont6)
        else:
            print("You entered wrong input")
else:
    print("You entered wrong input")


