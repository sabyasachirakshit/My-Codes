i= 10
t= 10
num = 15
a=i+1
while(i!=0):
    var = int(input("Enter the no "))
    if var==num:
        print("You Are Won and you have done within ",a-i,"attemp")
        break
    elif ((var<num and var>9)or (var>num and var<21)):
        print("You are too close")
    elif (var<=9 and var >= 0) :
        print("go up")
    elif var >= 21 and var<=30:
        print("go little down")
    elif var >30:
        print("you are too far,go down")
    elif var<0:
        print("you are too far,go up")
        continue
    i-=1
    t-=1
    if t!=0:
        print(t,"Guesses are left")
    if i==0:
        print("Game over, The actual no was ",num)

